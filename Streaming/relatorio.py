import os
import datetime
from .analises import Analises
from .utils import registrar_erro

def gerar_relatorio (musicas:list, playlists:list, usuarios:list, podcasts:list):
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
