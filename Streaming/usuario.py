from .musica import *
from .arquivo_de_midia import *
from .podcast import *

class Usuario:
    qntd_instancias = 0
    
    def __init__(self, nome:str, playlists, historico):
        self.nome = str(nome)
        self.playlists = {}
        self.historico = []
        Usuario.qntd_instancias += 1

    def ouvir_midia (self, midia:ArquivoDeMidia):
        if isinstance(midia, ArquivoDeMidia):
            self.historico.append()
            midia.reproduzir()

    def criar_playlist (self, nome):
        if nome in self.playlists.keys():
            raise NameError("Você já tem uma playlist com esse nome")
        else:
            self.playlists[nome] = []

    def __str__ (self):
        return (f"Nome: {self.nome}\n"
                f"Playlists: {self.playlists}\n"
                f"Histórico: {self.historico}\n")
    
    def __repr__(self):
        return (f"nome = {self.nome} | playlists = {self.playlists} | historico = {self.historico} | quantidade de usuarios = {Usuario.qntd_instancias}")

    