class Method_Mean_Var_Covar_Calc:

    
    def Mean_Calc(self,F_Parameter1,F_Parameter2):
        sum1=0
        sum2=0
        N1=len(F_Parameter1)
        N2=len(F_Parameter2)
        if(N1>N2):
            N1=N2
        for i in range (N1):
            sum1=sum1+F_Parameter1[i]
            sum2=sum2+F_Parameter2[i]
        Mean_x=sum1/N1
        Mean_y=sum2/N1
        Mean_xy=[Mean_x,Mean_y]
        return Mean_xy

    
    def Var_Calc(self,F_Parameter):
        M_sum=0
        V_sum=0
        N=len(F_Parameter)
        for i in range(N):
            M_sum=M_sum+F_Parameter[i]
            
        Mean=M_sum/N

        for i in range(N):
            V_sum=V_sum+(F_Parameter[i]-Mean)*(F_Parameter[i]-Mean)
        Vari=V_sum/N
        return Vari

    def Covar_Calc(self,F_Parameter1,F_Parameter2):
        C_sum=0
        N1=len(F_Parameter1)
        N2=len(F_Parameter2)
        if(N1>N2):
            N1= N2

        for i in range(N1):
             C_sum=C_sum+(F_Parameter1[i])*(F_Parameter2[i])
            
               

        Cvar=C_sum/(N1)
        #calling mean function
        
        MV=self.Mean_Calc(F_Parameter1,F_Parameter2)
        print(Cvar,MV)
        
        C_var=Cvar-(MV[0]*MV[1])

        return C_var

    def Matrix_inv(self,C0_Matrix):

        det_matrics=(C0_Matrix[0][0])*(C0_Matrix[1][1]) - (C0_Matrix[0][1])*(C0_Matrix[1][0])
        
        A00=C0_Matrix[0][0]
        A01=C0_Matrix[0][1]
        A10=C0_Matrix[1][0]
        A11=C0_Matrix[1][1]

        C0_Matrix[0][0]=A11/det_matrics
        
        C0_Matrix[1][1]=A00/det_matrics
        
        C0_Matrix[0][1]=(-1)*A01/det_matrics
        
        C0_Matrix[1][0]=(-1)*A10/det_matrics

        return C0_Matrix

    


# class to find desesion boundry ..........when sigma equall  for    all class and it is diagonal matrics and prior are equall
import math
import matplotlib.pyplot as plt
import numpy as nm

