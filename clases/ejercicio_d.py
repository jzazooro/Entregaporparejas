from encodings import utf_8


class Logger:
    def log(self,mensaje,x):
        f= open('cat log.txt','a+')
        if (x==1):
            f.write('--Start log--'+'\n')
        
        
        if(x==5):
            f.write('--End log:--')
            f.write(str(x))
            f.write('log(s)--')
            f.close

class Test:
    def llamada(self,mensaje):
        print()
