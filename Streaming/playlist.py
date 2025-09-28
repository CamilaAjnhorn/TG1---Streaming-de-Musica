from .arquivo_de_midia import *
from .musica import *
from .usuario import *

class Playlist:
    def __init__(self, nome:str, usuario:Usuario, 
                 itens:list[ArquivoDeMidia], reproducoes:int):
        self.nome = str(nome)
        self.usuario = usuario
        self.itens = list(itens)
        self.reproducoes = 0

    def adicionar_midia (self, midia:ArquivoDeMidia):
        if isinstance(midia, ArquivoDeMidia):
            self.itens.append(midia)
        else:
            raise TypeError("Arquivo não encontrado")
        
    def remover_midia (self, midia:ArquivoDeMidia):
        if midia in self.itens:
            self.itens.remove(midia)
            return f"Midia removida"
        else:
            raise NameError("Midia não encontada")
        
    def reproduzir (self):
        for i in self.itens:
            i.reproduzir()
        self.reproducoes += 1
    
    def __add__ (self, other):
        if isinstance(other, Playlist):
            nova = Playlist(
                self.nome,
                self.usuario,
            )
            nova.itens = self.itens + other.itens
            nova.reproducoes = self.reproducoes + nova.reproducoes

            return nova
        else:
            raise TypeError("Só é possível concatenar com outra Playlist.")
        
    def __len__ (self):
        return len(self.itens)
    
    def __getitem__ (self, index):
        return self.itens[index]
    
    def __eq__ (self, other):
        if isinstance(other, Playlist):
            if (self.usuario == other.usuario 
                and self.nome == other.nome
                and [m.titulo for m in self.itens] == [m.titulo for m in other.itens]):
                return True
            else:
                return False
        return False
    
    def __str__ (self):
        return (f"Playlist: {self.nome}\n"
                f"Usuario: {self.usuario}\n"
                f"Itens: {self.itens}\n"
                f"Reproduções: {self.reproducoes}")
    
    def __repr__(self):
        return (f"nome = {self.nome} | usuario = {self.usuario} | itens = {self.itens} | reproduções = {self.reproducoes}")