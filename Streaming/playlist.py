from .arquivo_de_midia import *
from .musica import *
from .usuario import *

class Playlist:
    def __init__(self, nome:str, usuario:Usuario, 
                 itens:list[ArquivoDeMidia], reproducoes:int):
        self.nome = str(nome)
        self.usuario = Usuario(usuario)
        self.itens = []
        self.reproducoes = 0

    def adicionar_midia (self, midia:ArquivoDeMidia):
        if isinstance(midia, ArquivoDeMidia):
            self.itens.append(midia)
        else:
            raise TypeError("Arquivo não encontrado")
        
    def remover_midia (self, nome):
        if nome in self.itens:
            self.itens.remove(nome)
            return f"Midia removida"
        else:
            raise NameError("Midia não encontada")
        
    def reproduzir (self):
        for i in self.itens:
            print(i)
            i.reproducoes += 1
        self.reproducoes += 1
    
    