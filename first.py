from main import *
import globals

def firstFit(self):

    currentSeg=[]
    size=len(globals.segments)
    cur=0

    for i in range (0,size):
        if(globals.segments[i]['process']==globals.currentP-1):
            currentSeg.append(globals.segments[i])

    cur=len(currentSeg)
    changes=False
    check =0

    testHoles = sorted(globals.holes, key=lambda k: k['size'],reverse=False)


    for j in range (0,cur):
        changed=False
        for i in range (0,globals.holesNo):
            if(currentSeg[j]['size']<=testHoles[0]['size']):
                if(currentSeg[j]['size']<=testHoles[0]['free'] and changed==False):
                    testHoles[0]['free']-=currentSeg[j]['size']
                    currentSeg[j]['starting']=testHoles[0]['freeStarting']
                    testHoles[0]['freeStarting']+=currentSeg[j]['size']
                    changed=True
                    check+=1

            elif(currentSeg[j]['size']>testHoles[0]['size']):
                if(currentSeg[j]['size']>testHoles[0]['free'] and changed==False):
                    testHoles[1]['free']-=currentSeg[j]['size']
                   # currentSeg[j]['starting']=testHoles[1]['freeStarting']
                   # testHoles[1]['freeStarting']+=currentSeg[j]['size']
                    changed=True
                    check+=1

            else:
                print('wont fit')
                break

    if(check == cur):
        globals.holes = sorted(globals.holes, key=lambda k: k['id'])

        for i in range (0,size):
            for j in range (0,cur):
                if(globals.segments[i]['process']==globals.currentP-1 and globals.segments[i]['id']==currentSeg[j]['id']):
                    globals.segments[i] = currentSeg[j]

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
