from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


# creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        width = 1280
        height = 720

        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.setStyleSheet("QLabel {font: 6pt SF Pro Display}")

        # creating a QWebEngineView
        self.browser = QWebEngineView()

        # setting default browser url as google
        self.browser.setUrl(QUrl("https://icloud.com/"))

        # adding action when url get changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)

        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)

        # creating a status bar object
        self.status = QStatusBar()

        # adding status bar to the main window
        self.setStatusBar(self.status)

        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")

        # adding this tool bar tot he main window
        self.addToolBar(navtb)

        # similarly for home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        mail_btn = QAction("Mail", self)
        mail_btn.setStatusTip("Go to iCloud Mail")
        mail_btn.triggered.connect(self.navigate_mail)
        navtb.addAction(mail_btn)

        photos_btn = QAction("Photos", self)
        photos_btn.setStatusTip("Go to iCloud Photos")
        photos_btn.triggered.connect(self.navigate_photos)
        navtb.addAction(photos_btn)

        drive_btn = QAction("Drive", self)
        drive_btn.setStatusTip("Go to iCloud Drive")
        drive_btn.triggered.connect(self.navigate_drive)
        navtb.addAction(drive_btn)

        notes_btn = QAction("Notes", self)
        notes_btn.setStatusTip("Go to iCloud Notes")
        notes_btn.triggered.connect(self.navigate_notes)
        navtb.addAction(notes_btn)


        # adding a separator in the tool bar
        navtb.addSeparator()

        # creating a line edit for the url
        self.urlbar = QLineEdit()
        self.urlbar.setReadOnly(True)
        # adding action when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding this to the tool bar
        navtb.addWidget(self.urlbar)

        # similarly for reload action
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # adding action to the reload button
        # making browser to reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # showing all the components
        self.show()

    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - iCloud Client (Created By Fosto)" % title)

    # method called by the home action
    def navigate_home(self):
        # open the google
        self.browser.setUrl(QUrl("https://icloud.com/"))

    def navigate_mail(self):
        self.browser.setUrl(QUrl("https://icloud.com/mail/"))

    def navigate_photos(self):
        self.browser.setUrl(QUrl("https://icloud.com/photos/"))

    def navigate_drive(self):
        self.browser.setUrl(QUrl("https://icloud.com/drive"))

    def navigate_notes(self):
        self.browser.setUrl(QUrl("https://icloud.com/notes/"))

    # method called by the line edit when return key is pressed
    def navigate_to_url(self):
        # getting url and converting it to QUrl object
        q = QUrl(self.urlbar.text())

        # if url is scheme is blank
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("http")

        # set the url to the browser
        self.browser.setUrl(q)

    # method for updating url
    # this method is called by the QWebEngineView object
    def update_urlbar(self, q):
        # setting text to the url bar
        self.urlbar.setText(q.toString())

        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)


# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("iCloud Client (Created By Fosto)")

# creating a main window object
window = MainWindow()

# loop
app.exec_()
