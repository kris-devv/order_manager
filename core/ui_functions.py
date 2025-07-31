from main import *

GLOBAL_STATE = 0

class UIFunctions(QMainWindow):
    def __init__(self):
        super().__init__()

    # Maximize / Restore
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE

        if GLOBAL_STATE == 0:
            self.normalGeometry = self.geometry()
            self.showMaximized()
            GLOBAL_STATE = 1
            # TODO: Change maximize button icon and tips
            # TODO: Hide size grips
        else:
            self.showNormal()
            GLOBAL_STATE = 0
            if self.normalGeometry is not None:
                self.setGeometry(self.normalGeometry)
            # TODO: Change maximize button icon and tips
            # TODO: Show size grips

    # Toggle settings
    # ///////////////////////////////////////////////////////////////
    def toggleSettings(self, toggle = False):
        if toggle:
            width = self.ui.settingsFrame.width()
            newWidth = 200

            if width == 0:
                newWidth = 200
            else:
                newWidth = 0
            
            self.right_box = QPropertyAnimation(self.ui.settingsFrame, b"minimumWidth")
            self.right_box.setDuration(500)
            self.right_box.setStartValue(width)
            self.right_box.setEndValue(newWidth)
            self.right_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.right_box.start()
    
    # Definitions
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        enable_custom_title_bar = True

        if enable_custom_title_bar:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                #if UIFunctions.returStatus(self):
                #   UIFunctions.maximize_restore(self)
                if event.buttons() == Qt.LeftButton:
                    self.move(event.globalPos() - self.dragPos + self.pos())
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.topMenu.mouseMoveEvent = moveWindow

        else:
            self.ui.styleSheet.setContentsMargins(0, 0, 0, 0)
            self.ui.btnMin.hide()
            self.ui.btnMax.hide()
            self.ui.btnClose.hide()
            #self.ui.frame_size_grip.hide()

        # Shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.styleSheet.setGraphicsEffect(self.shadow)

        # Buttons
        self.ui.btnMin.clicked.connect(lambda: self.showMinimized())
        self.ui.btnMax.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btnClose.clicked.connect(lambda: self.close())

        # TODO: Add resize grips