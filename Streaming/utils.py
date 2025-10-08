import datetime
import os
from .analises import Analises
from .musica import *
from .playlist import *
from .usuario import *
from .podcast import *

def registrar_erro (mensagem:str):
    caminho_logs = "logs"
    
    arquivo_log = os.path.join(caminho_logs, "erros.log")

    with open (arquivo_log, "a") as log:
        momento = datetime.datetime.now()

        log.write(f"{momento} {mensagem}\n")

def gerar_relatorio (musicas:list[Musica], playlists:list[Playlist], usuarios:list[Usuario]):
    try:
        caminho = os.path.join("relatorios", "relatorio.txt")

        with open(caminho, "w") as f:
            f.write("=== RELATÓRIO DO SISTEMA DE STREAMING ===\n")
            f.write(f"Gerado em: {datetime.now()}")

            #top musicas
            f.write("Top músicas mais reproduzidas:")
            top = Analises.top_musicas(musicas)
            for m in top:
                f.write(f"- {m.titulo} ({m.reproducoes} reproduções)\n")
            f.write("\n")

            # playlist mais popular
            p = Analises.playlist_mais_popular(playlists)
            if p:
                f.write(f"Playlist mais popular: {p.nome} ({p.reproducoes} reproduções)\n")
            
            # usuario mais ativo
            u = Analises.usuario_mais_ativo(usuarios)
            if u:
                f.write(f"Usuário mais ativo: {u.nome} ({len(u.historico)} músicas ouvidas)\n")

            # media de avaliações
            f.write("Media de avaliações das músicas:\n")
            medias = Analises.media_avaliacoes(musicas)
            for titulo, media in medias.items():
                f.write(f"- {titulo}: {media} estrelas")
            f.write("\n")

            # total de reproduções
            total = Analises.total_reproducoes(usuarios)
            f.write(f"Total de reproduções no sistema: {total}\n")
        
        print("Relatório gerado com sucesso!")
    except Exception as e:
        registrar_erro(f"[Relatorio] Erro ao gerar relatório")