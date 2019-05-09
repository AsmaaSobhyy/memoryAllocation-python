

def init ():
    global memorySize
    global holesNo
    global holes

    global currentP
    global segments
    global process
    global segNo

    global draw

    global width
    global height

    #----------------------MEMORY-------------
    memorySize=0 # the memory size in the input bar
    holesNo = 0
    holes=[] ##ex: {'id':i,'starting':Hstart,'size':Hsize,'free':Hsize,'freeStarting':Hstart}
    #----------------------PROCESS----------------------
    currentP=0
    segments=[] #{'name':n,'process':currentP,'size':s,'starting':0,'id':i}
    process=[]
    segNo = 0
    #---------------------allocator----------
    allocator='First Fit'
    #-----------------------------------------
    width=300 #dummy var 
    height=100 #dummy var 
    draw=False