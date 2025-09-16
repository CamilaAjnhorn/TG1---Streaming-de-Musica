from abc import ABC, abstractmethod

class ArquivoDeMidia(ABC):
    def __init__(
                 self, 
                 titulo:str,
                 duracao:int,
                 artista:str
                ):
        self.titulo = str(titulo)
        self.duracao = int(duracao)
        self.artista = str(artista)
        self.reproducoes = 0

    @abstractmethod
    def reproduzir(self):
        pass
        
    @abstractmethod
    def __eq__ (self, other):
        pass