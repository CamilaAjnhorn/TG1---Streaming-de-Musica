from .musica import *
from .arquivo_de_midia import *
from .podcast import *
from.utils import registrar_erro

class Usuario:
    qntd_instancias = 0
    
    def __init__(self, nome:str, playlists, historico):
        try:
            self.nome = str(nome)
            self.playlists = {}
            self.historico = []
            Usuario.qntd_instancias += 1
        except Exception as e:
            registrar_erro(f"[Usuario] Erro ao criar usuario: {e}")

    def ouvir_midia (self, midia:ArquivoDeMidia):
        try:
            if isinstance(midia, ArquivoDeMidia):
                self.historico.append()
                midia.reproduzir()
        except Exception as e:
            registrar_erro(f"[Usuario] Erro ao ouvir midia '{midia}': {e}")

    def criar_playlist (self, nome):
        try:
            if nome in self.playlists.keys():
                raise NameError("Você já tem uma playlist com esse nome")
            else:
                self.playlists[nome] = []
        except Exception as e:
            registrar_erro(f"[Usuario] Ero ao criar playlist: {e}")

    def __str__ (self):
        try:
            return (f"Nome: {self.nome}\n"
                    f"Playlists: {self.playlists}\n"
                    f"Histórico: {self.historico}\n")
        except Exception as e:
            registrar_erro(f"[Usuario] Erro ao gerar __str__: {e}")
            return f"[Erro ao exibir informações de '{self.nome}']"

    def __repr__(self):
        try:
            return (f"nome = {self.nome} | playlists = {self.playlists} | historico = {self.historico} | quantidade de usuarios = {Usuario.qntd_instancias}")
        except Exception as e:
            registrar_erro(f"[Usuario] Erro ao gerar __repr__: {e}")
            return f"Usuario(informações indispoiníveis)"
    