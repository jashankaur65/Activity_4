"""The module defines the ContactList class."""

__author__ = "Jashan"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import (
    QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel,
    QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
)


class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        #Initializes a new instance of the ContactList class.
        
        super().__init__()
        self.__initialize_widgets()
        self.__connect_signals()

    def __initialize_widgets(self):
        #Initializes the widgets on this Window.
        
       
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)

        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def __connect_signals(self):
        #Connects button signals to their respective slots.

        self.add_button.clicked.connect(self.on_add_contact)
        self.remove_button.clicked.connect(self.on_remove_contact)

    def on_add_contact(self):
        #Handles the event when Add Contact button is clicked.

        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and phone:
            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)
            self.contact_table.setItem(row_position, 0, QTableWidgetItem(name))
            self.contact_table.setItem(row_position, 1, QTableWidgetItem(phone))
            self.status_label.setText(f"Added contact: {name}")
            self.contact_name_input.clear()
            self.phone_input.clear()
        else:
            self.status_label.setText("Please enter a contact name and phone number.")
            QMessageBox.warning(self, "Input Error", "Both name and phone number are required.")

    def on_remove_contact(self):
        #Handles the event when Remove Contact button is clicked.

        selected_row = self.contact_table.currentRow()
        if selected_row >= 0:
            name_item = self.contact_table.item(selected_row, 0)
            name = name_item.text() if name_item else ""
            self.contact_table.removeRow(selected_row)
            self.status_label.setText(f"Removed contact: {name}")
        else:
            self.status_label.setText("Please select a row to be removed.")
            QMessageBox.warning(self, "Selection Error", "Please select a contact to remove.")
