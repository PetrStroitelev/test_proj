from typing import cast

from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QListWidget, QMainWindow, QPushButton, QStyle

from custom_q_list_widget_item import CustomQListWidgetItem
from dal import Migrator, Task


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        Migrator.start_migration()

        uic.loadUi('app.ui', self)
        add_button = cast(QPushButton, self.add_Button)
        del_button = cast(QPushButton, self.delete_Button)

        btn_styles = "QPushButton { background-color: #1F6AA5; border-radius: 5px; color: white; height: 25px; " \
                     "margin-top: 20px; }" \
                     "QPushButton:hover {background-color: #36719F}"

        add_button.setStyleSheet(btn_styles)
        del_button.setStyleSheet(btn_styles)

        add_button.clicked.connect(self._add_button_clicked)
        del_button.clicked.connect(self._delete_button_clicked)

        text_input = cast(QLineEdit, self.text_input)

        input_style = "QLineEdit{ background-color: #343638; border-radius: 5px; color: white; padding: 3px; " \
                      "border-style: outset; border-width: 1px; border-color: white; }"
        text_input.setPlaceholderText("Add Todo")
        text_input.setStyleSheet(input_style)

        self._load_data_from_db()

        self.show()

    def _load_data_from_db(self):
        list_view = cast(QListWidget, self.list_widget)

        for task in Task.get_all_tasks():
            item = CustomQListWidgetItem()
            item.setText(task.message)
            item.id = task.id
            list_view.addItem(item)

    def _delete_button_clicked(self):
        list_view = cast(QListWidget, self.list_widget)

        selected_items = list_view.selectedItems()
        for item in selected_items:
            Task.delete_task(item.id)
            list_view.takeItem(list_view.row(item))

    def _add_button_clicked(self):

        text_input = cast(QLineEdit, self.text_input)
        if text_input.text() == "":
            return

        list_view = cast(QListWidget, self.list_widget)

        text_ = text_input.text()
        task_id = Task.create_task(text_)

        item = CustomQListWidgetItem()
        item.setText(text_)
        item.id = task_id
        list_view.addItem(item)
        text_input.setText("")
