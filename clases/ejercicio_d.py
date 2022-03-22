class Logger:
    def log(self,mensaje,x):
        f= open('registry.txt','a+')
        if (x==1):
            f.write('--Start log--')

class Test:
    def llamada(self,mensaje):
        print()
