class Logger:
    def log(self,mensaje,x):
        f= open('cat log.txt','a+')
        if (x==1):
            f.write('--Start log--'+'\n')
        elif(x==5):
            f.write('--End log:--'+'\n')
            f.write(str(x))

class Test:
    def llamada(self,mensaje):
        print()
