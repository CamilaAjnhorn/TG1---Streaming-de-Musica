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

def carregar_dados_md (caminho = "config/dados.md"):
    musicas = []
    usuarios = []
    playlists = []
    secao_atual = None

    try:
        with open(caminho, "r") as f:
            for linha in f:
                linha = linha.strip()

                if linha.startswith("# "):
                    secao_atual = linha[2:].strip().lower()
                    continue

                if linha == "---" or linha == "":
                    continue

                if secao_atual == "usuários":
                    if linha.startswith("- nome:"):
                        nome = linha.split(":")[1].strip()
                        usuarios.append(Usuario(nome))
                
                elif secao_atual == "músicas":
                    if linha.startswith("- titulo:"):
                        titulo = linha.split(":")[1].strip()
                        artista = f.readline().split(":")[1].strip()
                        duracao = int(f.readline().split(":")[1].strip())
                        genero = f.readline().split(":")[1].strip()
                        aval = f.readline().split(":")[1].strip()
                        avaliacoes = [int(x) for x in aval.strip("[]").split(",")]
                        musicas.append(Musica(
                            titulo,
                            duracao,
                            artista,
                            genero,
                            avaliacoes
                        ))
                elif secao_atual == "playlists":
                    if linha.startswith("- nome:"):
                        nome = linha.split(":")[1].strip()
                        usuario = f.readline().split(":")[1].strip()
                        musicas_str = f.readline().split(":")[1].strip()
                        nomes = [x.strip() for x in musicas_str.strip("[]").split(",")]
                        playlists.append(nome, usuario, nomes)

        return musicas, usuarios, playlists
    except Exception as e:
        registrar_erro(f"[Config] Erro ao carregar dados do arquivo Markdown: {e}")
        return [], [], []
    