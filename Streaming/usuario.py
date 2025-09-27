from .musica import *
from .arquivo_de_midia import *
from .podcast import *

class Usuario:
    qntd_instancias = 0
    
    def __init__(self, nome:str, playlists, historico):
        self.nome = str(nome)
        self.playlists = []
        self.historico = []
        Usuario.qntd_instancias += 1

    def ouvir_midia (self, midia:ArquivoDeMidia):
        if isinstance(midia, ArquivoDeMidia):
            self.historico.append()
            midia.reproduzir()

    def criar_playlist (self, nome):
        pass