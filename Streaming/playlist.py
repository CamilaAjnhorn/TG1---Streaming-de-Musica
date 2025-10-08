from .arquivo_de_midia import *
from .musica import *
from .usuario import *
from .utils import registrar_erro

class Playlist:
    def __init__(self, nome:str, usuario:Usuario, 
                 itens:list[ArquivoDeMidia], reproducoes:int):
        try:
            self.nome = str(nome)
            self.usuario = usuario
            self.itens = list(itens)
            self.reproducoes = 0
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao gerar playlist: {e}")

    def adicionar_midia (self, midia:ArquivoDeMidia):
        try:
            if isinstance(midia, ArquivoDeMidia):
                self.itens.append(midia)
            else:
                raise TypeError("Arquivo não encontrado")
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao adicionar mídia '{midia}': {e}")
        
    def remover_midia (self, midia:ArquivoDeMidia):
        try:
            if midia in self.itens:
                self.itens.remove(midia)
                return f"Midia removida"
            else:
                raise NameError("Midia não encontada")
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao remover mídia '{midia}':{e}")
        
    def reproduzir (self):
        try:
            for i in self.itens:
                i.reproduzir()
            self.reproducoes += 1
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao reproduzir playlist '{self.nome}: {e}")
            return f"Erro ao reproduzir playlist '{self.nome}'"

    def __add__ (self, other):
        try:
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
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao unir playlists: {e}")
            return f"Erro ao unir playlists"

    def __len__ (self):
        try:
            return len(self.itens)
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao verificar tamanho da playlist: {e}")
            return f"Erro ao verificar tamanho da playlist"
        
    def __getitem__ (self, index):
        try:
            return self.itens[index]
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao encontrar item por index: {e}")
            return f"Erro ao encontrar item por index"
    
    def __eq__ (self, other):
        try:
            if isinstance(other, Playlist):
                if (self.usuario == other.usuario 
                    and self.nome == other.nome
                    and [m.titulo for m in self.itens] == [m.titulo for m in other.itens]):
                    return True
                else:
                    return False
            return False
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao comparar playlists: {e}")
            return f"Erro ao comparar playlists"
    
    def __str__ (self):
        try:
            return (f"Playlist: {self.nome}\n"
                    f"Usuario: {self.usuario}\n"
                    f"Itens: {self.itens}\n"
                    f"Reproduções: {self.reproducoes}")
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao gerar __str__ de '{self.nome}': {e}")
            return f"[Erro ao exibir informações de '{self.nome}']"
    
    def __repr__(self):
        try:
            return (f"nome = {self.nome} | usuario = {self.usuario} | itens = {self.itens} | reproduções = {self.reproducoes}")
        except Exception as e:
            registrar_erro(f"[Playlist] Erro ao gerar __repr__: {e}")
            return f"Playlist(informações indisponíveis)"