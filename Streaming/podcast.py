from .arquivo_de_midia import *

class Podcast (ArquivoDeMidia):
    def __init__(self, titulo, duracao, artista,
                 episodio:int, temporada:str, host:str):
        super().__init__(titulo, duracao, artista)
        
        self.episodio = int(episodio)
        self.temporada = str(temporada)
        self.host = str(host)

    def reproduzir(self):
        return (f"Titulo: {self.titulo}\n"
                f"{self.duracao} min\n"
                f"Episodio: {self.episodio}\n"
                f"Temporada: {self.temporada}\n"
                f"Host: {self.host}\n")
    
    def __eq__(self, other):
        if isinstance(other, Podcast):
            if (other.episodio == self.episodio
                and other.host == self.host
                and other.temporada == self.temporada):
                return True
            else:
                return False

    def __str__ (self):
        return (f"Título: {self.titulo}\n"
                f"{self.duracao} min\n"
                f"Episodio: {self.episodio}\n"
                f"Temporada: {self.temporada}\n"
                f"Host: {self.host}")
    
    def __repr__(self):
        return (f"titulo = {self.titulo} | duracao = {self.duracao}" 
                f"| episodio = {self.episodio} | temporada = {self.temporada}" 
                f"| host = {self.host}")