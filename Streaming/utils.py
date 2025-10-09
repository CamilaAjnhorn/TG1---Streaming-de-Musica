import datetime
import os

def registrar_erro (mensagem:str):
    caminho_logs = "logs"
    
    arquivo_log = os.path.join(caminho_logs, "erros.log")

    with open (arquivo_log, "a") as log:
        momento = datetime.datetime.now()

        log.write(f"{momento} {mensagem}\n")


def carregar_dados_md(caminho="config/dados.md"):
    from .modelos import Musica, Podcast, Playlist, Usuario

    musicas = []
    usuarios = []
    playlists = []
    podcasts = []

    def registrar_erro(msg):
        print(msg)  # substitua pelo seu logger, se houver

    try:
        with open(caminho, "r") as f:
            linhas = [linha.strip() for linha in f if linha.strip()]

        secao_atual = None
        secoes = {"usuarios": [], "musicas": [], "podcasts": [], "playlists": []}

        # separar linhas por seção
        for linha in linhas:
            if linha.startswith("# "):
                secao_atual = linha[2:].strip().lower()
            elif secao_atual:
                secoes[secao_atual].append(linha)

        # ----------------------
        # Carregar Usuários
        # ----------------------
        i = 0
        linhas_u = secoes.get("usuarios", [])
        while i < len(linhas_u):
            if linhas_u[i].startswith("- nome:"):
                nome = linhas_u[i].split(":")[1].strip()
                # playlists serão adicionadas depois
                usuarios.append(Usuario(nome, {}, []))
            i += 1

        # ----------------------
        # Carregar Músicas
        # ----------------------
        linhas_m = secoes.get("musicas", [])
        i = 0
        while i < len(linhas_m):
            if linhas_m[i].startswith("- titulo:"):
                try:
                    titulo = linhas_m[i].split(":")[1].strip()
                    artista = linhas_m[i+1].split(":")[1].strip()
                    genero = linhas_m[i+2].split(":")[1].strip()
                    duracao = int(linhas_m[i+3].split(":")[1].strip())
                    if duracao <= 0:
                        registrar_erro(f"[Config] Duração inválida em '{titulo}'")
                        duracao = 1
                    musicas.append(Musica(titulo, duracao, artista, genero, []))
                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar música: {e}")
                i += 4
            else:
                i += 1

        # ----------------------
        # Carregar Podcasts
        # ----------------------
        linhas_p = secoes.get("podcasts", [])
        i = 0
        while i < len(linhas_p):
            if linhas_p[i].startswith("- titulo:"):
                try:
                    titulo = linhas_p[i].split(":")[1].strip()
                    temporada = linhas_p[i+1].split(":")[1].strip()
                    episodio = int(linhas_p[i+2].split(":")[1].strip())
                    host = linhas_p[i+3].split(":")[1].strip()
                    duracao = int(linhas_p[i+4].split(":")[1].strip())
                    podcasts.append(Podcast(titulo, duracao, host, episodio, temporada, host))
                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar podcast: {e}")
                i += 5
            else:
                i += 1

        # ----------------------
        # Carregar Playlists
        # ----------------------
        linhas_pl = secoes.get("playlists", [])
        i = 0
        while i < len(linhas_pl):
            if linhas_pl[i].startswith("- nome:"):
                try:
                    nome = linhas_pl[i].split(":")[1].strip()
                    usuario_nome = linhas_pl[i+1].split(":")[1].strip()
                    itens_raw = linhas_pl[i+2].split(":")[1].strip(" []")
                    item_nomes = [x.strip() for x in itens_raw.split(",") if x.strip()]

                    usuario_obj = next((u for u in usuarios if u.nome == usuario_nome), None)
                    if not usuario_obj:
                        registrar_erro(f"[Config] Playlist '{nome}' com usuário inexistente: {usuario_nome}")
                        i += 3
                        continue

                    playlist = Playlist(nome, usuario_obj, [], 0)
                    for item_nome in item_nomes:
                        midia = next((m for m in musicas if m.titulo == item_nome), None)
                        if not midia:
                            midia = next((p for p in podcasts if p.titulo == item_nome), None)
                        if midia:
                            playlist.adicionar_midia(midia)
                        else:
                            registrar_erro(f"[Config] Mídia inexistente '{item_nome}' na playlist '{nome}'")

                    playlists.append(playlist)
                except Exception as e:
                    registrar_erro(f"[Config] Erro ao carregar playlist: {e}")
                i += 3
            else:
                i += 1

        return musicas, usuarios, playlists, podcasts

    except Exception as e:
        registrar_erro(f"[Config] Erro ao carregar dados do arquivo Markdown: {e}")
        return [], [], [], []

