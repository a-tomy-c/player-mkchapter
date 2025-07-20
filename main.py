import os
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from skin_mkchapter import Ui_PlayerMakeChapter
from playerp6 import PlayerP6


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
        self.player = PlayerP6()
        self.ui.vly_player.addWidget(self.player)
        self.setAcceptDrops(True)
        self.player.setAcceptDrops(False)
        self.player.video_widget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.player.timer.timeout.connect(self.update_time_label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            filepath = urls[0].toLocalFile()
            print(filepath)
            self.player.set_videopath(filepath)
        event.acceptProposedAction()

    def update_time_label(self):
        res= self.player.get_current_time()
        self.ui.lb_time.setText(res)


if __name__=="__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)

    mc = MakeChapters()
    mc.show()

    sys.exit(app.exec())