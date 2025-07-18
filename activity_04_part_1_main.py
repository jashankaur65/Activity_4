"""A client program written to verify correctness of the activity classes."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# REQUIREMENT: import statements
from contact_list.contact_list import ContactList
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = ContactList()
    window.show()

    # Start the event loop
    sys.exit(app.exec())
