from .musica import *
from .playlist import *
from .usuario import * 
from .utils import registrar_erro

class Analises:
    
    """
    Percorre as musicas cadastras e retorna as to 5 musicas mais reproduzidas
    """
    @staticmethod
    def top_musicas (musicas:list["Musica"], top_n:int = 5):
        mais_rep = [m for m in musicas[:top_n]]
        rep_mus = {m.reproducoes : idx for idx, m in enumerate(mais_rep)}

        try:
            for m in musicas:
                if m.reproducoes > min(rep_mus.keys()):
                    mais_rep[rep_mus[min(rep_mus.keys())]] = m

            return mais_rep
        except Exception as e:
            registrar_erro(f"[Analises] Erro ao gerar top_musicas: {e}")
    
    """
    percorre as playlists existentes e retorna a mais escutada
    """
    @staticmethod
    def playlist_mais_popular (playlists:list["Playlist"]):
        mais_rep = None
        
        try:
            for p in playlists:
                if p.reproducoes > mais_rep:
                    mais_rep = p

            return mais_rep
        except Exception as e:
            registrar_erro(f"[Analises] Erro ao encontrar playlist mais popular: {e}")
    
    """
    percorre os usuarios ecistentes e retorna o mais ativo
    (o que mais ouviu musicas)
    """
    @staticmethod
    def usuario_mais_ativo (usuarios:list["Usuario"]):
        mais_ativo = None
        
        try:
            for u in usuarios:
                if mais_ativo == None:
                    mais_ativo = u
                elif len(u.historico) > len(mais_ativo.historico):
                    mais_ativo = u
            return mais_ativo
        except Exception as e:
            registrar_erro(f"[Analises] Erro ao encontrar usuario mais ativo: {e}")

    """
    faz a media das avaliações das musicas e retorna um dicionario com as informações
    """
    @staticmethod
    def media_avaliacoes (musicas:list["Musica"]):
        dic = {}

        try:
            for m in musicas:
                if  not m._avaliacoes:
                    dic[m.titulo] = 0
                else:
                    dic[m.titulo] = sum(m._avaliacoes) / len(m._avaliacoes)
            return dic
        except Exception as e:
            registrar_erro(f"[Analises] Erro ao gerar dicionário de médias: {e}")
    
    """
    percorre todos os usuarios e retorna o total te reproduções
    """
    @staticmethod
    def total_reproducoes (usuarios:list["Usuario"]):
        total = 0
        
        try:
            for u in usuarios:
                total += len(u.historico)
            return total
        except Exception as e:
            registrar_erro(f"[Analises] Erro ao contabilizar reproduções: {e}")