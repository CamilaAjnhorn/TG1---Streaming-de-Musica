from .arquivo_de_midia import *
from .utils import registrar_erro

class Podcast (ArquivoDeMidia):
    def __init__(self, titulo, duracao, artista,
                 episodio:int, temporada:str, host:str):
        super().__init__(titulo, duracao, artista)
        try:
            self.episodio = int(episodio)
            self.temporada = str(temporada)
            self.host = str(host)
        except Exception as e:
            registrar_erro(f"[Podcast] Erro ao registrar podcast: {e}")

    def reproduzir(self):
        try:
            return (f"Titulo: {self.titulo}\n"
                    f"{self.duracao} min\n"
                    f"Episodio: {self.episodio}\n"
                    f"Temporada: {self.temporada}\n"
                    f"Host: {self.host}\n")
        except Exception as e:
            registrar_erro(f"[Podcast] Erro ao reproduzir podcast '{self.titulo}': {e}")
    
    def __eq__(self, other):
        try:
            if isinstance(other, Podcast):
                if (other.episodio == self.episodio
                    and other.host == self.host
                    and other.temporada == self.temporada):
                    return True
                else:
                    return False
        except Exception as e:
            registrar_erro(f"[Podcast] Erro ao comparar podcasts: {e}")
            return f"Erro ao comparar podcasts"

    def __str__ (self):
        try:
            return (f"Título: {self.titulo}\n"
                    f"{self.duracao} min\n"
                    f"Episodio: {self.episodio}\n"
                    f"Temporada: {self.temporada}\n"
                    f"Host: {self.host}")
        except Exception as e:
            registrar_erro(f"[Podcast] Erro ao gerar __str__ de '{self.titulo}: {e}'")
            return f"[Erro ao exibir informações de '{self.titulo}']"
    
    def __repr__(self):
        try:
            return (f"titulo = {self.titulo} | duracao = {self.duracao}" 
                    f"| episodio = {self.episodio} | temporada = {self.temporada}" 
                    f"| host = {self.host}")
        except Exception as e:
            registrar_erro(f"[Podcast] Erro ao gerer __repr__: {e}")
            return f"Podcast(informações indisponíveis)"