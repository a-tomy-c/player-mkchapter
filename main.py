import os
from pathlib import Path
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer
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
        self.player.ui.sld_tiempo.sliderReleased.connect(self.update_time_label)
        self.ui.bt_backward.clicked.connect(self.backward_1s)
        self.ui.bt_forward.clicked.connect(self.forward_1s)
        self.ui.bt_capture.clicked.connect(self.capture_frame)

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
        now = self.player.get_current_time()
        self.ui.lb_time.setText(now)
        rem = self.player.get_time_rem()
        self.ui.lb_time_rem.setText(rem)

    def backward_1s(self):
        self.player._move_x_seg(-1)
        self.update_time_label()

    def forward_1s(self):
        self.player._move_x_seg(1)
        self.update_time_label()

    def capture_frame(self):
        # Capturar solo el área del widget de video (sin botones)
        try:
            # Obtener la pantalla actual
            screen = QApplication.primaryScreen()
            
            # Obtener la posición global del widget de video
            video_widget = self.player.video_widget
            global_pos = video_widget.mapToGlobal(video_widget.rect().topLeft())
            
            # Capturar solo el área del widget de video
            pixmap = screen.grabWindow(0, 
                                     global_pos.x(), 
                                     global_pos.y(),
                                     video_widget.width(), 
                                     video_widget.height())
            
            if not pixmap.isNull():
                timestamp = self.player.format_time(self.player.position)
                # filename = f"captura_{timestamp.replace(':', '.').replace('.', '-')}.png"
                filename = f"{timestamp.replace('.', ' ').replace(':', '.')}.jpg"
                
                file_path = filename
                video_path = self.player.current_filepath()
                if video_path:
                    path = Path(video_path)
                    parent = path.parent.as_posix()
                    file_path = os.path.join(parent, filename)
                
                if pixmap.save(file_path, "JPG"):
                    original_title = self.windowTitle()
                    self.setWindowTitle(f"{original_title} - ✓ Captura guardada!")
                    QTimer.singleShot(2000, lambda: self.setWindowTitle(original_title))
                else:
                    print("Error al guardar la captura")
            else:
                print("No se pudo capturar el frame")
                
        except Exception as e:
            print(f"Error al capturar frame: {e}")


if __name__=="__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)

    mc = MakeChapters()
    mc.show()

    sys.exit(app.exec())