class Pages(MainWindow):
    def __init__(self):
        super().__init__()
        
    def add_order(self):
        self.ui.rightStackedWidget.setCurrentWidget(self.ui.addPage)
        self.excel_controller.add_order_to_excel()