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
        print(f"Titulo: {self.titulo}/n"
              f"Artista: {self.artista}/n"
              f"Duração: {self.duracao}")
        
    @abstractmethod
    def __eq__ (self, other):
        if isinstance(other, ArquivoDeMidia):
            return self.titulo == other.titulo