# inherite the methode of builded method class
class EquallSigmaDiagonalMatrics(Method_Mean_Var_Covar_Calc):
    
    def __init__(self):
        self.mean=None
        print('enter 1 for dataset 1 :\n enter 2 for dataset 2:\n enter 3 for dataset 3:')
        self.dataset=int(input('Please Enter :'))

    def Equll_sigma_Diagonal_Classifier(self):
        print('enter 1 for classifier between Class 1 and Class 2:\n enter 2 for classifier between Class 2 and 3 :\n enter 3 for classifier between 1 and 3:')
        k=int(input('PLease choose option above mention:'))
        
        if(self.dataset==1):
            
           
            if(k==1):
                graph_name='C1_12.png'
                c_name1='Class1.txt'
                c_name2='Class2.txt'
                l0='class1'
                l1='class2'
                cl='red'
                cl2='green'
                
                Title='Fig_1 graph between class1 and class2 in dataset 1'
                
            elif(k==2):
                graph_name='C1_23.png'
                c_name1='Class2.txt'
                c_name2='Class3.txt'
                l0='class2'
                l1='class3'
                Title='Fig_2 graph between class2 and class3 in dataset 1'
                cl='green'
                cl2='blue'
                
            elif(k==3):
                graph_name='C1_31.png'
                c_name1='Class3.txt'
                c_name2='Class1.txt'
                l0='class3'
                l1='class1'
                Title='Fig_3 graph between class3 and class1 in dataset 1'
                cl='blue'
                cl2='red'

            self.classX=[]
            self.classY=[]
            self.classX1=[]
            self.classY1=[]
            fp1=open(c_name1 ,'r')
            fp2=open(c_name2 ,'r')
          
            
           
            while(1):
                d=fp1.readline()
                if(d==''):
                    break
                d1=d.split()
                
                self.classX.append(float(d1[0]))
                self.classY.append(float(d1[1]))
                
              
            fp1.close()
           
            while(1):
                d2=fp2.readline()
                if(d2==''):
                    break
                d3=d2.split()
                self.classX1.append(float(d3[0]))
                self.classY1.append(float(d3[1]))
               
        
            fp2.close()
           

            #  now calculation  of sum part ..........
            M_class1=self.Mean_Calc(self.classX,self.classY)
            M_class2=self.Mean_Calc(self.classX1,self.classY1)
            
            print(M_class1,M_class2)
            
            
            plt.title(Title)
            plt.xlabel('X-AXIS')
            plt.ylabel('Y-AXIS')
            # plotting of  boundary desesion between the classes
            x=nm.arange(-5,25,0.1)
            #classifier Function
            My0=M_class2[0]*M_class2[0]
            My1=M_class2[1]*M_class2[1]
            M=M_class1[1]-M_class2[1]
            #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y

            plt.xlim(-5,25)
            plt.ylim(-20,5)

            r_x=-5
            r_y=-20
            A=[[],[]]
            B=[[],[]]
            while(1):
                r_y=r_y+0.1
                if(r_y>5):
                    break
                r_x=-5
                while(1):
                    r_x=r_x+0.1
                    if(r_x>25):
                        break
                    d=-r_y+(-(M_class1[0]-M_class2[0])*r_x)/(M_class1[1]-  M_class2[1]) +(
            
                        (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M))
                    #print(d)
                    if(d>0):
                        A[0].append(r_x)
                        A[1].append(r_y)
                    else:
                        B[0].append(r_x)
                        B[1].append(r_y)
                    


            '''
            y= -y+(-(M_class1[0]-M_class2[0])*x)/(M_class1[1]-  M_class2[1]) +
            
                        (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M)     '''

            plt.scatter(A[0],A[1],color='yellow' ,s=5)
            plt.scatter(B[0],B[1],color='pink',s=5)
            plt.scatter(self.classX,self.classY,color=cl ,marker='*',s=5,label=l0  )
            plt.scatter(self.classX1,self.classY1,color=cl2 ,marker='*',s=5,label=l1  )
            
            

          

            
            plt.legend()
            #plt.savefig(graph_name)
            plt.show()
        # that is for third dataset
            
        elif(self.dataset==3):
            
             
           
            if(k==1):
                
                graph_name1='C3_12.png'
                c_name1='d3_class1.txt'
                c_name2='d3_class2.txt'
                l0='class1'
                l1='class2'
                cl='red'
                cl2='green'
                
                Title='Fig_1 graph between class1 and class2 in dataset 3'
                
            elif(k==2):
                graph_name1='C3_23.png'
                c_name1='d3_class2.txt'
                c_name2='d3_class3.txt'
                l0='class2'
                l1='class3'
                cl='green'
                cl2='blue'
                
                Title='Fig_2 graph between class2 and class3 in dataset 3'
            elif(k==3):
                graph_name1='C3_31.png'
                c_name1='d3_class3.txt'
                c_name2='d3_class1.txt'
                l0='class3'
                l1='class1'
                cl='blue'
                cl2='red'
                Title='Fig_3 graph between class3 and class1 in dataset 3'

            self.classX=[]
            self.classY=[]
            self.classX1=[]
            self.classY1=[]
            fp1=open(c_name1 ,'r')
            fp2=open(c_name2 ,'r')
          
            
           
            while(1):
                d=fp1.readline()
                if(d==''):
                    break
                d1=d.split()
                
                self.classX.append(float(d1[0]))
                self.classY.append(float(d1[1]))
                
              
            fp1.close()
           
            while(1):
                d2=fp2.readline()
                if(d2==''):
                    break
                d3=d2.split()
                self.classX1.append(float(d3[0]))
                self.classY1.append(float(d3[1]))
               
        
            fp2.close()
           

            #  now calculation  of sum part ..........
            M_class1=self.Mean_Calc(self.classX,self.classY)
            M_class2=self.Mean_Calc(self.classX1,self.classY1)
            
            print('Mean:c1 : c2 ',M_class1,M_class2)
            
            #plt.scatter(self.classX,self.classY,color='red',marker='*',s=5,label=l0  )
            #plt.scatter(self.classX1,self.classY1,color='green',marker='*',s=5,label=l1  )
            plt.title(Title)
            plt.xlabel('X-AXIS')
            plt.ylabel('Y-AXIS')
            # plotting of  boundary desesion between the classes
            x=nm.arange(0,1400,0.1)
            #classifier Function
            My0=M_class2[0]*M_class2[0]
            My1=M_class2[1]*M_class2[1]
            M=M_class1[1]-M_class2[1]
            #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y

            plt.xlim(150,1500)
            plt.ylim(-200,1500)

            r_x=-150
            r_y=-200
            A=[[],[]]
            B=[[],[]]
            while(1):
                r_y=r_y+5
                if(r_y>1500):
                    break
                r_x=-150
                while(1):
                    r_x=r_x+5
                    if(r_x>1500):
                        break
                    d=-r_y+(-(M_class1[0]-M_class2[0])*r_x)/(M_class1[1]-  M_class2[1]) +(
            
                        (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M))
                    #print(d)
                    if(d>0):
                        A[0].append(r_x)
                        A[1].append(r_y)
                    else:
                        B[0].append(r_x)
                        B[1].append(r_y)
                    


            

            #y=(-(M_class1[0]-M_class2[0])*x)/(M_class1[1]-  M_class2[1]) + (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M)
            #plt.plot(x,y,label='b_decesion',color='black')

                        
            plt.scatter(A[0],A[1],color='yellow' ,s=5)
            plt.scatter(B[0],B[1],color='pink',s=5)
            plt.scatter(self.classX,self.classY,color=cl ,marker='*',s=5,label=l0  )
            plt.scatter(self.classX1,self.classY1,color=cl2 ,marker='*',s=5,label=l1  )
            


                        
            plt.legend()
            plt.savefig(graph_name1)
            plt.show()

        elif(self.dataset==2):
            self.x_class1=[]
            self.y_class1=[]
            self.x1_class2=[]
            self.y1_class2=[]
            self.x2_class3=[]
            self.y2_class3=[]
            fp3=open('C123.txt','r')
            fp3.readline()
            for i in range (500):
                d_3=fp3.readline()
                d_s=d_3.split()
                self.x_class1.append(float(d_s[0]))
                self.y_class1.append(float(d_s[1]))

            for i in range (500,1000):
                d_4=fp3.readline()
                d_s1=d_4.split()
                self.x1_class2.append(float(d_s1[0]))
                self.y1_class2.append(float(d_s1[1]))
                
                
            for i in range (1000,1500):
                d_5=fp3.readline()
                d_s2=d_5.split()
                self.x2_class3.append(float(d_s2[0]))
                self.y2_class3.append(float(d_s2[1]))
            
            if (k==1):
                l0='class1'
                l1='class2'
                Title='Fig_1 graph between class1 and class2 in dataset 2'
                M_class1=self.Mean_Calc(self.x_class1,self.y_class1)
                M_class2=self.Mean_Calc(self.x1_class2,self.y1_class2)
            
                print('Mean:c1 : c2 ',M_class1,M_class2)
            
                plt.scatter(self.x_class1,self.y_class1,color='red',marker='*',s=5,label=l0  )
                plt.scatter(self.x1_class2,self.y1_class2,color='green',marker='*',s=5,label=l1  )
                plt.title(Title)
                plt.xlabel('X-AXIS')
                plt.ylabel('Y-AXIS')
                # plotting of  boundary desesion between the classes
                x=nm.arange(-4,5,0.1)
                #classifier Function
                My0=M_class2[0]*M_class2[0]
                My1=M_class2[1]*M_class2[1]
                M=M_class1[1]-M_class2[1]
                #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
                y=(-(M_class1[0]-M_class2[0])*x)/(M_class1[1]-  M_class2[1]) + (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M)
                plt.plot(x,y,label='b_decesion',color='black')
                plt.legend()
                #plt.savefig('d2_c1_c2.png')
                plt.show()


            elif (k==2):
                
                
               
                    
                l0='class2'
                l1='class3'
                    
                Title='Fig_1 graph between class2 and class3 in dataset 2'
                M_class1=self.Mean_Calc(self.x1_class2,self.y1_class2)
                M_class2=self.Mean_Calc(self.x2_class3,self.y2_class3)
            
                print('Mean:c1 : c2 ',M_class1,M_class2)
            
                plt.scatter(self.x1_class2,self.y1_class2,color='red',marker='*',s=5,label=l0  )
                plt.scatter(self.x2_class3,self.y2_class3,color='green',marker='*',s=5,label=l1  )
                plt.title(Title)
                plt.xlabel('X-AXIS')
                plt.ylabel('Y-AXIS')
                # plotting of  boundary desesion between the classes
                x=nm.arange(-4,5,0.1)
                #classifier Function
                My0=M_class2[0]*M_class2[0]
                My1=M_class2[1]*M_class2[1]
                M=M_class1[1]-M_class2[1]
                #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
                y=(-(M_class1[0]-M_class2[0])*x)/(M_class1[1]-  M_class2[1]) + (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M)
                plt.plot(x,y,label='b_decesion',color='black')
                plt.legend()
                #plt.savefig('d2_c2_c3.png')
                plt.show()
            

            elif (k==3):
                
                
               
                    
                l0='class3'
                l1='class1'
                    
                Title='Fig_1 graph between class3 and class1 in dataset 2'
                M_class1=self.Mean_Calc(self.x2_class3,self.y2_class3)
                M_class2=self.Mean_Calc(self.x_class1,self.y_class1)
            
                print('Mean:c1 : c2 ',M_class1,M_class2)
            
                plt.scatter(self.x1_class2,self.y1_class2,color='red',marker='*',s=5,label=l0  )
                plt.scatter(self.x2_class3,self.y2_class3,color='green',marker='*',s=5,label=l1  )
                plt.title(Title)
                plt.xlabel('X-AXIS')
                plt.ylabel('Y-AXIS')
                # plotting of  boundary desesion between the classes
                x=nm.arange(-4,5,0.1)
                #classifier Function
                My0=M_class2[0]*M_class2[0]
                My1=M_class2[1]*M_class2[1]
                M=M_class1[1]-M_class2[1]
                #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
                y=(-(M_class1[0]-M_class2[0])*x)/(M_class1[1]-  M_class2[1]) + (-(1/2)*(-(M_class1[0]*M_class1[0]) - (M_class1[1]*M_class1[1])+ My0+My1))/(M)
                plt.plot(x,y,label='b_decesion',color='black')
                plt.legend()
                #plt.savefig('d2_c1_c3.png')
                plt.show()

                
                
                
          
                
             
               
                
            
          
           

if(__name__=='__main__'):

    
    s1=EquallSigmaDiagonalMatrics()
    s1.Equll_sigma_Diagonal_Classifier()
    
    
    
        
            
        
                
        
    


        
