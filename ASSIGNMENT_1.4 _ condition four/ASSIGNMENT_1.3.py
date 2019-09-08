



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
        #print(Cvar,MV)
        
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
                cl='green'
                cl2='blue'
                Title='Fig_2 graph between class2 and class3 in dataset 1'
            elif(k==3):
                graph_name='C1_31.png'
                c_name1='Class3.txt'
                c_name2='Class1.txt'
                l0='class3'
                l1='class1'
                cl='blue'
                cl2='red'
                Title='Fig_3 graph between class3 and class1 in dataset 1'

            self.classX=[]
            self.classY=[]
            self.classX1=[]
            self.classY1=[]
            fp1=open(c_name1 ,'r')
            fp2=open(c_name2 ,'r')
          
            
            t=0
            while(1):
                t=t+1
                d=fp1.readline()
                if(d==''):
                    break
                if(t==375):
                    break
                d1=d.split()
                
                self.classX.append(float(d1[0]))
                self.classY.append(float(d1[1]))
                
              
            fp1.close()
            t=0
            while(1):
                t=t+1
                d2=fp2.readline()
                if(d2==''):
                    break
                if(t==375):
                    break
                
                d3=d2.split()
                self.classX1.append(float(d3[0]))
                self.classY1.append(float(d3[1]))
               
        
            fp2.close()
           

            #  now calculation  of mean  part ..........
            M_class1=self.Mean_Calc(self.classX,self.classY)
           
            
            M_class2=self.Mean_Calc(self.classX1,self.classY1)
            

            
            # CALCULATE THE SIGMA MATRICS
            m00=self.Var_Calc(self.classX)
            m11=self.Var_Calc(self.classY)
            
            m_00=self.Var_Calc(self.classX1)
            m_11=self.Var_Calc(self.classY1)
            
            m01=self.Covar_Calc(self.classX,self.classY)
            m10=self.Covar_Calc(self.classX,self.classY)

            m_01=self.Covar_Calc(self.classX1,self.classY1)
            m_10=self.Covar_Calc(self.classX1,self.classY1)
            
            # sigma matrics of given class
            sigm_matrics1=[[m00,m01],[m10,m11]]
            sigm_matrics2=[[m_00,m_01],[m_10,m_11]]

            # determinant of sigma matrics
            
            D1=m00*m11-m01*m10
            D2=m_00*m_11-m_01*m_10
            if(D1<0):
                D1=-1*D1
            if(D2<0):
                    D2=-1*D2

            

            
            #calling inverse function to comput sigma inverse
            sigma_inverse1=self.Matrix_inv( sigm_matrics1)
            A=sigma_inverse1
            sigma_inverse2=self.Matrix_inv( sigm_matrics2)
            B=sigma_inverse2

            #print('inverse',A)
            #print('sigma',sigm_matrics1)
            print('sigma inverse A:B:',A,B)



            
            print('mean of class:', M_class1,M_class2)

            # plotting of graph  hear of data 
            
            plt.scatter(self.classX,self.classY,color='red',marker='*',s=5,label=l0  )
            plt.scatter(self.classX1,self.classY1,color='green',marker='*',s=5,label=l1  )
            plt.title(Title)
            plt.xlabel('X-AXIS')
            plt.ylabel('Y-AXIS')
            # plotting of  boundary desesion between the classes
            x=nm.arange(5,25,0.1)


            
            #Cofficient calculation of require equation
            a0=1/2*(B[0][0]-A[0][0])
            b0=1/2*(B[0][1]-A[0][1])
            a1=1/2*(B[1][1]-A[1][1])
            b1=1/2*(B[1][0]-A[1][0])
            c0=((M_class1[0]*A[0][0]+M_class1[1]*A[1][0])-(M_class2[0]*B[0][0]+M_class2[1]*B[1][0]))
            d0=((M_class1[0]*A[0][1]+M_class1[1]*A[1][1])-(M_class2[0]*B[0][1]+M_class2[1]*B[1][1]))
            k1=-(1/2)*(M_class1[0]*(A[0][0]*M_class1[0] + A[0][1]*M_class1[1]) + M_class1[1]*(A[1][0]*M_class1[0] + A[1][1]*M_class1[1]))
            k2=(1/2)*(M_class2[0]*(B[0][0]*M_class2[0] + B[0][1]*M_class2[1]) + M_class1[1]*(B[1][0]*M_class2[0] + B[1][1]*M_class2[1]))
            k12=k1+k2
            k3=(1/2)* math.log((D2/D1),2)
            k0=k12 + k3
            
            
        
            
            #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
            #y1=(-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)
            
            #y2=(-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)
            
            i=0
            if(i==0):
                A1=[[],[]]
                B1=[[],[]]
                y1=-100
                x=0
                while(1):
                    y1=y1+0.2
                    if(y1>50):
                        break
                    x=0
                    while(1):
                        x=x+0.1
                        if(x>20):
                            break
                        di1=nm.linalg.det(sigm_matrics1)
                        if(di1<0):
                            di1=-1*di1
                        
                        
                        d1=nm.dot([x,y1],nm.dot(A,[x,y1]))-math.log(2*3.14*math.pow(di1,0.5))
                        
                        #d1 =(-y1 + (-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        #print(d1)
                        
                        di2=nm.linalg.det(sigm_matrics2)
                        if(di2<0):
                            di2=-1*di2
                            
                        d2=nm.dot([x,y1],nm.dot(B,[x,y1]))-math.log(2*3.14*math.pow(di2,0.5))
                        
                        #d2=  (y1+ (-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        #d0=d1*d2
                        #print(d2)
                       
                        #print('d2',d2)
                        if(d2>d1):
                            A1[0].append(x)
                            A1[1].append(y1)
                        else:
                            B1[0].append(x)
                            B1[1].append(y1)
                        

                
                #print('\n',B)
                print('lenth a',len(A1[0]))
                print('lenth b',len(B1[0]))
                plt.scatter(A1[0],A1[1],s=0.01)
                plt.scatter(B1[0],B1[1],s=0.01)
                plt.scatter(self.classX,self.classY,color=cl,marker='*',s=5,label=l0  )
                plt.scatter(self.classX1,self.classY1,color=cl2,marker='*',s=5,label=l1  )
            

            




            #plt.plot(x,y1,color='black')
            #plt.plot(x,y2,label='b_decesion',color='black')
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
            
            
            #print('Mean:c1 : c2 ',M_class1,M_class2)
            
            # plotting of  boundary desesion between the classes
            # hear we can range x in (380-480) and other set is (100-1000)
            x=nm.arange(-100,1200,0.1)
           
            # CALCULATE THE SIGMA MATRICS
            m00=self.Var_Calc(self.classX)
            m11=self.Var_Calc(self.classY)
            
            m_00=self.Var_Calc(self.classX1)
            m_11=self.Var_Calc(self.classY1)
            
            m01=self.Covar_Calc(self.classX,self.classY)
            m10=self.Covar_Calc(self.classX,self.classY)

            m_01=self.Covar_Calc(self.classX1,self.classY1)
            m_10=self.Covar_Calc(self.classX1,self.classY1)

            # sigma matrics of given class
            sigm_matrics1=[[m00,m01],[m10,m11]]
            sigm_matrics2=[[m_00,m_01],[m_10,m_11]]

            # determinant of sigma matrics
            
            D1=m00*m11-m01*m10
            D2=m_00*m_11-m_01*m_10
            if(D1<0):
                D1=-1*D1
            if(D2<0):
                    D2=-1*D2

            

            
            #calling inverse function to comput sigma inverse
            sigma_inverse1=self.Matrix_inv( sigm_matrics1)
            A=sigma_inverse1
            sigma_inverse2=self.Matrix_inv( sigm_matrics2)
            B=sigma_inverse2
            print('sigma inverse A:B:',A,B)





            
            print('mean of class:', M_class1,M_class2)

            # plotting of graph  hear of data 
            
            #plt.scatter(self.classX,self.classY,color='red',marker='*',s=5,label=l0  )
            #plt.scatter(self.classX1,self.classY1,color='green',marker='*',s=5,label=l1  )
            plt.title(Title)
            plt.xlabel('X-AXIS')
            plt.ylabel('Y-AXIS')

            
            
            
            #Cofficient calculation of require equation
            a0=1/2*(B[0][0]-A[0][0])
            b0=1/2*(B[0][1]-A[0][1])
            a1=1/2*(B[1][1]-A[1][1])
            b1=1/2*(B[1][0]-A[1][0])
            c0=((M_class1[0]*A[0][0]+M_class1[1]*A[1][0])-(M_class2[0]*B[0][0]+M_class2[1]*B[1][0]))
            d0=((M_class1[0]*A[0][1]+M_class1[1]*A[1][1])-(M_class2[0]*B[0][1]+M_class2[1]*B[1][1]))
            k1=-(1/2)*(M_class1[0]*(A[0][0]*M_class1[0] + A[0][1]*M_class1[1]) + M_class1[1]*(A[1][0]*M_class1[0] + A[1][1]*M_class1[1]))
            k2=(1/2)*(M_class2[0]*(B[0][0]*M_class2[0] + B[0][1]*M_class2[1]) + M_class1[1]*(B[1][0]*M_class2[0] + B[1][1]*M_class2[1]))
            k12=k1+k2
            k3=(1/2)* math.log((D2/D1),2)
            k0=k12 + k3
            
            
        
            
            #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
            #y1=(-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)
            #y2=(-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)



            i=0
            if(i==0):
                A1=[[],[]]
                B1=[[],[]]
                y1=-200
                x=150
                while(1):
                    y1=y1+5
                    if(y1>1500):
                        break
                    x=150
                    while(1):
                        x=x+5
                        if(x>1500):
                            break
                        #di1=nm.linalg.det(sigm_matrics1)
                        #if(di1<0):
                            #di1=-1*di1
                        
                        
                        #d1=nm.dot([x,y1],nm.dot(A,[x,y1]))-math.log(2*3.14*math.pow(di1,0.5))
                        
                        d1 =(-y1 + (-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        #print(d1)
                        
                        #di2=nm.linalg.det(sigm_matrics2)
                        #if(di2<0):
                            #di2=-1*di2
                            
                        #d2=nm.dot([x,y1],nm.dot(B,[x,y1]))-math.log(2*3.14*math.pow(di2,0.5))
                        
                        d2=  (-y1+ (-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        #d0=d1*d2
                        #print(d2)
                       
                        #print('d2',d2)
                        if(d2>d1):
                            A1[0].append(x)
                            A1[1].append(y1)
                        else:
                            B1[0].append(x)
                            B1[1].append(y1)
                        

                
                #print('\n',B)
                print('lenth a',len(A1[0]))
                print('lenth b',len(B1[0]))
                plt.scatter(A1[0],A1[1],s=0.01)
                plt.scatter(B1[0],B1[1],s=0.01)
                plt.scatter(self.classX,self.classY,color=cl,marker='*',s=5,label=l0  )
                plt.scatter(self.classX1,self.classY1,color=cl2,marker='*',s=5,label=l1  )
            

            




            #plt.plot(x,y1,color='black')
            #plt.plot(x,y2,label='b_decesion',color='black')
            plt.legend()
            #plt.savefig(graph_name1)
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
            
                #plt.scatter(self.x_class1,self.y_class1,color='red',marker='*',s=5,label=l0  )
                #plt.scatter(self.x1_class2,self.y1_class2,color='green',marker='*',s=5,label=l1  )
                plt.title(Title)
                plt.xlabel('X-AXIS')
                plt.ylabel('Y-AXIS')
                # plotting of  boundary desesion between the classes
                x=nm.arange(-4,5,0.1)
                #classifier Function

                
                # finding the matrics 
                
                m00=self.Var_Calc(self.x_class1)
                m11=self.Var_Calc(self.y_class1)
            
                m_00=self.Var_Calc(self.x1_class2)
                m_11=self.Var_Calc(self.y1_class2)
            
                m01=self.Covar_Calc(self.x_class1,self.y_class1)
                m10=self.Covar_Calc(self.x_class1,self.y_class1)

                m_01=self.Covar_Calc(self.x1_class2,self.y1_class2)
                m_10=self.Covar_Calc(self.x1_class2,self.y1_class2)

                # sigma matrics of given class
                sigm_matrics1=[[m00,m01],[m10,m11]]
                sigm_matrics2=[[m_00,m_01],[m_10,m_11]]

                # determinant of sigma matrics
            
                D1=m00*m11-m01*m10
                D2=m_00*m_11-m_01*m_10
                if(D1<0):
                    
                    D1=-1*D1
                if(D2<0):
                    
                    D2=-1*D2

            

            
                #calling inverse function to comput sigma inverse
                sigma_inverse1=self.Matrix_inv( sigm_matrics1)
                A=sigma_inverse1
                sigma_inverse2=self.Matrix_inv( sigm_matrics2)
                B=sigma_inverse2
                print('sigma inverse A:B:',A,B)


                


            
                print('mean of class:', M_class1,M_class2)

             
                #Cofficient calculation of require equation
                a0=1/2*(B[0][0]-A[0][0])
                b0=1/2*(B[0][1]-A[0][1])
                a1=1/2*(B[1][1]-A[1][1])
                b1=1/2*(B[1][0]-A[1][0])
                c0=((M_class1[0]*A[0][0]+M_class1[1]*A[1][0])-(M_class2[0]*B[0][0]+M_class2[1]*B[1][0]))
                d0=((M_class1[0]*A[0][1]+M_class1[1]*A[1][1])-(M_class2[0]*B[0][1]+M_class2[1]*B[1][1]))
                k1=-(1/2)*(M_class1[0]*(A[0][0]*M_class1[0] + A[0][1]*M_class1[1]) + M_class1[1]*(A[1][0]*M_class1[0] + A[1][1]*M_class1[1]))
                k2=(1/2)*(M_class2[0]*(B[0][0]*M_class2[0] + B[0][1]*M_class2[1]) + M_class1[1]*(B[1][0]*M_class2[0] + B[1][1]*M_class2[1]))
                k12=k1+k2
                k3=(1/2)* math.log((D2/D1),2)
                k0=k12 + k3
            
            
        
            
                #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
                y1=(-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)
                y2=(-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)

            
                A1=[[],[]]
                B1=[[],[]]
                y1=-2
                x=-5
                while(1):
                    y1=y1+.01
                    if(y1>2):
                        break
                    x=-5
                    while(1):
                        x=x+.01
                        if(x>5):
                            break
                        #di1=nm.linalg.det(sigm_matrics1)
                        #if(di1<0):
                            #di1=-1*di1
                        
                        
                        #d1=nm.dot([x,y1],nm.dot(A,[x,y1]))-math.log(2*3.14*math.pow(di1,0.5))
                        
                        d1 =(-y1 + (-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        #print(d1)
                        
                        #di2=nm.linalg.det(sigm_matrics2)
                        #if(di2<0):
                            #di2=-1*di2
                            
                        #d2=nm.dot([x,y1],nm.dot(B,[x,y1]))-math.log(2*3.14*math.pow(di2,0.5))
                        
                        d2=  ( -y1+ (-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        d0=d1*d2
                        #print(d2)
                       
                        #print('d2',d2)
                        if(d0>0):
                            A1[0].append(x)
                            A1[1].append(y1)
                        else:
                            B1[0].append(x)
                            B1[1].append(y1)
                        

                
                #print('\n',B)
                print('lenth a',len(A1[0]))
                print('lenth b',len(B1[0]))
                plt.scatter(A1[0],A1[1],s=0.01)
                plt.scatter(B1[0],B1[1],s=0.01)
                plt.scatter(self.x_class1,self.y_class1,color='red',marker='*',s=5,label=l0  )
                plt.scatter(self.x1_class2,self.y1_class2,color='green',marker='*',s=5,label=l1  )
            

            




                #plt.plot(x,y1,color='black')
                #plt.plot(x,y2,label='b_decesion',color='black')
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
            
                #plt.scatter(self.x1_class2,self.y1_class2,color='red',marker='*',s=5,label=l0  )
                #plt.scatter(self.x2_class3,self.y2_class3,color='green',marker='*',s=5,label=l1  )
                plt.title(Title)
                plt.xlabel('X-AXIS')
                plt.ylabel('Y-AXIS')
                # plotting of  boundary desesion between the classes
                x=nm.arange(-4,5,0.1)
                #classifier Function

                
                # finding the matrics 
                
                m00=self.Var_Calc(self.x2_class3)
                m11=self.Var_Calc(self.y2_class3)
            
                m_00=self.Var_Calc(self.x1_class2)
                m_11=self.Var_Calc(self.y1_class2)
            
                m01=self.Covar_Calc(self.x2_class3,self.y2_class3)
                m10=self.Covar_Calc(self.x2_class3,self.y2_class3)

                m_01=self.Covar_Calc(self.x1_class2,self.y1_class2)
                m_10=self.Covar_Calc(self.x1_class2,self.y1_class2)

                # sigma matrics of given class
                sigm_matrics1=[[m00,m01],[m10,m11]]
                sigm_matrics2=[[m_00,m_01],[m_10,m_11]]

                # determinant of sigma matrics
            
                D1=m00*m11-m01*m10
                D2=m_00*m_11-m_01*m_10
                if(D1<0):
                    
                    D1=-1*D1
                if(D2<0):
                    
                    D2=-1*D2

            

            
                #calling inverse function to comput sigma inverse
                sigma_inverse1=self.Matrix_inv( sigm_matrics1)
                A=sigma_inverse1
                sigma_inverse2=self.Matrix_inv( sigm_matrics2)
                B=sigma_inverse2
                print('sigma inverse A:B:',A,B)




            
                print('mean of class:', M_class1,M_class2)

             
                #Cofficient calculation of require equation
                a0=1/2*(B[0][0]-A[0][0])
                b0=1/2*(B[0][1]-A[0][1])
                a1=1/2*(B[1][1]-A[1][1])
                b1=1/2*(B[1][0]-A[1][0])
                c0=((M_class1[0]*A[0][0]+M_class1[1]*A[1][0])-(M_class2[0]*B[0][0]+M_class2[1]*B[1][0]))
                d0=((M_class1[0]*A[0][1]+M_class1[1]*A[1][1])-(M_class2[0]*B[0][1]+M_class2[1]*B[1][1]))
                k1=-(1/2)*(M_class1[0]*(A[0][0]*M_class1[0] + A[0][1]*M_class1[1]) + M_class1[1]*(A[1][0]*M_class1[0] + A[1][1]*M_class1[1]))
                k2=(1/2)*(M_class2[0]*(B[0][0]*M_class2[0] + B[0][1]*M_class2[1]) + M_class1[1]*(B[1][0]*M_class2[0] + B[1][1]*M_class2[1]))
                k12=k1+k2
                k3=(1/2)* math.log((D2/D1),2)
                k0=k12 + k3
            
            
        
            
                #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
                y1=(-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)
                y2=(-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)


                A1=[[],[]]
                B1=[[],[]]
                y1=-2
                x=-5
                while(1):
                    y1=y1+.01
                    if(y1>2):
                        break
                    x=-5
                    while(1):
                        x=x+.01
                        if(x>5):
                            break
                        #di1=nm.linalg.det(sigm_matrics1)
                        #if(di1<0):
                            #di1=-1*di1
                        
                        
                        #d1=nm.dot([x,y1],nm.dot(A,[x,y1]))-math.log(2*3.14*math.pow(di1,0.5))
                        
                        d1 =(-y1 + (-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        #print(d1)
                        
                        #di2=nm.linalg.det(sigm_matrics2)
                        #if(di2<0):
                            #di2=-1*di2
                            
                        #d2=nm.dot([x,y1],nm.dot(B,[x,y1]))-math.log(2*3.14*math.pow(di2,0.5))
                        
                        d2=  ( -y1+ (-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/1000000000
                        d0=d1*d2
                        #print(d2)
                       
                        #print('d2',d2)
                        if(d0>0):
                            A1[0].append(x)
                            A1[1].append(y1)
                        else:
                            B1[0].append(x)
                            B1[1].append(y1)
                        

                
                #print('\n',B)
                print('lenth a',len(A1[0]))
                print('lenth b',len(B1[0]))
                plt.scatter(A1[0],A1[1],s=0.01)
                plt.scatter(B1[0],B1[1],s=0.01)
                plt.scatter(self.x1_class2,self.y1_class2,color='green',marker='*',s=5,label=l0  )
                plt.scatter(self.x2_class3,self.y2_class3,color='blue',marker='*',s=5,label=l1  )
            

            




                #plt.plot(x,y1,color='black')
                #plt.plot(x,y2,label='b_decesion',color='black')
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
            
                #plt.scatter(self.x1_class2,self.y1_class2,color='red',marker='*',s=5,label=l0  )
                #plt.scatter(self.x2_class3,self.y2_class3,color='green',marker='*',s=5,label=l1  )
                plt.title(Title)
                plt.xlabel('X-AXIS')
                plt.ylabel('Y-AXIS')
                # plotting of  boundary desesion between the classes
                x=nm.arange(-1,1,0.1)



                
                #classifier Function
                # finding the matrics 
                
                m00=self.Var_Calc(self.x_class1)
                m11=self.Var_Calc(self.y_class1)
            
                m_00=self.Var_Calc(self.x2_class3)
                m_11=self.Var_Calc(self.y2_class3)
            
                m01=self.Covar_Calc(self.x_class1,self.y_class1)
                m10=self.Covar_Calc(self.x_class1,self.y_class1)

                m_01=self.Covar_Calc(self.x2_class3,self.y2_class3)
                m_10=self.Covar_Calc(self.x2_class3,self.y2_class3)

                # sigma matrics of given class
                sigm_matrics1=[[m00,m01],[m10,m11]]
                sigm_matrics2=[[m_00,m_01],[m_10,m_11]]

                # determinant of sigma matrics
            
                D1=m00*m11-m01*m10
                D2=m_00*m_11-m_01*m_10
                if(D1<0):
                    
                    D1=-1*D1
                if(D2<0):
                    D2=-1*D2

            

            
                #calling inverse function to comput sigma inverse
                sigma_inverse1=self.Matrix_inv( sigm_matrics1)
                A=sigma_inverse1
                sigma_inverse2=self.Matrix_inv( sigm_matrics2)
                B=sigma_inverse2
                print('sigma inverse A:B:',A,B)

                print('mean of class:', M_class1,M_class2)
                
                #Cofficient calculation of require equation
                a0=1/2*(B[0][0]-A[0][0])
                b0=1/2*(B[0][1]-A[0][1])
                a1=1/2*(B[1][1]-A[1][1])
                b1=1/2*(B[1][0]-A[1][0])
                c0=((M_class1[0]*A[0][0]+M_class1[1]*A[1][0])-(M_class2[0]*B[0][0]+M_class2[1]*B[1][0]))
                d0=((M_class1[0]*A[0][1]+M_class1[1]*A[1][1])-(M_class2[0]*B[0][1]+M_class2[1]*B[1][1]))
                k1=-(1/2)*(M_class1[0]*(A[0][0]*M_class1[0] + A[0][1]*M_class1[1]) + M_class1[1]*(A[1][0]*M_class1[0] + A[1][1]*M_class1[1]))
                k2=(1/2)*(M_class2[0]*(B[0][0]*M_class2[0] + B[0][1]*M_class2[1]) + M_class1[1]*(B[1][0]*M_class2[0] + B[1][1]*M_class2[1]))
                k12=k1+k2
                k3=(1/2)* math.log((D2/D1),2)
                k0=k12 + k3
            
            
        
            
                #BELOW GIVEN EQUATION IS FOR RELATION BETWEEN X AND Y
                y1=(-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)
                y2=(-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1)


                A1=[[],[]]
                B1=[[],[]]
                y1=-2
                x=-5
                while(1):
                    y1=y1+.01
                    if(y1>2):
                        break
                    x=-5
                    while(1):
                        x=x+.01
                        if(x>5):
                            break
                        di1=nm.linalg.det(sigm_matrics1)
                        if(di1<0):
                            di1=-1*di1
                        
                        
                        d1=nm.dot([x,y1],nm.dot(A,[x,y1]))-math.log(2*3.14*math.pow(di1,0.5))
                        
                        #d1 =(-y1 + (-1*(b0+b1*x+d0)+((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/100000000000000
                        #print(d1)
                        
                        di2=nm.linalg.det(sigm_matrics2)
                        if(di2<0):
                            di2=-1*di2
                            
                        d2=nm.dot([x,y1],nm.dot(B,[x,y1]))-math.log(2*3.14*math.pow(di2,0.5))
                        
                        #d2=  ( -y1+ (-1*(b0+b1*x+d0)-((b0*x+b1*x+d0)**2-4*a1*(a0*x*x+c0*x +k0))**1/2)/(2*a1))/10000000000000
                        #d0=d1*d2
                        #print(d2)
                       
                        #print('d2',d2)
                        if(d2>d1):
                            A1[0].append(x)
                            A1[1].append(y1)
                        else:
                            B1[0].append(x)
                            B1[1].append(y1)
                        

                
                #print('\n',B)
                print('lenth a',len(A1[0]))
                print('lenth b',len(B1[0]))
                plt.scatter(A1[0],A1[1],s=0.01)
                plt.scatter(B1[0],B1[1],s=0.01)
                plt.scatter(self.x1_class2,self.y1_class2,color='red',marker='*',s=5,label=l0  )
                plt.scatter(self.x2_class3,self.y2_class3,color='green',marker='*',s=5,label=l1  )
            

            




                #plt.plot(x,y1,color='black')
                #plt.plot(x,y2,label='b_decesion',color='black')

             
                
                plt.legend()
                #plt.savefig('d2_c1_c3.png')
                plt.show()

                
                
                
          
                
             
               
                
            
          
           

if(__name__=='__main__'):

    
    s1=EquallSigmaDiagonalMatrics()
    s1.Equll_sigma_Diagonal_Classifier()
    
    
    
        
            
        
                
        
    


        
