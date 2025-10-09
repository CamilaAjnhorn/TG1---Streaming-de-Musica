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
    podcasts = []
    secao_atual = None

    try:
        with open(caminho, "r") as f:
            linhas = [linha.strip() for linha in f if linha.strip()]

        i = 0
        
        while i < len(linhas):
            linha = linhas[i]

            if linha.startswith("# "):
                secao_atual = linha[2:].strip().lower()
                i += 1
                continue

            # usuarios
            if secao_atual == "usuários" and linha.startswith("- nome:"):
                try:
                    nome = linha.split(":")[1].strip()
                    playlists_str = linhas[i + 1].split(":")[1].strip(" []")
                    nomes_playlists = [p.strip() for p in playlists_str.split(",") if p.strip()]
                    
                    if any (u.nome == nome for u in usuarios):
                        registrar_erro(f"[Config] Usuário duplicado: {nome}")
                    else:
                        usuarios.append(Usuario(nome, {}, []))
                    
                    i += 2        
                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar usuario na linha {i + 1}: {e}")
                    i += 1
                continue

            # musicas
            if secao_atual == "músicas" and linha.startswith("- titulo:"):
                try:
                    titulo = linha.split(":")[1].strip()
                    artista = linhas[i + 1].split(":")[1].strip()
                    genero = linhas[i + 2].split(":")[1].strip()
                    duracao = int(linhas[i + 3].split(":")[1].strip())

                    if duracao <= 0:
                        registrar_erro(f"[Config] Duração inválida para '{titulo}': {duracao}")              
                        duracao = 1

                    if genero not in ["Rock", "Pop", "Rap", "Classico"]:
                        registrar_erro(f"[Config] Gênero inválido '{genero}' em '{titulo}'")
                        genero = "Desconhecido"

                    musicas.append(Musica(
                        titulo, 
                        duracao, 
                        artista, 
                        genero,
                        []
                    ))

                    i += 4
                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar música na linha {i + 1}: {e}")
                    i += 1
                continue

            # podcasts
            if secao_atual == "podcasts" and linha.startswith("- titulo"):
                try:
                    titulo = linha.split(":")[1].strip()
                    temporada = linhas[i + 1].split(":")[1].strip()
                    episodio_raw = linhas[i + 2].split(":")[1].strip()
                    host = linhas[i + 3].split(":")[1].strip()
                    duracao = int(linhas[i + 4].split(":")[1].strip())

                    try:
                        episodio = int(episodio_raw)
                    except ValueError:
                        registrar_erro(f"[Config] Episódio inválido '{episodio_raw}' no podcast '{titulo}'")
                        episodio = 0

                    if duracao <= 0:
                        registrar_erro(f"[Config] Duração inválida no podcast '{titulo}'")
                        duracao = 60

                    podcasts.append(Podcast(
                        titulo, 
                        duracao,
                        host,
                        episodio,
                        temporada,
                        host
                    ))

                    i += 5

                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar podcast na linha '{i + 1}: {e}'")
                    i +=1
                continue

            # playlists
            if secao_atual == "playlists" and linha.startswith("- nome:"):
                try:
                    nome = linha.split(":")[1].strip()
                    usuario = linhas[i + 1].split(":")[1].strip()
                    itens_raw = linhas[i + 2].split(":")[1].strip(" []")
                    item_nomes = [x.strip() for x in itens_raw.split(",") if x.strip()]

                    usuario_obj = next((u for u in usuarios if u.nome == usuario), None)
                    if not usuario_obj:
                        registrar_erro(f"[Config] Playlist '{nome}' com usuário inexistente: {usuario}")
                        i += 3
                        continue

                    playlist = Playlist(nome, usuario_obj, [])

                    for item_nome in item_nomes:
                        midia = next((m for m in musicas if m.titulo == item_nome), None)
                        if not midia:
                            midia = next((p for p in podcasts if p.titulo == item_nome))
                        if midia:
                            playlist.adicionar_midia(midia)
                        else:
                            registrar_erro(f"[Config] Mídia inexistente '{item_nome}' na playlist '{nome}'")

                    playlists.append(playlist)

                    i += 3

                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar playlist na linha {i + 1}: {e}")
                    i += 1
                continue
            
            i += 1

        return musicas, usuarios, playlists, podcasts
    
    except Exception as e:
        registrar_erro(f"[Config] Erro ao carregar dados do arquivo Markdown: {e}")
        return [], [], [], []
    