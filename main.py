from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import wikipedia

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Search")
        self.setWindowIcon(QIcon("E:\\Python\\Wikipedia Search\\search.ico"))
        #self.setGeometry(150, 100, 1100, 600)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color:#343434;")
        self.UIComponents()
        self.setFocus()
        self.show()

    def UIComponents(self):
        self.ent = QLineEdit(self)
        self.ent.setClearButtonEnabled(True)
        self.ent.returnPressed.connect(self.search)
        self.ent.setStyleSheet("font-size:25px;font:baloo 2;background-color:#ffffff;border-radius:15px;")
        self.ent.setAlignment(Qt.AlignCenter)
        self.ent.setPlaceholderText("Type Here to Search")
        self.ent.resize(600, 35)
        self.ent.move(100, 30)

        self.btn = QPushButton(self)
        self.btn.setIcon(QIcon("searc.ico"))
        self.btn.setStyleSheet("background-color:#b0b057;border-radius:15px;")
        self.btn.setText("Search")
        self.btn.move(350, 130)
        self.btn.clicked.connect(self.search)

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.textEdit.move(50, 200)
        self.textEdit.resize(700, 350)
        self.textEdit.setStyleSheet("background-color:#ffffff;font-size:20px;border-radius:15px;color:#000000;")

    def search(self):
        self.s = self.ent.text()
        try:
            answer = wikipedia.summary(self.s)
            self.textEdit.setText(answer)

        except:
            self.textEdit.setText("An error occured")

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())

# import cv2
# from pyzbar.pyzbar import decode, ZBarSymbol

# # Image.open('barcode1.png')  # if use PIL library
# im = cv2.imread("qrcode1.png")  # if use cv2

# # codes = decode(im, symbols=[ZBarSymbol.QRCODE])  # specify code type
# codes = decode(im)  # auto detect code type
# print('Decoded:', codes)

# for code in codes:
#     data = code.data.decode('ascii')
#     print('Data:', code.data.decode('ascii'))
#     print('Code Type:', code.type)
#     print('BBox:', code.rect)
#     x, y, w, h = code.rect.left, code.rect.top, \
#                  code.rect.width, code.rect.height
#     cv2.rectangle(im, (x,y),(x+w, y+h),(255, 0, 0), 8)
#     print('Polygon:', code.polygon)
#     cv2.rectangle(im, code.polygon[0], code.polygon[1],
#                   (0, 255, 0), 4)

#     txt = '(' + code.type + ')  ' + data
#     cv2.putText(im, txt, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

# text1 = 'No. Codes: %s' % len(codes)
# cv2.putText(im, text1, (5, 15),
#             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# cv2.imshow('bounding box', im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()