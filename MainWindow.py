from PySide6.QtCore import (
    Signal,
    QSize,
    QObject,
    Slot
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QButtonGroup,
    QFileSystemModel,
    QSplitter
)

from MainWindow_ui import *


def buttons_icon_refresh(group: QButtonGroup, uncheck_icon: list, check_icon: list):
    buttons = group.buttons()
    for i, button in enumerate(buttons):
        if button.isChecked():
            button.setIcon(check_icon[i])
        else:
            button.setIcon(uncheck_icon[i])


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.left_button_checked_icons = None
        self.left_button_unchecked_icons = None
        self.left_buttons = None
        self.setup_left_button_group()

        self.left_pages = None
        self.folder_model = None
        self.setup_left_pages()

        self.elem_buttons = None
        self.set_up_elem_buttons()

        self.operation_button = None
        self.current_operation = "Choose"
        self.set_up_operation_buttons()

        self.current_operation_changed = Signal(str)

    def setup_left_button_group(self):
        self.left_buttons = QButtonGroup(self)
        self.left_buttons.addButton(self.folder_tab, 0)
        self.left_buttons.addButton(self.edit_tab, 1)
        self.left_buttons.addButton(self.solve_tab, 2)
        self.left_buttons.addButton(self.notes_tab, 3)
        self.left_buttons.addButton(self.report_tab, 4)
        self.left_buttons.setExclusive(True)
        self.left_button_unchecked_icons = [QIcon(":/tab_button/folder"),
                                            QIcon(":/tab_button/edit"),
                                            QIcon(":/tab_button/solve"),
                                            QIcon(":/tab_button/note"),
                                            QIcon(":/tab_button/report")]
        self.left_button_checked_icons = [QIcon(":/tab_button/folder_c"),
                                          QIcon(":/tab_button/edit_c"),
                                          QIcon(":/tab_button/solve_c"),
                                          QIcon(":/tab_button/note_c"),
                                          QIcon(":/tab_button/report_c")]
        buttons_icon_refresh(self.left_buttons,
                                  self.left_button_unchecked_icons,
                                  self.left_button_checked_icons)
        self.left_buttons.buttonClicked.connect(self.left_button_and_page_refresh)


    # left button group 的buttonClicked信号连接到这个槽
    def left_button_and_page_refresh(self, button):
        buttons_icon_refresh(self.left_buttons,
                             self.left_button_unchecked_icons,
                             self.left_button_checked_icons)
        index = self.left_buttons.id(button)
        self.left_page.setCurrentWidget(self.left_pages[index])

    # operation button 的buttonClicked连接到这个槽
    def send_operation_changed_signal(self, button):
        sig_dict = {
            self.add_button: "Placement",
            self.choose_button: "Choose",
            self.rotate_button: "Rotate",
            self.delete_button: "Delete",
            self.link_button: "Link",
            self.unlink_button: "Unlink"
        }
        self.board.setOperation(sig_dict[button])
        
    # elem button 的 buttonClicked 连接到这个槽
    def send_elem_changed_signal(self, button):
        elem_dict = {
            self.choose_node: "Node",
            self.choose_resistor: "Resistor",
            self.choose_capacitor: "Capacitor",
            self.choose_intuctor: "Inductor",
            self.choose_vs: "VoltageSource",
            self.choose_cvs: "CVoltageSource",
            self.choose_cs: "CurrentSource",
            self.choose_ccs: "CCurrentSource"
        }
        self.board.setIntendedDrawItemType(elem_dict[button])

    def setup_left_pages(self):
        self.left_pages = [self.folder_page,
                           self.edit_page,
                           self.solve_page,
                           self.notes_page,
                           self.report_page]
        self.folder_model = QFileSystemModel(self)
        self.folder_model.setRootPath("")
        self.folder_view.setModel(self.folder_model)

    def set_up_elem_buttons(self):
        self.elem_buttons = QButtonGroup(self)
        self.elem_buttons.addButton(self.choose_node, 0)
        self.elem_buttons.addButton(self.choose_resistor, 1)
        self.elem_buttons.addButton(self.choose_capacitor, 2)
        self.elem_buttons.addButton(self.choose_intuctor, 3)
        self.elem_buttons.addButton(self.choose_vs, 4)
        self.elem_buttons.addButton(self.choose_cvs, 5)
        self.elem_buttons.addButton(self.choose_cs, 6)
        self.elem_buttons.addButton(self.choose_ccs, 7)
        self.elem_buttons.setExclusive(True)
        self.elem_buttons.buttonClicked.connect(self.send_elem_changed_signal)

    def set_up_operation_buttons(self):
        self.operation_button = QButtonGroup(self)
        self.operation_button.addButton(self.add_button, 0)
        self.operation_button.addButton(self.choose_button, 1)
        self.operation_button.addButton(self.rotate_button, 2)
        self.operation_button.addButton(self.delete_button, 3)
        self.operation_button.addButton(self.link_button, 4)
        self.operation_button.addButton(self.unlink_button, 5)
        self.operation_button.setExclusive(True)
        self.operation_button.buttonClicked.connect(self.send_operation_changed_signal)


