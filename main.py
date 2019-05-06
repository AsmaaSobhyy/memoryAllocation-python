import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#-------------------------------------initializing window-----------------#
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('scheduler')       
    
        self.show()





if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =  Example()


    
    sys.exit(app.exec_())