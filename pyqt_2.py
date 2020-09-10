
# -*- coding: utf-8 -*-
 
"""
PyQt5 tutorial 
 
In this example, we determine the event sender
object.
 
author: py40.com
last edited: 2017年3月
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QInputDialog,QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
 
        openFile = QAction(QIcon('/Users/admin/Denny/learning/python_games/pyqt-test/wajueji.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        ok = QAction(QIcon('/Users/admin/Denny/learning/python_games/pyqt-test/wajueji.png'), 'Open', self)
        ok.setShortcut('ctrl+B')
        ok.setStatusTip('this is ok')
        ok.triggered.connect(self.showok)


        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        okMenu=menubar.addMenu('&OK')
        okMenu.addAction(ok)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showok(self):
        text, ok = QInputDialog.getText(self, 'OK Dialog', 'Enter your name:')
        if ok:
            self.textEdit.setText(text) 
            print(str(text))
            
    def showDialog(self):
 
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
 
        if fname[0]:
            f = open(fname[0], 'r')
 
            with f:
                data = f.read()
                self.textEdit.setText(data)        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())