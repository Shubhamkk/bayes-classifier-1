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


import numpy as nm
import matplotlib.pyplot as plt
import math

class contour_boundary_confusion(Method_Mean_Var_Covar_Calc):
        def __init__(self):
            pass

        def con_bou_conf(self):
            print ('Enter 1 for case one 2 for case two and 3 for case for 3 and 4 for case four')
            k=int(input('..........................>:'))
            case=1
            if(case==1):
                print('Enter the name of class1')
                file1=input('....................>:')
                fp1=open(file1+'.txt','r')

                print('Enter the name of class1')
                file2=input('....................>:')
                fp2=open(file2+'.txt','r')

                print('Enter the name of class1')
                file3=input('....................>:')
                fp3=open(file3+'.txt','r')
                x1=[]
                y1=[]
                x2=[]
                y2=[]
                x3=[]
                y3=[]

                while(1):
                    d=fp1.readline()
                    if(d==''):
                        break
                    d1=d.split()
                    
                    x1.append(float(d1[0]))
                    y1.append(float(d1[1]))
                
              
                fp1.close()
               
                while(1):
                    d2=fp2.readline()
                    if(d2==''):
                        break
                    d3=d2.split()
                    x2.append(float(d3[0]))
                    y2.append(float(d3[1]))
                   
            
                fp2.close()

                while(1):
                    d4=fp3.readline()
                    if(d4==''):
                        break
                    d5=d4.split()
                    x3.append(float(d5[0]))
                    y3.append(float(d5[1]))
                   
            
                fp3.close()

                plt.xlim(-5,5)
                plt.ylim(-2,2)
                
                plt.scatter(x1,y1,color='red',s=5,label='class1')
                plt.scatter(x2,y2,color='green',s=5,label='class2')
                plt.scatter(x3,y3,color='blue',s=5,label='class3')
                
               
               

                #  now calculation  of sum part ..........
                M_class1=self.Mean_Calc(x1,y1)
                M_class2=self.Mean_Calc(x2,y2)
                M_class3=self.Mean_Calc(x3,y3)
                print(M_class1)
                print(M_class2)
                print(M_class3)

                
             
                if(k==1):

                    plt.title('contoure plt of class1 class2 and class3 where sigma=kI')
                    d11=self.Var_Calc(x1)
                    d14=self.Var_Calc(y1)
                    d12=self.Covar_Calc(x1,y1)
                    d13=self.Covar_Calc(x1,y1)



                    d21=self.Var_Calc(x2)
                    d24=self.Var_Calc(y2)
                    d22=self.Covar_Calc(x2,y2)
                    d23=self.Covar_Calc(x2,y2)


                    d31=self.Var_Calc(x3)
                    d34=self.Var_Calc(y3)
                    d32=self.Covar_Calc(x3,y3)
                    d33=self.Covar_Calc(x3,y3)

                    d1=(d11+d21+d31)/3
                    d2=(d12+d22+d32)/3
                    d3=(d13+d23+d33)/3
                    d4=(d14+d24+d34)/3

                    A1=[[d1,0],[0,d4]]
                    
                    A=self.Matrix_inv(A1)
                    B=self.Matrix_inv(A1)
                    C=self.Matrix_inv(A1)
               
                if(k==2):

                    plt.title('contoure plt of class1 class2 and class3 where sigma=sigma')
                    d11=self.Var_Calc(x1)
                    d14=self.Var_Calc(y1)
                    d12=self.Covar_Calc(x1,y1)
                    d13=self.Covar_Calc(x1,y1)



                    d21=self.Var_Calc(x2)
                    d24=self.Var_Calc(y2)
                    d22=self.Covar_Calc(x2,y2)
                    d23=self.Covar_Calc(x2,y2)


                    d31=self.Var_Calc(x3)
                    d34=self.Var_Calc(y3)
                    d32=self.Covar_Calc(x3,y3)
                    d33=self.Covar_Calc(x3,y3)

                    d1=(d11+d21+d31)/3
                    d2=(d12+d22+d32)/3
                    d3=(d13+d23+d33)/3
                    d4=(d14+d24+d34)/3

                    A1=[[d1,d2],[d3,d4]]
                    
                    A=self.Matrix_inv(A1)
                    B=self.Matrix_inv(A1)
                    C=self.Matrix_inv(A1)
             
                if(k==3):

                    plt.title('contoure plt of class1 class2 and class3 where sigma=Arbitry diagonal')
                    d11=self.Var_Calc(x1)
                    d14=self.Var_Calc(y1)
                    d12=self.Covar_Calc(x1,y1)
                    d13=self.Covar_Calc(x1,y1)



                    d21=self.Var_Calc(x2)
                    d24=self.Var_Calc(y2)
                    d22=self.Covar_Calc(x2,y2)
                    d23=self.Covar_Calc(x2,y2)


                    d31=self.Var_Calc(x3)
                    d34=self.Var_Calc(y3)
                    d32=self.Covar_Calc(x3,y3)
                    d33=self.Covar_Calc(x3,y3)

                    
                    A1=[[d11,0],[0,d14]]
                    B1=[[d21,0],[0,d24]]
                    C1=[[d31,0],[0,d34]]
                    
                    A=self.Matrix_inv(A1)
                    B=self.Matrix_inv(B1)
                    C=self.Matrix_inv(C1)

                if(k==4):

                    plt.title('contoure plt of class1 class2 and class3 where sigma=Arbitry')
                    d11=self.Var_Calc(x1)
                    d14=self.Var_Calc(y1)
                    d12=self.Covar_Calc(x1,y1)
                    d13=self.Covar_Calc(x1,y1)



                    d21=self.Var_Calc(x2)
                    d24=self.Var_Calc(y2)
                    d22=self.Covar_Calc(x2,y2)
                    d23=self.Covar_Calc(x2,y2)


                    d31=self.Var_Calc(x3)
                    d34=self.Var_Calc(y3)
                    d32=self.Covar_Calc(x3,y3)
                    d33=self.Covar_Calc(x3,y3)

                    
                    A1=[[d11,d12],[d13,d14]]
                    B1=[[d21,d22],[d23,d24]]
                    C1=[[d31,d32],[d33,d34]]
                    
                    A=self.Matrix_inv(A1)
                    B=self.Matrix_inv(B1)
                    C=self.Matrix_inv(C1)






                
                    
                self.sigma=[]
                self.mean=[]
                self.sigma.append(A)
                self.sigma.append(B)
                self.sigma.append(C)
                self.mean.append(M_class1)
                self.mean.append(M_class2)
                self.mean.append(M_class3)
                
                plt.xlabel('X-axis')
                plt.ylabel('Y-label')

            
                for k in range(3):
                    if(k==0):
                        clr='green'
                        lb='class_1_cluster_1'
                    elif(k==1):
                        clr='blue'
                        lb='class_1_cluster_2'
                    elif(k==2):
                        clr='red'
                        lb='class_1_cluster_3'

                    

                    #print(self.sigma[k])

                    b=(self.sigma[k][0][1]+ self.sigma[k][1][0])
                    #b=float('%.2f'%b)
                            
                    a=self.sigma[k][0][0]
                    #a=float('%.2f'%a)
                        
                    c=self.sigma[k][1][1]
                    #c=float('%.2f'%c)
                        
                    u_0=self.mean[k][0]
                        
                    u_1=self.mean[k][1]

                        
                    a1=nm.arange((u_0-3),(u_0 +3),0.01)
                    a2=nm.arange((u_1-3),(u_1 +3),0.01)
                    x,y= nm.meshgrid(a1,a2)
                       
                         
                            
                    z=  nm.exp(  (-1/2)*(a*x*x +a*u_0*u_0 -a*2*x*u_0 + b*x*y -b*x*u_1 - b*u_0*y + b*u_0*u_1 + c*y*y +c*u_1*u_1 - c*2*y*u_1))

                   
                    plt.contour(x,y,z,10,colors=clr,label=lb,linnestyles='solid')

                    
                                                                                                                    
                                                                              
                    
            
   

                plt.legend()
                plt.show()

                
                

                
if(__name__=='__main__'):
    ob=contour_boundary_confusion()
    ob.con_bou_conf()
                    













            
