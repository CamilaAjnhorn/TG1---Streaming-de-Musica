from .musica import *
from .playlist import *
from .usuario import * 

class Analises:
    @staticmethod
    def top_musicas (musicas:list[Musica], top_n:int = 5):
        mais_rep = [m for m in musicas[:top_n]]
        rep_mus = {m.reproducoes : idx for idx, m in enumerate(mais_rep)}

        for m in musicas:
            if m.reproducoes > min(rep_mus.keys()):
                mais_rep[rep_mus[min(rep_mus.keys())]] = m

        return mais_rep
    
    @staticmethod
    def playlist_mais_popular (playlists:list[Playlist]):
        mais_rep = None
        for p in playlists:
            if p.reproducoes > mais_rep:
                mais_rep = p

        return mais_rep
    
    @staticmethod
    def usuario_mais_ativo (usuarios:list[Usuario]):
        pass
