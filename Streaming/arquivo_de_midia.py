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

    def __str__(self):
        return (f"Titulo: {self.titulo}\n"
                f"{self.duracao} min\n"
                f"Artista: {self.artista}\n"
                f"Reproduções: {self.reproducoes}")
    
    def __repr__(self):
        return (f"titulo = {self.titulo} | duração = {self.duracao} |"
                f"artista = {self.artista} | reproducoes = {self.reproducoes}")