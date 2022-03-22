class Logger:
    def log(self,mensaje,x):
        f= open('cat log.txt','a+')
        if (x==1):
            f.write('--Start log--'+'\n')
        
        f.write(str(mensaje))
        f.write('\n')
        
        if(x==5):
            f.write('--End log:--')
            f.write(str(x))
            f.write('log(s)--')
            f.close

class Test:
    def llamada(self,mensaje,x):
        Logger.log(mensaje,x)
