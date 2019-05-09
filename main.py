import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from worst import *
import globals




#-------------------------------------initializing window-----------------#
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.path = QPainterPath()
        globals.init()

        self.memorySizeL = QLabel(self)
        self.memorySizeL.move(20, 20)
        self.memorySizeL.setText('please enter the memory size :')

        self.memorySizeInput = QLineEdit(self)
        self.memorySizeInput.move(170,20)
        self.memorySizeInput.textChanged[str].connect(self.onChanged)
        self.validator=QDoubleValidator()
        self.memorySizeInput.setValidator(self.validator)

        self.holesB = QPushButton('adjust holes',self)
        self.holesB.move(20,150)
        self.holesB.resize(90,40)
        self.holesB.clicked.connect(self.getHoles)

        self.clear = QPushButton('clear',self)
        self.clear.move(120,150)
        self.clear.resize(90,40)
        self.clear.clicked.connect(self.cleared)

        self.allocatorL = QLabel(self)
        self.allocatorL.move(20, 80)
        self.allocatorL.setText('please choose the allocator type :')

        self.allocatorB=QPushButton('allocator type',self)
        self.allocatorB.move(190,70)
        self.allocatorB.resize(90,40)
        self.allocatorB.clicked.connect(self.allocatorType)
        

        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('memory alocator')       
    
        self.show()

    #--------------------painting have to be in here--------------------------
    def paintEvent(self,e):
        y=0
        if (globals.draw):
            painter= QPainter(self)
            painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            painter.drawRect(350,0,globals.width,float(globals.memorySize))
            for i in range (0,globals.holesNo):
                painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                painter.drawRect(350,globals.holes[i]['starting'],globals.width,globals.holes[i]['size'])
                y+=globals.holes[i]['size']
            

#----------------------reading memory size-----------------------------
    def onChanged(self, text):
        globals.memorySize = text
        #print(memorySize)

#-----------------------pop up inputs--------------------------
    def getHoles(self):

        h,okPressed = QInputDialog.getInt(self, f"number of holes","enter no of holes :")
        globals.holesNo=h

        for i in range(0,h):
            Hstart,okPressed = QInputDialog.getDouble(self, f"hole {i}",f"enter hole {i} starting address :")
            Hsize,okPressed = QInputDialog.getDouble(self, f"hole {i}",f"enter hole {i} size :")

            globals.holes.append({'id':i,'starting':Hstart,'size':Hsize,'free':Hsize,'freeStarting':Hstart})
        
        
        globals.draw = True
        self.update()
        for i in range (0,globals.holesNo):
            y=globals.holes[i]['starting']+globals.holes[i]['size']
            lable = QLabel(self)
            lable .move(310, y)
            lable .setText(f'{y}')
            lable.show()

            y=globals.holes[i]['starting']
            lable1=QLabel(self)
            lable1.move(310,y)
            lable1 .setText(f'{y}')
            lable1.show()

        addProcess=QPushButton('add process',self)
        addProcess.move(20,200)
        addProcess.resize(90,40)
        addProcess.clicked.connect(self.addProcess)
        #addProcess.clicked.connect(test)
        addProcess.show()


#------------------------------------------------
    def addProcess(self):
        n,okPressed = QInputDialog.getInt(self, f"number of segments",f"enter number of segments :")
        globals.process.append({'id': globals.currentP,'seg':n})

        for i in range (0,n):
            n,okPressed = QInputDialog.getText(self, f"segment name",f"enter segment {i}'s name :", QLineEdit.Normal, "")
            s,okPressed = QInputDialog.getDouble(self, f"segment size",f"enter segment {i}'s size :")
            globals.segments.append({'name':n,'process':globals.currentP,'size':s,'starting':0,'id':i})

        globals.currentP+=1

        if (globals.allocator == 'First Fit'):
            print('first fit function here')
        elif(globals.allocator == 'Best Fit'):
            print('best fit function here')
        else:
            print('worst fit function here')
            # worstFit(globals.holes,globals.segments,globals.currentP)
            worstFit(self)
    

    #-----------------------allocator------------------------
    def allocatorType(self):
        items = ("Best Fit","First Fit","Worst Fit")
        item, okPressed = QInputDialog.getItem(self, "Get item","allocator type:", items, 0, False)
        globals.allocator= item
        #print(allocator)

    
#---------------clear the drawing--------------
    def cleared(): #not working yet
        globals.draw=False
        self.update()
        
        


def test(self) :
    print(globals.holes)




#----------------------------------------------------


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =  Example()

    

    


    
    sys.exit(app.exec_())