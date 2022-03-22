class Logger:
    def log(self,mensaje,x):
        f= open('cat log.txt','a+')
        if (x==1):
            f.write('--Start log--'+'\n')


class Test:
    def llamada(self,mensaje):
        print()
