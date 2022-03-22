from clases.ejercicio_c import *


def main():
    acabar=False
    while(acabar==False):
        seguir=str(input('Quieres seguir viendo ejercicios(S/N)?:'))    
        if(seguir=='s' or seguir=='S'):
            cual=str(input('Que ejercicio quieres ver (a,b,c,d)?:'))
            if(cual=='a' or cual=='A'):
                print('Ejercicio A:\n')

            elif(cual=='b' or cual=='B'):
                print('Ejercicio B:\n')

            elif(cual=='c' or cual=='C'):
                print('Ejercicio C:\n')
        
                a = A 
                y = a.z 
                print(y(a)) 
                aa = a() 
                print(aa is a()) 
                z = aa.y 
                print(z(())) 
                print(a().y((a,))) 
                print(A.y(aa, (a,z))) 
                print(aa.y((z,1,'z')))

            elif(cual=='d' or cual=='D'):
                print('Ejercicio D:\n')
                test = Test() 
                for i in range(1, 6): 
                    if i == 1: 
                        test.llamada("Primera llamada") 
                    else: 
                        test.llamada("{}ª llamada".format(string))

            else:
                print('Eso no es un 4, un 5 o un 6.')
        if(seguir=='n' or seguir=='N'):
            acabar=True
        else:
            print('Introduzca una N o una S')

if __name__=='__main__':
    main()