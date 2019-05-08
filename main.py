import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#---------------------------------global vars--------------------------------#
memorySize=0
holes=[]
opened=False

#-------------------------------------initializing window-----------------#
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.memorySizeL = QLabel(self)
        self.memorySizeL.move(60, 40)
        self.memorySizeL.setText('please enter the memory size :')

        self.memorySizeInput = QLineEdit(self)
        self.memorySizeInput.move(220,40)
        self.memorySizeInput.textChanged[str].connect(self.onChanged)
        self.validator=QDoubleValidator()
        self.memorySizeInput.setValidator(self.validator)

        self.holesB = QPushButton('adjust holes',self)
        self.holesB.move(200,90)
        self.holesB.resize(90,40)
        self.holesB.clicked.connect(self.getHoles)

        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle('memory alocator')       
    
        self.show()

    


    def onChanged(self, text):
        global memorySize 
        memorySize = text
        #print(memorySize)

    def getHoles(self):
        global holes
        h,okPressed = QInputDialog.getInt(self, f"number of holes","enter no of holes :")
        
        for i in range(0,h):
            Hstart,okPressed = QInputDialog.getDouble(self, f"hole {i}",f"enter hole {i} starting address :")
            Hsize,okPressed = QInputDialog.getDouble(self, f"hole {i}",f"enter hole {i} size :")

            holes.append({'starting':Hstart,'size':Hsize})
        
        
        draw1 = QDialog()
        draw1.setWindowTitle("memory Allocator")
        draw1.setModal(True)
        #self.memoryDraw(draw1)
        
        draw1.exec()
        #print(holes)
    

    # def memoryDraw(self):
    #     qp = QPainter()
    #     qp.begin(self)           
    #     qp.drawRect(20, 50, 60, 90)        
    #     qp.end()
        # qp = QPainter()
        # br = QBrush(QtGui.QColor(100, 10, 10, 40))  
        # qp.setBrush(br)   
        # qp.drawRect(QtCore.QRect(self.begin, self.end))  

        






# def paint(self):
#         painter= QPainter(self)
#         painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
#         painter.drawRect(100,15,400,200)



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =  Example()
    #global opened

    # painter= QPainter(w)
    # painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
    # painter.drawRect(100,15,400,200)



    
    sys.exit(app.exec_())