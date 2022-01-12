
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DraggableWidget(QWidget):
    def __init__(self,name,image):
        super(DraggableWidget, self).__init__()
        self._name = name
        self._image = image

        layout = QHBoxLayout(self)
        imageLabel = QLabel(self)
        nameLabel = QLabel(self._name)
        self.pixmap = QPixmap(self._image)
        imageLabel.setPixmap(self.pixmap)
        imageLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setMinimumHeight(self.pixmap.height())
        nameLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(imageLabel)
        layout.addWidget(nameLabel)
        imageLabel.setStyleSheet("""
            background-color: white;
        """)
        nameLabel.setStyleSheet("""
            background-color: white;
            color: black;
            padding: 0px 10px 0px 10px;
        """)
        layout.setSpacing(0)
        layout.addStretch()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.name)
        mimedata.setImageData(self.pixmap.toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.pixmap.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    print("test")
    app = QApplication(sys.argv)
    window = DraggableWidget('test','dragAndDrop\\aquadopp.bmp')
    window.setGeometry(600, 100, 200, 30)
    window.show()
    sys.exit(app.exec_())