class No:
    def __init__(self, conteudo, proximo=None):
        self.conteudo = conteudo
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def insere_no_fim(self, x):
        novo = No(x)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.tamanho += 1

    def imprime_primeiros_cinco(self):
        atual = self.cabeca
        contador = 0
        while atual and contador < 5:
            print(atual.conteudo)
            atual = atual.proximo
            contador += 1

    def insere_no_inicio(self, x):
        novo = No(x, self.cabeca)
        self.cabeca = novo
        self.tamanho += 1

    def remove_primeiro(self):
        if self.cabeca is not None:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1

    def remove_impares(self):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.conteudo % 2 != 0:  # Verifica se é ímpar
                if anterior is None:  # Se o nó atual é a cabeça
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
            else:
                anterior = atual
            atual = atual.proximo

    def tamanho_lista(self):
        return self.tamanho

# Exemplo de uso
lista = Lista()
lista.insere_no_fim(1)
lista.insere_no_fim(2)
lista.insere_no_fim(3)
lista.insere_no_fim(4)
lista.insere_no_fim(5)
lista.insere_no_fim(6)

print("Primeiros cinco elementos:")
lista.imprime_primeiros_cinco()

print("\nInserindo no início:")
lista.insere_no_inicio(0)
lista.imprime_primeiros_cinco()

print("\nRemovendo o primeiro elemento:")
lista.remove_primeiro()
lista.imprime_primeiros_cinco()

print("\nRemovendo números ímpares:")
lista.remove_impares()
atual = lista.cabeca
while atual:
    print(atual.conteudo)
    atual = atual.proximo

print("\nTamanho da lista:", lista.tamanho_lista())
