## Python 3.11
class No:
    def __init__(self, x):
        self.chave = x
        self.prox = None
        self.prox4 = None

class Lista:
    def __init__(self):
        self.prim = None

    def insere(self, inserida):
        p = self.prim
        while p != None:
            if p.chave == inserida.chave:
                return
            p = p.prox
        p = avalia = self.prim
        while p != None and inserida.chave > p.chave : 
            avalia = p
            p = p.prox
        if self.prim == None or inserida.chave < self.prim.chave:
            inserida.prox = self.prim
            self.prim = inserida
        else:
            inserida.prox = avalia.prox
            avalia.prox = inserida 
        x = f'Palavra inserida: {inserida.chave}'
        return (x)
        
    
    def insere4 (self, inserida):
        p = self.prim
        while p != None:
            if p.chave == inserida.chave:
                return
            p = p.prox4
        p = avalia = self.prim
        while p != None and inserida.chave > p.chave :
            avalia = p
            p = p.prox4
        if self.prim == None or inserida.chave < self.prim.chave:
            inserida.prox4 = self.prim
            self.prim = inserida
        else:
            inserida.prox4 = avalia.prox4
            avalia.prox4 = inserida

    def remove(self, removida):
        p = self.prim
        avalia = None

        while p != None and p.chave != removida.chave:
            avalia = p
            p = p.prox

        if p == None:
            return f'palavra inexistente:{removida.chave}'

        if avalia == None:
            self.prim = p.prox
        else:
            avalia.prox = p.prox
        return f'palavra removida:{removida.chave}'
    
    def remove4(self, removida):
        p = self.prim
        avalia = None

        while p != None and p.chave != removida.chave:
            avalia = p
            p = p.prox4

        if p == None:
            return f'palavra inexistente:{removida.chave}'

        if avalia == None:
            self.prim = p.prox4
        else:
            avalia.prox4 = p.prox4

        return f'palavra removida:{removida.chave}'
    
            
    def listaPorNumeroDeLetras(self, numeroDeLetras):
         contador = 0
         p = self.prim
         while p != None:
             if len(p.chave) == numeroDeLetras:
                 print(p.chave)
                 contador += 1
             p = p.prox4
         if contador == 0:
            print('lista vazia')
        
    def listaOrdemAlfabetica (self, l1, l2):
         contador = 0
         p = self.prim
         while p != None:
             if l1 <= p.chave[0] <= l2:
                print(p.chave)
                contador += 1
             p = p.prox4
         if contador == 0:
            print('lista vazia')
    
    def imprime(self):
        p = self.prim
        if p == None:
            print('lista vazia')
        while p!= None:
            print(p.chave)
            p = p.prox

    def imprime4(self):
        p = self.prim
        if p == None:
            print('lista vazia')
        while p!= None:
            print(p.chave)
            p = p.prox4
    
lista1 = Lista()
lista2 = Lista()
lista3 = Lista()
lista4 = Lista()

while True:
    comando = input()
    if comando == 'e':
        break
    
    if comando == 'i':
        palavra = input()
        p = No(palavra)
        if len(palavra) <= 5:
            resultado = lista1.insere(p)
        elif len(palavra) >= 6 and len(palavra) <= 10:
            resultado = lista2.insere(p)
        else:
            resultado = lista3.insere(p)
        lista4.insere4(p)
        print(resultado)
        
    if comando == 'r':
        palavraRemovida = input()
        t = No(palavraRemovida)
        if len(palavraRemovida) <= 5:
            resultado = lista1.remove(t)
        elif len(palavraRemovida) >= 6 and len(palavraRemovida) <= 10:
            resultado = lista2.remove(t)
        else:
            resultado = lista3.remove(t)
        lista4.remove4(t)
        print(resultado)
        
    if comando == 'l':
        numerolista = int(input())
        if numerolista == 1:
            lista1.imprime()
        elif numerolista == 2:
            lista2.imprime()
        elif numerolista == 3:
            lista3.imprime()
        elif numerolista == 4:
            lista4.imprime4()

    if comando == 'x':
        numeroDeLetras = int(input())
        lista4.listaPorNumeroDeLetras(numeroDeLetras)

    if comando == 'o':
        l1 = input()
        l2 = input()
        lista4.listaOrdemAlfabetica(l1, l2)