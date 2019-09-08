import matplotlib.pyplot as plt
#import sss

def avi():

    '''
    print('calling module function ')
    sss.avi()
    '''
    
    for i in range(3):
        
        t=0
        print('enter file')
        f=input('........>')
        fp=open(f+'.txt','r')
        f2=open('Class_'+str(i+2)+'_test.txt','w')
        while(1):
            c1=fp.readline()
            if(c1==''):
                break
            c2=c1.split()
            if(t>375):
                f2.write(str(float(c2[0]))+' ')
                f2.write(str(float(c2[1])))
                f2.write('\n')
            t=t+1
       
        
    
    
    
        
    
    



