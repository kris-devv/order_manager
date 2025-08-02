import sys
import os
import pandas as pd

from core import *
from ui_compiled import *

os.environ["QT_FONT_DPI"] = "96"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO: Enable custom title bar
        
        # Window Title
        # ///////////////////////////////////////////////////////////////
        title = "MF-COMP"
        description = "Serwis komputerowy."

        self.setWindowTitle(title)
        self.ui.topMenuLabel.setText(description)

        UIFunctions.uiDefinitions(self)

        self.excel_controller = ExcelController()

        # Buttons Clicks
        # ///////////////////////////////////////////////////////////////
        self.ui.btnHome.clicked.connect(lambda: self.ui.rightStackedWidget.setCurrentWidget(self.ui.homePage))
        self.ui.addOrderButton.clicked.connect(lambda: self.ui.rightStackedWidget.setCurrentWidget(self.ui.addPage))
        self.ui.infoPageEditButton.clicked.connect(lambda: self.ui.rightStackedWidget.setCurrentWidget(self.ui.editPage))

        self.ui.infoPagePrintButton.clicked.connect(self.printOrder)

        self.ui.listWidget.itemClicked.connect(self.listWidgetClicked)

        self.ui.addPageConfirmButton.clicked.connect(self.confirmAddOrder)
        self.ui.addPageCancelButton.clicked.connect(lambda: self.ui.rightStackedWidget.setCurrentWidget(self.ui.homePage))

        self.ui.editPageConfirmButton.clicked.connect(self.confirmEditOrder)
        self.ui.editPageCancelButton.clicked.connect(lambda: self.ui.rightStackedWidget.setCurrentWidget(self.ui.homePage))

        def openCloseSettings():
            UIFunctions.toggleSettings(self, True)
        self.ui.settingsButton.clicked.connect(openCloseSettings)

        self.show()

        # Setup pages
        # ///////////////////////////////////////////////////////////////
        self.ui.rightStackedWidget.setCurrentWidget(self.ui.homePage)
        self.loadOrdersList()
    
    def confirmAddOrder(self):
        pass

    def confirmEditOrder(self):
        pass
    
    def printOrder(self):
        pass
        
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def loadOrdersList(self):
        self.ui.listWidget.clear()

        df = pd.read_excel("_dane/dane.xlsx")
        sorted_df = df.sort_values(['Zlecenie'], ascending=False)
        ordersIDs = sorted_df['Zlecenie'].tolist()
        ordersPhones = sorted_df['Nrtel'].tolist()
        isReady = pd.read_excel("_dane/dane.xlsx", index_col="Zlecenie")["Gotowe"]

        search_text = self.ui.searchBar.text().lower()

        try: 
            isNumber = search_text[0] == "+"
            searchPhone = search_text[1:].replace(" ", "")
        except: isNumber = False

        # Loading data to QListWidget
        for o, p in zip(ordersIDs, ordersPhones):
            if isNumber:
                if searchPhone in str(p):
                    item = QListWidgetItem(str(o))
                    item.setData(Qt.UserRole, o)
                    if isReady[o] == "nie":
                        item.setBackground(QColor(255,105,98))
                    elif isReady[o] == "tak":
                        item.setBackground(QColor(122, 189, 145))
                    self.ui.listWidget.addItem(item)
            elif search_text in str(o):
                item = QListWidgetItem(str(o))
                item.setData(Qt.UserRole, o)
                if isReady[o] == "nie":
                    item.setBackground(QColor(255,105,98))
                elif isReady[o] == "tak":
                    item.setBackground(QColor(122, 189, 145))
                self.ui.listWidget.addItem(item)

    def listWidgetClicked(self):
        self.ui.rightStackedWidget.setCurrentWidget(self.ui.infoPage)
        
        currentOrderID = self.ui.listWidget.currentItem().data(Qt.UserRole)
        self.ui.infoPageLabel.setText(f"Zlecenie nr. {currentOrderID}")

        # Loading data
        df = pd.read_excel("_dane/dane.xlsx")
        orderData = df.loc[df["Zlecenie"] == int(currentOrderID)].reset_index()

        phone = str(orderData["Nrtel"][0])
        if phone == "nan": phone = ''
        model = str(orderData["Model"][0])
        if model == "nan": model = ''
        desc = str(orderData["Opis"][0])
        if desc == "nan": desc = ''
        forUs = str(orderData["Dlanas"][0])
        if forUs == "nan": forUs = ''

        self.ui.infoPagePhoneLineEdit.setText(phone)
        self.ui.infoPageModelLineEdit.setText(model)
        self.ui.infoPageDescPlainTextEdit.setPlainText(desc)
        self.ui.infoPageForUsPlainTextEdit.setPlainText(forUs)

        if str(orderData["Gotowe"][0]) == "tak":
            self.ui.infoPageReadyCheckBox.setChecked(True)
        else:
            self.ui.infoPageReadyCheckBox.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())