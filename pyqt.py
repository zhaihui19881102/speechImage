# -*- coding: utf-8 -*-
#import _init_path
#from models.conv import GatedConv
from record import record
from aip import AipSpeech
import random
import sys
from PyQt5 import  QtCore, QtGui
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication,QLabel)
 

#some keys
APP_ID = '22013274'
API_KEY = '5RGT82W295rGGCCIaYmc2hPg'
SECRET_KEY = 'ZpLz9jM4oV3kO70WVjdFt2W6rsLrBnu1'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

imageList=['飞机','蝴蝶','火箭','骆驼','汽车','热气球','挖掘机','长颈鹿','苹果','菠萝','鸭梨','草莓','西瓜','葡萄','葡萄','爸爸','妈妈','奶奶','爷爷' ,'糖果','蓝火车','泡泡机','自行车','小猪佩奇','火车道','妹妹','姐姐','积木','睡觉的狗狗','吃饭']

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



#the pyqt GUI
class SpeechImage(QWidget):

    def __init__(self):
        super().__init__()
        self.audio='/Users/admin/Denny/learning/python_games/pyqt-test/voice.wav'
        self.label='test'
        self.period=5   #the record time    
        self.result='the result'
        self.imgName='/Users/admin/Denny/learning/python_games/pyqt-test/picture/飞机.png'
        self.imgNamePre='/Users/admin/Denny/learning/python_games/pyqt-test/picture/'
        self.initUI()
        

    def initUI(self):
        

        #lbl1 = QLabel(self.label, self)
        #lbl1.move(25, 10)
        #self.resize(600,400)
        self.okButton = QPushButton("开始说话",self)
        self.okButton.move(250,20)
        self.changeButton = QPushButton("change picture",self)
        self.changeButton.move(230,60)     

        self.lbl1 = QLabel(self.label, self)
        self.lbl1.setText('this is a picture')
        self.lbl1.setFixedSize(1200,800)
        self.lbl1.move(160, 100)
        self.lbl1.setStyleSheet("QLabel{background:white;}" 
                    "QLabel{color:rgb(250,0,0);font-size:10px;font-weight:bold;font-family:宋体;}")

        jpg = QtGui.QPixmap(self.imgName).scaled(self.lbl1.width(), self.lbl1.height())
        self.lbl1.setPixmap(jpg)
        #lbl1.setPicture(self.imgName)

        self.okButton.clicked.connect(self.process)
        self.changeButton.clicked.connect(self.changePicture)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('SpeechImage')    
        self.show()

    def changePicture(self):
        print('change picture....')
        jpg0 = QtGui.QPixmap(self.imgName).scaled(self.lbl1.width(), self.lbl1.height())
        jpg1 = QtGui.QPixmap(self.imgName)

        if(random.randint(0,1)):
            self.lbl1.setPixmap(jpg0)
        else:
            self.lbl1.setPixmap(jpg1)

    def process(self):
        #print(self.sender().text())
        #print('processing....')
        self.record()
        self.recognize()
        self.changeLabel()
        self.changePic()

    def record(self):
        #print('recording...')
        record(self.audio,self.period)
        
    def recognize(self):
        #print('recognizing....')
        result_s = client.asr(get_file_content(self.audio), 'wav', 16000, {'dev_pid': 1537, })
        self.result=result_s['result']
        print(self.result)
    def changeLabel(self):
        #self.lbl1.setText(self.result)
        #print('change label')
        pass
    def changePic(self):
        for picture in imageList:
            print('picture:',str(picture),'     ' ,'self.result:',str(self.result[0]))
            if(picture in self.result[0]):

                jpg_show = QtGui.QPixmap(self.imgNamePre+picture+'.png').scaled(self.lbl1.width(), self.lbl1.height())
                print(jpg_show)
                self.lbl1.setPixmap(jpg_show)
                return




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = SpeechImage()
    sys.exit(app.exec_())