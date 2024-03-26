## Python 3.11
class No:
    def __init__(self, x):
        self.chave = x
        self.prox = None
        self.esq = None
        self.dir = None
        self.pai = None

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
        x = f'palavra inserida: {inserida.chave}'
        return (x)
    
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
    
    def listaPorNumeroDeLetras(self, numeroDeLetras):
        contador = 0
        p = self.prim
        while p != None:
            if len(p.chave) == numeroDeLetras:
                print(p.chave)
                contador += 1
            p = p.prox
        if contador == 0:
            print('lista vazia')
     
    def listaOrdemAlfabetica (self, l1, l2):
         contador = 0
         p = self.prim
         while p != None:
             if l1 <= p.chave[0] <= l2:
                print(p.chave)
                contador += 1
             p = p.prox
         if contador == 0:
            print('lista vazia')
    
    def imprime(self):
        p = self.prim
        if p == None:
            print('lista vazia')
        while p!= None:
            print(p.chave)
            p = p.prox

class Arvore:
    def __init__(self):
     self.raiz = None
        
    def buscaArvore(self, palavra):
        atual = self.raiz
        while  (atual != None) and (palavra != atual.chave):
            if (palavra < atual.chave):
             atual = atual.esq
            else:
             atual = atual.dir
        if atual != None:
            print(f'palavra já existente: {palavra}')
            return True
        else:
            print(f'palavra inexistente: {palavra}')
            return False
              

    def inserirArvore(self, no):
        self.pai = None
        atual = self.raiz

        while (atual is not None) and (no.chave != atual.chave):
            self.pai = atual
            if (no.chave < atual.chave):
                atual = atual.esq
            else:
                atual = atual.dir

        if (atual != None):
            print(f'palavra já existente: {no.chave}')
            return
        else:
            no.pai = self.pai
        if self.pai is None:
            self.raiz = no
        elif no.chave < self.pai.chave:
            self.pai.esq = no
        else:
            self.pai.dir = no
        print(f'palavra inserida: {no.chave}')
       
        
    def imprimeArvore(self,raiz): 
    
        if raiz:
            if(raiz.esq and raiz.dir):
                print(f'palavra: {raiz.chave} fesq:{raiz.esq.chave} fdir: {raiz.dir.chave}')
                self.imprimeArvore(raiz.esq)
                self.imprimeArvore(raiz.dir)
            elif(raiz.esq == None) and (raiz.dir == None):
                print(f'palavra: {raiz.chave} fesq: nil fdir: nil')
                self.imprimeArvore(raiz.esq)
                self.imprimeArvore(raiz.dir)
            elif(raiz.esq == None):
                print(f'palavra: {raiz.chave} fesq: nil fdir: {raiz.dir.chave}')
                self.imprimeArvore(raiz.esq)
                self.imprimeArvore(raiz.dir)
            else:
                print(f'palavra: {raiz.chave} fesq:{raiz.esq.chave} fdir: nil')
                self.imprimeArvore(raiz.esq)
                self.imprimeArvore(raiz.dir)
    

    def listaOrdemAlfabetica(self, letra1, letra2):
        if (self.raiz == None):
            print('lista vazia')
        else:
            self.listaOrdemAlfabeticaRecurssiva(self.raiz, letra1, letra2)

    def listaOrdemAlfabeticaRecurssiva(self, no, letra1, letra2):
        if (no != None):
            self.listaOrdemAlfabeticaRecurssiva(no.esq, letra1, letra2)
            if (letra1 <= no.chave[0] <= letra2):
                print(no.chave)
            self.listaOrdemAlfabeticaRecurssiva(no.dir, letra1, letra2)
    

    def minimoArvore(self, raiz):
        atual = raiz
        while atual.esq != None:
            atual = atual.esq
        return atual


    def removeArvore(self, raiz, palavraRemovida): ## as vezes está printando ''palavra removida: {palavraRemovida}' duas vezes, porém está removendo 
        if (raiz == None) or (self.buscaArvore == False) :
            print(f'palavra inexistente: {palavraRemovida}')
            return 

        if (palavraRemovida < raiz.chave):
            raiz.esq = self.removeArvore(raiz.esq, palavraRemovida)
        elif (palavraRemovida > raiz.chave):
            raiz.dir = self.removeArvore(raiz.dir, palavraRemovida)
        else:
            if (raiz.esq == None):
                return raiz.dir
            elif (raiz.dir == None):
                return raiz.esq
            raiz.chave = self.minimoArvore(raiz.dir).chave
            raiz.dir = self.removeArvore(raiz.dir, raiz.chave)
        
        print(f'palavra removida: {palavraRemovida}')
        return raiz

            



lista1 = Lista()
lista2 = Lista()
arvore = Arvore()
    
while True:
    comando = input()
    if comando == 'e':
        break
    
    if comando == 'i':
        palavra = input()
        p = No(palavra)
        if len(palavra) <= 5:
            resultado = lista1.insere(p)
        elif len(palavra) >= 6:
            resultado = lista2.insere(p)
        arvore.inserirArvore(p)
        
    if comando == 'r':
        palavraRemovida = input()
        t = No(palavraRemovida)
        if len(palavraRemovida) <= 5:
            resultado = lista1.remove(t)
        elif len(palavraRemovida) >= 6:
            resultado = lista2.remove(t)
        arvore.raiz = arvore.removeArvore(arvore.raiz, palavraRemovida)
                
        
    if comando == 'l':
        numerolista = int(input())
        if numerolista == 1:
            lista1.imprime()
        elif numerolista == 2:
            lista2.imprime()
    
    if comando == "c":
        palavra = input()
        arvore.buscaArvore(palavra)
    
    if comando == "p":
        if arvore.raiz == None:
            print('arvore vazia')
        else:
            arvore.imprimeArvore(arvore.raiz)
        
    if comando == 'x':
        numeroDeLetras = int(input())
        if numeroDeLetras <= 5:
            lista1.listaPorNumeroDeLetras(numeroDeLetras)
        else:
            lista2.listaPorNumeroDeLetras(numeroDeLetras)
        
    
    if comando == 'o':
        letra1 = input()
        letra2 = input()
        arvore.listaOrdemAlfabetica(letra1, letra2)
        
        

    