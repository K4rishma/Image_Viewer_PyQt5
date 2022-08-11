#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
import sys
module_path = os.path.abspath(os.getcwd())    

if module_path not in sys.path:       

    sys.path.append(module_path)
from PyQt5.QtWidgets import QVBoxLayout, QMenuBar, QWidget, QSizePolicy, QMainWindow, QApplication, QLabel, QFileDialog, QAction, QMenu
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt



class ImageWidget(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True)

    def hasHeightForWidth(self):
        return self.pixmap() is not None

    def heightForWidth(self, w):
        if self.pixmap():
            return int(w * (self.pixmap().height() / self.pixmap().width()))
        
class Label(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)


class ImageWidget(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True)

    def hasHeightForWidth(self):
        return self.pixmap() is not None

    def heightForWidth(self, w):
        if self.pixmap():
            return int(w * (self.pixmap().height() / self.pixmap().width()))


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.lay = QVBoxLayout(self)
        self.lb = Label(self)
        self.menubar = QMenuBar()
        
        self.fileMenu = QMenu(' &File')
        self.menubar.addMenu(self.fileMenu)
        
        self.fileMenu.addAction(' &Open Image')
        self.fileMenu.triggered.connect(self.openImage) 
        
        self.fileMenu.addAction(' &View/Keep aspect ratio')
        self.fileMenu.triggered.connect(self.keepRatio)
        
        self.lay.addWidget(self.lb)
        self.lay.setMenuBar(self.menubar)
        
    def openImage(self):

        
        self.image_path, _ = QFileDialog.getOpenFileName()
        self.pixmap = QPixmap(self.image_path)
        self.lb.setPixmap(self.pixmap)
        
        

    def keepRatio(self):

        ImageWidget(self.lb)
        self.lb.resize(self.pixmap.size())
        
            
def main():
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 


# In[ ]:


# import sys
# from PyQt5.QtWidgets import QVBoxLayout, QMenuBar, QWidget, QSizePolicy, QMainWindow, QApplication, QLabel, QFileDialog, QAction, QMenu
# from PyQt5.QtGui import QPixmap, QPainter
# from PyQt5.QtCore import Qt

# class Label(QWidget):
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent=parent)
#         self.p = QPixmap()

#     def setPixmap(self, p):
#         self.p = p
#         self.update()

#     def paintEvent(self, event):
#         if not self.p.isNull():
#             painter = QPainter(self)
#             painter.setRenderHint(QPainter.SmoothPixmapTransform)
#             painter.drawPixmap(self.rect(), self.p)

# class MainWindow(QMainWindow):

#     def __init__(self, parent = None):
#         super(MainWindow, self).__init__(parent)
#         self.widget = QWidget()
#         self.lay = QVBoxLayout(self.widget)
#         self.lb = Label(self.widget)
#         self.setCentralWidget(self.lb)
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu(' &File')
#         self.resize(500, 500)
        
#         # sets the background colour of the dialog box
#         self.setStyleSheet("background-color: yellow;")
        
#         # prompts the user to load the image
#         openAction = QAction(' &Open Image', self)  
#         openAction.triggered.connect(self.openImage) 
#         fileMenu.addAction(openAction)

        
#         # exits the application
#         closeAction = QAction(' &Exit', self)  
#         closeAction.triggered.connect(self.close) 
#         fileMenu.addAction(closeAction)
        
#         # scales the image while maintaining its aspect ratio
#         ratioAction = QAction(' &Aspect Ratio', self)  
#         ratioAction.triggered.connect(self.maintainRatio) 
#         fileMenu.addAction(ratioAction)
        
        
        
#         # self.lay.setMenuBar(self.menubar)


#     def openImage(self):
#         # image fits the window size upon maximizing the dialog box
#         # imagePath, _ = QFileDialog.getOpenFileName()
#         # pixmap = QPixmap(imagePath)
#         # self.pixmap = pixmap
#         # pixmap = self.pixmap.scaled(self.width(), 
#         #                 self.height())
#         # self.label.setPixmap(pixmap)
#         # self.resize(pixmap.size())
#         # self.adjustSize()
        
#         imagePath, _ = QFileDialog.getOpenFileName()
   
#         self.pixmap = QPixmap(imagePath)
#         self.lb.setPixmap(QPixmap(imagePath))
#         self.lay.addWidget(self.lb)
#         self.widget.show()
        
        
#     def maintainRatio(self):
#         # image scales while maintaing its aspect ratio. Extra space is blackened.
#         pixmap = self.pixmap.scaled(self.width(), 
#                         self.height(), 
#                         Qt.KeepAspectRatio)
#         self.resize(pixmap.size())


    

        
        
        

# def main():
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     # win.show()
#     return app.exec_()

# if __name__ == '__main__':
#     sys.exit(main()) 

