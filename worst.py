from main import *
import globals

# def worstFit(holes,segments,currentP):
def worstFit(self):
    #print(globals.holesNo)
    
    # holesNo = len(holes)
    currentSeg=[]
    size=len(globals.segments)
    cur=0
    #print('in')
    for i in range (0,size):
        if (globals.segments[i]['process']==globals.currentP-1):
            currentSeg.append(globals.segments[i])

    #print(currentSeg)
    cur=len(currentSeg)
    changed=False
    check =0

    testHoles = sorted(globals.holes, key=lambda k: k['size'],reverse=True)

    for j in range (0,cur):
        changed=False
        for i in range (0,globals.holesNo):
            if(currentSeg[j]['size']<=testHoles[i]['size']):
                if(currentSeg[j]['size']<=testHoles[i]['free'] and changed==False ):
                    testHoles[i]['free']-=currentSeg[j]['size']
                    currentSeg[j]['starting']=testHoles[i]['freeStarting']
                    testHoles[i]['freeStarting']+=currentSeg[j]['size']
                    changed=True
                    check+=1
                    #print(currentSeg[j])

            else:
                print('wont fit')
                break
    if(check == cur):
        globals.holes = sorted(globals.holes, key=lambda k: k['id'])

        for i in range (0,size):
            for j in range (0,cur):
                if (globals.segments[i]['process']==globals.currentP-1 and globals.segments[i]['id']== currentSeg[j]['id']):
                    globals.segments[i] = currentSeg[j]
        #print(globals.segments)

        for k in range (0,cur):
            p= currentSeg[k]['process']
            n = currentSeg[k]['name']
            processB=QPushButton(f'p{p} : {n}',self)
            n= currentSeg[k]['starting']
            processB.move(350,n)
            n=currentSeg[k]['size']
            processB.resize(globals.width,n)
            #processB.clicked.connect(self.allocatorType)
            processB.show()

        x=globals.currentP-1
        deprocess =QPushButton(f'process {x}',self)
        deprocess.move(800,globals.dealocateY)
        globals.dealocateY+=40
        deprocess.resize(90,40)
        deprocess.show()
        deprocess.clicked.connect(deallocate)
        
    else:
        print("doesn't fit")
    # print(testHoles)
    # print(currentSeg)

def deallocate():
    print('deallocated')
