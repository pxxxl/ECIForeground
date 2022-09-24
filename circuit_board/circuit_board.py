import copy
import json

from PySide6.QtWidgets import(
    QWidget,
    QPushButton
)
from PySide6.QtGui import (
    QPaintEvent,
    QMouseEvent, QPainter, QBrush, QPen, Qt
)

MAXIMUM_ITEMS_ALLOWED = 1000


'''
ItemType: Node, Resistance, Capacity, Inductance, VoltageSource,
CurrentSource, CVoltageSource, CCurrentSource, Impedance

Orientations : Right, Up, Down, Left
'''


"""
PaintType:Normal, Intention, Chosen,
CurrentToOrient, CurrentBackOrient

Operation:Placement, Remove, Rotate,
Choose, Connect, Disconnect
"""

"""
signals:
itemChosen(DrawItem
"""


class ECIBoard(QWidget):
    def __init__(self, *args, **kwargs):
        super(ECIBoard, self).__init__(*args, **kwargs)
        self.edge = 20
        self.dot_interval = 48
        self.dot_physical_radius = 3
        self.dot_sense_radius = 18
        self.item_line_width = 2

        self.elems = []
        self.intending_item_type = None
        self.intending_item = None
        self.chosen_place = (0, 0)
        self.linker = None
        self.voltage = {}  # {名字：值的列表}
        self.current = {}  # {名字：值的列表，且将与link保持同步}

        self.read_only = False
        self.intending_item_type = "Resistor"
        self.current_operation = "Choose"

        self.__name_alloc = 1
        pass

    def paintEvent(self, event: QPaintEvent) -> None:
        self.paintBackground()
        self.paintElems()
        self.paintLinks()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        i = self.widthReConvert(event.x())
        j = self.heightReConvert(event.y())
        flag = False

        match self.current_operation:
            case "Placement":
                if i != -1 and j != -1 and not self.read_only:
                    if self.isPlaceable(i, j, self.intending_item_type):
                        item_n = {
                            "name" :self.nameAlloc(),
                            "type": self.intending_item_type,
                            "orientation": "Left",
                            "x": str(i),
                            "y": str(j),
                            "properties": []
                        }
                        if self.intending_item_type == "Node":
                            self.elems.append(item_n)
                            self.current[item_n["name"]] = []
                        else:
                            self.elems.append(item_n)
                            if self.isPlaceable(i+1, j, "Node"):
                                self.elems.append({
                                    "name": self.nameAlloc(),
                                    "orientation": "Left",
                                    "type": "Node",
                                    "x": str(i+1),
                                    "y": str(j),
                                    "links": []
                                })
                            if self.isPlaceable(i-1, j, "Node"):
                                self.elems.append({
                                    "name": self.nameAlloc(),
                                    "orientation": "Left",
                                    "type": "Node",
                                    "x": str(i-1),
                                    "y": str(j),
                                    "links": []
                                })
                        self.repaint()
                        return
            case "Choose":
                if i != -1 and j != -1 and not self.read_only:
                    for elem in self.elems:
                        if elem["x"] == i and elem["y"] == j:
                            self.chosen_place = (i, j)
            case "Remove":
                if i != -1 and j != -1 and not self.read_only:
                    self.elems[:] = [elem for elem in self.elems if elem["x"] == i and elem["y"] == j]
            case "Rotate":
                if i != -1 and j != -1 and not self.read_only:
                    for elem in self.elems:
                        if elem["x"] == i and elem["y"] == j:
                            ori_map = {"Down": "Right",
                                       "Right": "Up",
                                       "Up": "Left",
                                       "Left": "Down"}
                            elem["orientation"] = ori_map[elem["orientation"]]
            case "Link":
                if i != -1 and j != -1 and not self.read_only:
                    if self.linker is None:
                        for elem in self.elems:
                            if elem["type"] == "Node":
                                self.linker = elem
                                self.linker["links"].append([])
                        return
                    else:
                        for elem in self.elems:
                            if elem["x"] == str("i") and elem["y"] == str("j") and elem["type"] == "Node":
                                # 发现点击到了结点，此时立即终结链接
                                self.linker["links"][-1].append(elem)
                                self.linker = None
                                return
                            if elem is self.linker:
                                # 点击自己取消链接
                                self.linker["links"].pop()
                                return
                            if elem["x"] == str("i") and elem["y"] == str("j"):
                                # 点击到了某个别的元件，取消链接
                                self.linker["links"].pop()
                                return
                        # 什么都没点到
                        self.linker["links"][-1].append([str("i"), str("j")])
            case "Unlink":
                if i != -1 and j != -1 and not self.read_only:
                    for elem in self.elems:
                        if elem["x"] == str("i") and elem["y"] == str("j") and elem["type"] == "Node":
                            elem["links"].clear()

    def mouseMoveEvent(self, event: QMouseEvent):
        i = self.widthReConvert(event.x())
        j = self.heightReConvert(event.y())
        match self.current_operation:
            case "Placement":
                if i != -1 and j != -1 and not self.read_only:
                    if self.isPlaceable(i, j, self.intending_item_type):
                        self.intending_item = {
                            "name": "",
                            "type": self.intending_item_type,
                            "Orientation": "Left",
                            "x": str(i),
                            "y": str(j),
                            "properties": []
                        }
                        self.repaint()
                        return
            case _:
                return

    def importJsonDocumentStorage(self, js) -> bool:
        self.clear()
        self.elems = json.load(js)
        # 接下来替换node的link
        name_dic = {node["name"]: node for node in self.elems if node["type"] == "Node"}
        for elem in self.elems:
            for link in elem["links"]:
                link[-1] = name_dic[link[-1]]
        return True

    def exportJsonDocumentStorage(self) -> str:
        data = copy.deepcopy(self.elems)
        for elem in data:
            for link in elem["links"]:
                link[-1] = link[-1]["name"]
        return json.dumps(data)

    def exportJsonDocumentTransport(self) -> str:
        data = {
            "protocol": "Static Transport Protocol",
            "version": "2.0",
            "circuit": {
                "nodes": [],
                "elems": [],
                "voltage": {},
                "current": {}
            }
        }
        circuit = data["circuit"]
        nodes = circuit["nodes"]
        elems = circuit["elems"]
        for elem in self.elems:
            if elem["type"] == "Node":
                for link in elem["links"]:
                    link[-1] = link[-1]["name"]
                nodes.append({"name": elem["name"], "links": elem["links"]})
            else:
                elem_f = {
                    "name": elem["name"],
                    "type": elem["type"],
                    "properties": elem["properties"],
                    "neighbor":[]
                }
        circuit["voltage"] = self.voltage
        circuit["current"] = self.current
        return json.dumps(data)

    def loadJsonDocumentResult(self, js):
        data = json.load(js)
        self.voltage = data["circuit"]["voltage"]
        self.current = data["circuit"]["current"]

    def setChosenItemProperty(self, name, properties) -> bool:
        for elem in self.elems:
            if elem["x"] == self.chosen_place[0] and elem["y"] == self.chosen_place[1]:
                if len([ele for ele in self.elems if ele["name"] == name]) == 0:
                    elem["name"] = name
                    elem["properties"] = properties
                    return True
        return False

    def getChosenItem(self):
        for elem in self.elems:
            if elem["x"] == self.chosen_place[0] and elem["y"] == self.chosen_place[1]:
                return elem
        return None

    def setIntendedDrawItemType(self, type):
        self.intending_item_type = type

    def setOperation(self, operation):
        self.current_operation = operation

    def clear(self):
        self.elems.clear()

    def widthConvert(self, i):
        i = int(i)
        return self.edge + i * self.dot_interval

    def heightConvert(self, j):
        j = int(j)
        return self.edge + j * self.dot_interval

    def widthReConvert(self, i):
        i = int(i)
        di = (i - self.edge) // self.dot_interval
        ins = (i - self.edge) - di * self.dot_interval
        mk = ins - self.dot_interval // 2
        if abs(mk) >= self.dot_interval // 2 - self.dot_sense_radius:
            if mk > 0:
                return di + 1
            elif mk < 0:
                return di
        return -1

    def heightReConvert(self, j):
        return self.widthReConvert(j)

    def paintBackground(self):
        painter = QPainter(self)
        brush = QBrush("#F7F7F7")
        painter.setBrush(brush)
        painter.setPen(QPen(brush, 0))
        height = int((self.height()) / self.dot_interval)
        width = int((self.width()) / self.dot_interval)
        painter.drawRect(0, 0, self.width(), self.height())

        painter.setBrush(Qt.gray)
        for i in range(0, int(width)):
            for j in range(0, int(height)):
                painter.drawEllipse(self.widthConvert(i) - self.dot_physical_radius,
                                    self.heightConvert(j) - self.dot_physical_radius,
                                    self.dot_physical_radius * 2,
                                    self.dot_physical_radius * 2)

    def paintElem(self, elem_type, orientation, x, y, paint_type):
        match elem_type:
            case "Node":
                self.paintNode(orientation, x, y, paint_type)
            case "Resistor":
                self.paintResistor(orientation, x, y, paint_type)
            case "Capacitor":
                self.paintCapacitor(orientation, x, y, paint_type)
            case "Inductor":
                pass
                self.paintInductor(orientation, x, y, paint_type)
            case "VoltageSource":
                self.paintVoltageSource(orientation, x, y, paint_type)
            case "CurrentSource":
                self.paintCurrentSource(orientation, x, y, paint_type)
            case "CVoltageSource":
                self.paintCVoltageSource(orientation, x, y, paint_type)
            case "CCurrentSource":
                self.paintCCurrentSource(orientation, x, y, paint_type)

    def paintElems(self):
        for elem in self.elems:
            if self.chosen_place == (elem["x"], elem["y"]):
                self.paintElem(elem["type"], elem["orientation"], int(elem["x"]), int(elem["y"]), "Chosen")
            else:
                self.paintElem(elem["type"], elem["orientation"], int(elem["x"]), int(elem["y"]), "Normal")
        if self.intending_item is not None and self.current_operation == "Placement":
            elem = self.intending_item
            self.paintElem(elem["type"], elem["orientation"], int(elem["x"]), int(elem["y"]), "Intention")

    def paintLinks(self):
        for elem in self.elems:
            if elem["type"] == "Node":
                begin = [int(elem["x"]), int(elem["y"])]
                for link in elem["links"]:
                    cursor = copy.deepcopy(begin)
                    for i in range(0, len(link) - 1):
                        target = [int(link[i][0]), int(link[i][1])]
                        self.paintLine(cursor, target, "Normal")
                        cursor = target
                    if isinstance(link[-1], list):
                        target = [int(link[-1][0]), int(link[-1][1])]
                        self.paintLine(cursor, target, "Normal")
                    else:
                        target = [int(link[-1]["x"]), int(link[-1]["y"])]
                        self.paintLine(cursor, target, "Normal")

    def paintNode(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = QPainter(self)
        match paint_type:
            case "Normal":
                painter.setBrush(Qt.green)
                painter.setPen(QPen(Qt.green, 0))
                painter.drawEllipse(
                    rx - self.dot_physical_radius,
                    ry - self.dot_physical_radius,
                    self.dot_physical_radius * 2,
                    self.dot_physical_radius * 2
                )
            case "Intention":
                pass
            case "Chosen":
                painter.setBrush(Qt.blue)
                painter.setPen(QPen(Qt.blue, 0))
                painter.drawEllipse(
                    rx - self.dot_physical_radius - 3,
                    ry - self.dot_physical_radius - 3,
                    (self.dot_physical_radius + 3) * 2,
                    (self.dot_physical_radius + 3) * 2
                )

    def paintResistor(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)
        if orientation == "Left" or orientation == "Right":
            painter.drawRect(rx - self.dot_interval // 2, ry - self.dot_interval // 4, self.dot_interval, self.dot_interval // 2)
            painter.drawLine(rx - self.dot_interval, ry, rx - self.dot_interval // 2, ry)
            painter.drawLine(rx + self.dot_interval, ry, rx + self.dot_interval // 2, ry)
        else:
            painter.drawRect(rx - self.dot_interval // 4, ry - self.dot_interval // 2, self.dot_interval // 2, self.dot_interval)
            painter.drawLine(rx, ry - self.dot_interval, rx, ry - self.dot_interval // 2)
            painter.drawLine(rx, ry + self.dot_interval, rx, ry + self.dot_interval // 2)
        

    def paintCapacitor(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)
        if orientation == "Left" or orientation == "Right":
            painter.drawLine(rx - self.dot_interval // 4, ry + self.dot_interval // 2, rx - self.dot_interval // 4, ry - self.dot_interval // 2)
            painter.drawLine(rx + self.dot_interval // 4, ry + self.dot_interval // 2, rx + self.dot_interval // 4, ry - self.dot_interval // 2)
            painter.drawLine(rx - self.dot_interval, ry, rx - self.dot_interval // 4, ry)
            painter.drawLine(rx + self.dot_interval, ry, rx + self.dot_interval // 4, ry)
        else:
            painter.drawLine(rx - self.dot_interval // 4, ry - self.dot_interval // 4, rx + self.dot_interval // 4, ry - self.dot_interval // 4)
            painter.drawLine(rx - self.dot_interval // 4, ry + self.dot_interval // 4, rx + self.dot_interval // 4, ry + self.dot_interval // 4)
            painter.drawLine(rx, ry - self.dot_interval, rx, ry - self.dot_interval // 4)
            painter.drawLine(rx, ry + self.dot_interval, rx, ry + self.dot_interval // 4)

    def paintInductor(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)

    def paintVoltageSource(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)
        if orientation == "Left" or orientation == "Right":
            painter.drawEllipse(rx - self.dot_interval // 2, ry - self.dot_interval // 2, self.dot_interval, self.dot_interval)
            painter.drawLine(rx - self.dot_interval, ry, rx + self.dot_interval, ry)
        else:
            painter.drawEllipse(rx - self.dot_interval // 2, ry - self.dot_interval // 2, self.dot_interval, self.dot_interval)
            painter.drawLine(rx, ry - self.dot_interval, rx, ry + self.dot_interval)


    def paintCVoltageSource(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)
        if orientation == "Left" or orientation == "Right":
            painter.drawLine(rx - self.dot_interval // 2, ry, rx, ry + self.dot_interval // 3)
            painter.drawLine(rx - self.dot_interval // 2, ry, rx, ry - self.dot_interval // 3)
            painter.drawLine(rx + self.dot_interval // 2, ry, rx, ry + self.dot_interval // 3)
            painter.drawLine(rx + self.dot_interval // 2, ry, rx, ry - self.dot_interval // 3)
            painter.drawLine(rx - self.dot_interval, ry, rx + self.dot_interval, ry)
        else:
            painter.drawLine(rx, ry - self.dot_interval // 2, rx + self.dot_interval // 3, ry)
            painter.drawLine(rx, ry - self.dot_interval // 2, rx - self.dot_interval // 3, ry)
            painter.drawLine(rx, ry + self.dot_interval // 2, rx + self.dot_interval // 3, ry)
            painter.drawLine(rx, ry + self.dot_interval // 2, rx - self.dot_interval // 3, ry)
            painter.drawLine(rx - self.dot_interval, ry, rx + self.dot_interval, ry)


    def paintCCurrentSource(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)
        if orientation == "Left" or orientation == "Right":
            painter.drawLine(rx - self.dot_interval // 2, ry, rx, ry + self.dot_interval // 3)
            painter.drawLine(rx - self.dot_interval // 2, ry, rx, ry - self.dot_interval // 3)
            painter.drawLine(rx + self.dot_interval // 2, ry, rx, ry + self.dot_interval // 3)
            painter.drawLine(rx + self.dot_interval // 2, ry, rx, ry - self.dot_interval // 3)
            painter.drawLine(rx - self.dot_interval, ry, rx - self.dot_interval // 2, ry)
            painter.drawLine(rx + self.dot_interval, ry, rx + self.dot_interval // 2, ry)
            painter.drawLine(rx, ry + self.dot_interval // 3, rx, ry - self.dot_interval // 3)
        else:
            painter.drawLine(rx, ry - self.dot_interval // 2, rx + self.dot_interval // 3, ry)
            painter.drawLine(rx, ry - self.dot_interval // 2, rx - self.dot_interval // 3, ry)
            painter.drawLine(rx, ry + self.dot_interval // 2, rx + self.dot_interval // 3, ry)
            painter.drawLine(rx, ry + self.dot_interval // 2, rx - self.dot_interval // 3, ry)
            painter.drawLine(rx, ry - self.dot_interval, rx, ry - self.dot_interval // 2)
            painter.drawLine(rx, ry + self.dot_interval, rx, ry + self.dot_interval // 2)
            painter.drawLine(rx + self.dot_interval // 3, ry, rx - self.dot_interval // 3, ry)
            painter = self.setUpPen(paint_type)

    def paintCurrentSource(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)
        if orientation == "Left" or orientation == "Right":
            painter.drawEllipse(rx - self.dot_interval // 2, ry - self.dot_interval // 2, self.dot_interval, self.dot_interval)
            painter.drawLine(rx - self.dot_interval, ry, rx - self.dot_interval // 2, ry)
            painter.drawLine(rx + self.dot_interval, ry, rx + self.dot_interval // 2, ry)
            painter.drawLine(rx, ry - self.dot_interval // 2, rx, ry + self.dot_interval // 2)
        else:
            painter.drawEllipse(rx - self.dot_interval // 2, ry - self.dot_interval // 2, self.dot_interval, self.dot_interval)
            painter.drawLine(rx, ry - self.dot_interval, rx, ry - self.dot_interval // 2)
            painter.drawLine(rx, ry + self.dot_interval, rx, ry + self.dot_interval // 2)
            painter.drawLine(rx - self.dot_interval // 2, ry, rx + self.dot_interval // 2, ry)


    def paintImpedance(self, orientation, x, y, paint_type):
        rx = self.widthConvert(x)
        ry = self.heightConvert(y)
        painter = self.setUpPen(paint_type)

    def paintLine(self, point1, point2, paint_type):
        painter = self.setUpPen(paint_type)
        painter.drawLine(self.widthConvert(point1[0]),
                         self.heightConvert(point1[1]),
                         self.widthConvert(point2[0]),
                         self.heightConvert(point2[1]))

    def setUpPen(self, paint_type):
        painter = QPainter(self)
        match paint_type:
            case "Normal":
                painter.setBrush(QBrush("#F7F7F7"))
                painter.setPen(QPen(Qt.black, self.item_line_width))
            case "Intention":
                painter.setBrush(QBrush("#F7F7F7"))
                painter.setPen(QPen(QBrush("#AAB1B1"), self.item_line_width))
            case "Chosen":
                painter.setBrush(QBrush("#F7F7F7"))
                painter.setPen(QPen(Qt.blue, self.item_line_width + 1))
        return painter

    def nameAlloc(self):
        self.__name_alloc += 1
        return "___" + str(self.__name_alloc)
        pass

    def isPlaceable(self, i, j, intending_type):
        for elem in self.elems:
            if type == "Node" or intending_type == "Node":
                if i == elem["x"] and j == elem["j"]:
                    return False
            else:
                if abs(i - int(elem["x"])) <= 1 and abs(j - int(elem["y"])) <= 1:
                    return False
        return True
