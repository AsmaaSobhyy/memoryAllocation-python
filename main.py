import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#---------------------------------global vars--------------------------------#
memorySize=0 # the memory size in the input bar
holesNo=0
width=300 #dummy var 
height=100 #dummy var 
holes=[] ##ex: {'starting':0,'size':100}
draw=False
#-------------------process shape-------------------------------
#process=[] # [no of process][no on segments] ## [1][{'segment':1,'size':3}]
#------#
#process = []                                                           
#for i in range (0, no of process):                               
    #process.append([])                 
    #for j in range (0, no of segments in process i):    } with a list         
        #process[i].append({'seg;:1,'size':30}) 

#-------------------------------------initializing window-----------------#
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.path = QPainterPath()

        self.memorySizeL = QLabel(self)
        self.memorySizeL.move(20, 20)
        self.memorySizeL.setText('please enter the memory size :')

        self.memorySizeInput = QLineEdit(self)
        self.memorySizeInput.move(170,20)
        self.memorySizeInput.textChanged[str].connect(self.onChanged)
        self.validator=QDoubleValidator()
        self.memorySizeInput.setValidator(self.validator)

        self.holesB = QPushButton('adjust holes',self)
        self.holesB.move(20,50)
        self.holesB.resize(90,40)
        self.holesB.clicked.connect(self.getHoles)

        self.clear = QPushButton('clear',self)
        self.clear.move(120,50)
        self.clear.resize(90,40)
        self.clear.clicked.connect(self.cleared)
        

        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('memory alocator')       
    
        self.show()

    #--------------------painting have to be in here--------------------------
    def paintEvent(self,e):
        global holesNo
        global holes
        global width
        global height
        global memorySize
        y=0
        if (draw):
            painter= QPainter(self)
            painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            painter.drawRect(350,0,width,int(memorySize))
            for i in range (0,holesNo):
                painter.drawRect(350,holes[i]['starting'],width,holes[i]['size'])
                y+=holes[i]['size']
            

#----------------------reading memory size-----------------------------
    def onChanged(self, text):
        global memorySize 
        memorySize = text
        #print(memorySize)

#-----------------------pop up inputs--------------------------
    def getHoles(self):
        global holes
        global holesNo

        h,okPressed = QInputDialog.getInt(self, f"number of holes","enter no of holes :")
        holesNo=h

        for i in range(0,h):
            Hstart,okPressed = QInputDialog.getDouble(self, f"hole {i}",f"enter hole {i} starting address :")
            Hsize,okPressed = QInputDialog.getDouble(self, f"hole {i}",f"enter hole {i} size :")

            holes.append({'id':i,'starting':Hstart,'size':Hsize,'free':Hsize})
        
        global draw
        draw = True
        self.update()
        for i in range (0,holesNo):
            y=holes[i]['starting']+holes[i]['size']
            lable = QLabel(self)
            lable .move(310, y)
            lable .setText(f'{y}')
            lable.show()
            y=holes[i]['starting']
            lable1=QLabel(self)
            lable1.move(310,y)
            lable1 .setText(f'{y}')
            lable1.show()



    
#---------------clear the drawing--------------
    def cleared(): #not working yet
        global draw
        draw=False
        self.update()
        
        



    




#----------------------------------------------------


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =  Example()

    

    


    
    sys.exit(app.exec_())