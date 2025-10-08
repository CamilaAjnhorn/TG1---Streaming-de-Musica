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
        mais_ativo = None
        for u in usuarios:
            if mais_ativo == None:
                mais_ativo = u
            elif len(u.historico) > len(mais_ativo.historico):
                mais_ativo = u
        return mais_ativo

    @staticmethod
    def media_avaliacoes (musicas:list[Musica]):
        dic = {}
        for m in musicas:
            if m._avaliacoes == 0:
                dic[m] = 0
            else:
                dic[m] = sum(m._avaliacoes) / len(m._avaliacoes)
        return dic
    
    @staticmethod
    def total_reproducoes (usuarios:list[Usuario]):
        total = 0
        for u in usuarios:
            total += len(u.historico)
        return total