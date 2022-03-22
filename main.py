from clases import *

acabar=False
while(acabar==False):
    seguir=str(input('Quieres seguir viendo ejercicios(S/N)?:'))    
    if(seguir=='s' or seguir=='S'):
        cual=str(input('Que ejercicio quieres ver (4,5,6)?:'))
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

        else:
            print('Eso no es un 4, un 5 o un 6.')
    if(seguir=='n' or seguir=='N'):
        acabar=True
    else:
        print('Introduzca una N o una S')
