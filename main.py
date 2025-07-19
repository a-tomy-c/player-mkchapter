import os
from PySide6.QtWidgets import QWidget
from skin_mkchapter import Ui_PlayerMakeChapter


class MakeChapters(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PlayerMakeChapter()
        self.ui.setupUi(self)
        self.__configs_makechapters()

    def __configs_makechapters(self):
        self.ui.splitter_h.setSizes([10,1])
        self.ui.splitter_h.setStretchFactor(0, 1)
        # self.ui.splitter_h.setStretchFactor(1, 0)
        self.ui.fm_chapters.setMinimumWidth(150)
        self.ui.splitter_v.setSizes([4,1])
        self.ui.splitter_v.setStretchFactor(0, 1)
        self.ui.tex.setMinimumHeight(110)
        self.ui.lb_capture.setMinimumWidth(180)


if __name__=="__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)

    mc = MakeChapters()
    mc.show()

    sys.exit(app.exec())