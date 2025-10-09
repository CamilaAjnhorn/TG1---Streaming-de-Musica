from .usuario import Usuario
from .analises import Analises
from .arquivo_de_midia import ArquivoDeMidia
from .musica import Musica
from .playlist import Playlist
from .podcast import Podcast
from .utils import *
from .relatorio import gerar_relatorio

class Menu:    
    def __init__(self):
        try:
            self.musicas, self.usuarios, self.playlists, self.podcasts = carregar_dados_md()
            self.usuario_atual = None
            print("Dados carregados com sucesso!")
        except Exception as e:
            registrar_erro(f"[Menu] Erro ao inicializar Menu: {e}")

    # menu principal
    def exibir_menu_principal (self):
        print(" === MENU PRINCIPAL ===")
        print("1 - Entrar como usuário")
        print("2 - Criar novo usuário")
        print("3 - Listar usuários")
        print("0 - Sair")

    def menu_principal (self):
        while True:
            try:
                self.exibir_menu_principal()
                opcao = input("\nEscolha uma opção: ").strip()

                if opcao == "1":
                    self.entrar_usuario()
                elif opcao == "2":
                    self.criar_usuario()
                elif opcao == "3":
                    self.listar_usuarios()
                elif opcao == "0":
                    print("Encerrando sistema...")
                    break
                else:
                    print("Opção inválida, tente novamente...")
            
            except Exception as e:
                registrar_erro("[MenuPrincipal] Erro: {e}")

    # açoes do menu principal
    def entrar_usuario (self):
        try:
            nome = input("Digite o nome do usuário").strip()
            usuario = next((u for u in self.usuarios if u.nome.lower() == nome.lower()), None)

            if usuario:
                self.usuario_atual = usuario
                print("Usuario logado com sucesso!")
                self.menu_usuario()
            else:
                print("Usuário não encontrado")

        except Exception as e:
            registrar_erro("[Menu] Erro ao entrar como usuário")
            print("Erro ao entrar como usuário...")

    def criar_usuario (self):
        try:
            nome = input("Digite o nome do novo usuário: ").strip()

            if any(u.nome.lower() == nome.lower() for u in self.usuarios):
                print("Nome já registrado")
                return
            
            novo = Usuario(nome, {}, [])
            self.usuarios.append(novo)

            print("Usuário '{nome}' criado com sucesso!")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao criar usuário: {e}")

    def listar_usuarios (self):
        try:
            print("=== LISTA DE USUÁRIOS ===")

            if not self.usuarios:
                print("Nenhum usuário cadastrado")
            
            for u in self.usuarios:
                print(f"- {u.nome}")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao listar usuarios: {e}")

    # menu interno
    def exibir_menu_usuario(self):
        print(f"=== MENU DO USUÁRIO: {self.usuario_atual.nome} ===")
        print("1 - Reproduzir uma música")
        print("2 - Listar músicas")
        print("3 - Listar podcasts")
        print("4 - Listar playlists")
        print("5 - Reproduzir uma playlist")
        print("6 - Criar nova playlist")
        print("7 - Concatenar playlists")
        print("8 - Gerar relatório")
        print("0 - Sair do usuário")

    def menu_usuario (self):
        while True:
            try:
                self.exibir_menu_usuario()
                opcao = input("Escolha uma opção:").strip()

                if opcao == "1":
                    self.reproduzir_musica()
                elif opcao == "2":
                    self.listar_musicas()
                elif opcao == "3":
                    self.listar_podcasts()
                elif opcao == "4":
                    self.listar_playlists()
                elif opcao == "5":
                    self.reproduzir_playlist()
                elif opcao == "6":
                    self.criar_playlist()
                elif opcao == "7":
                    self.concatenar_playlists()
                elif opcao == "8":
                    self.gerar_relatorio_sistema()
                elif opcao == "0":
                    print(f"Saindo do usuário {self.usuario_atual.nome}...")
                    self.usuario_atual = None
                    break
                else:
                    print("Opção inválida, tente novamente...")
                
            except Exception as e:
                registrar_erro(f"[MenuUsuario] Erro: {e}")
                print("Ocorreu um erro")

    # funcionalidades internas
    def reproduzir_musica(self):
        try:
            titulo = input("Informe o nome da música: ").strip()
            musica = next((m for m in self.musicas if m.titulo.lower() == titulo.lower()))

            if musica:
                print("Reproduzindo...\n")
                print(musica.reproduzir())
                self.usuario_atual.historico.append(musica)
            else:
                print("Musica não encontrada...")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao reproduzir música: {e}")
            print("Erro ao reproduzir música")

    def listar_musicas (self):
        try:
            print("=== MÚSICAS DISPONÍVEIS ===")

            for m in self.musicas:
                print(f"- {m.titulo} | {m.artista} | {m.genero} | {m.duracao}s")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao listar músicas: {e}")
            print("Erro ao listar músicas...")

    def listar_podcasts (self):
        try:
            print("=== PODCASTS DISPONÍVEIS ===")

            for p in self.podcasts:
                print(f"- {p.titulo} | {p.temporada} | Episódio {p.episodio} | Host: {p.host}")
        
        except Exception as e:
            registrar_erro(f"[Menu] Erro ao listar podcasts: {e}")
            print("Erro ao listar podcasts")

    def listar_playlists (self):
        try:
            print("=== PLAYLISTS DISPONÍVEIS ===")

            for p in self.playlists:
                print(f"- {p.nome} | Usuário: {p.usuario.nome} | {len(p.itens)} itens | {p.reproducoes} reproduções")
        
        except Exception as e:
            registrar_erro(f"[Menu] Erro ao listar playlists: {e}")
            print("Erro ao listar playlists")

    def reproduzir_playlist(self):
        try:
            nome = input("Digite o nome da playlist: ").strip()
            playlist = next((p for p in self.playlists if p.nome.lower() == nome.lower()))

            if playlist:
                print(f"Reproduzindo playlist '{playlist.nome}'")
                playlist.reproduzir()
                playlist.reproducoes += 1
                self.usuario_atual.historico.append(playlist)

            else:
                print("Playlist não encontrada...")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao reproduzir playlist: {e}")
            print("Erro ao reproduzir playlist")

    def criar_playlist (self):
        try:
            nome = input("Informe o nome da nova playlist:").strip()

            if any(p.nome.lower() == nome.lower() and p.usuario == self.usuario_atual for p in self.playlists):
                print("Voce já possui uma playlist com esse nome")
                return

            nova = Playlist(nome, self.usuario_atual, [], 0)

            while True:
                titulo = input("Adicione o nome de uma música ou 'fim' para encerrar:").strip()

                if titulo.lower() == "fim":
                    break

                musica = next((m for m in self.musicas if m.titulo.lower() == titulo.lower()), None)
                if musica:
                    nova.adicionar_midia(musica)
                else:
                    print("Música não encontrada")

            self.playlists.append(nova)
            print(f"Playlist '{nome}' criada com sucesso!")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao criar playlist: {e}")
            print("Erro ao criar playlist")

    def concatenar_playlists (self):
        try:
            nome1 = input("Informe o nome da primeira playlist: ").strip()
            nome2 = input("Informe o nome da segunda playlist: ").strip()

            p1 = next((p for p in self.playlists if p.nome.lower() == nome1.lower()), None)
            p2 = next((p for p in self.playlists if p.nome.lower() == nome2.lower()), None)

            if not p1 or not p2:
                print("Uma ou ambas as playlists não foram encontradas")
                return
            
            nova = p1 + p2
            nova.nome = f"{p1.nome}_{p2.nome}_Mix"
            self.playlists.append(nova)
            print(f"Nova playlist criada com sucesso!")

        except Exception as e:
            registrar_erro(f"[Menu] Erro ao concatenar playlists: {e}")

    def gerar_relatorio_sistema (self):
        try:
            gerar_relatorio(self.musicas, self.playlists, self.usuarios, self.podcasts)
            print("Relatorio gerado com sucesso!")
        
        except Exception as e:
            registrar_erro(f"[Menu] Erro ao gerar relatorio: {e}")
            print("Erro ao gerar relatorio...")