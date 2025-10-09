while True:
    acao = menu_usuario(usuario.nome)

    if acao == "1":
        # Listar músicas
        print("\n--- Músicas Disponíveis ---")
        for m in musicas:
            print(m)

    elif acao == "2":
        # Reproduzir música
        titulo = input("Digite o título da música: ")
        musica = next((m for m in musicas if m.titulo == titulo), None)
        if musica:
            usuario.ouvir_midia(musica)
            print(musica.reproduzir())
        else:
            print("Música não encontrada.")

    elif acao == "3":
        # Listar playlists do usuário
        print("\n--- Suas Playlists ---")
        if usuario.playlists:
            for nome, playlist in usuario.playlists.items():
                print(playlist)
        else:
            print("Você ainda não criou playlists.")

    elif acao == "4":
        # Reproduzir playlist
        nome_playlist = input("Nome da playlist: ")
        playlist = usuario.playlists.get(nome_playlist)
        if playlist:
            playlist.reproduzir()
            print(f"Reproduzindo playlist '{nome_playlist}'")
        else:
            print("Playlist não encontrada.")

    elif acao == "5":
        # Criar nova playlist
        nome_playlist = input("Nome da nova playlist: ")
        if nome_playlist in usuario.playlists:
            print("Você já tem uma playlist com esse nome.")
        else:
            from Streaming.playlist import Playlist
            nova_playlist = Playlist(nome_playlist, usuario, [], 0)
            usuario.playlists[nome_playlist] = nova_playlist
            print("Playlist criada com sucesso.")

    elif acao == "6":
        # Concatenar playlists
        nome1 = input("Nome da primeira playlist: ")
        nome2 = input("Nome da segunda playlist: ")
        p1 = usuario.playlists.get(nome1)
        p2 = usuario.playlists.get(nome2)
        if p1 and p2:
            nova = p1 + p2
            novo_nome = input("Nome da playlist concatenada: ")
            nova.nome = novo_nome
            usuario.playlists[novo_nome] = nova
            print(f"Playlists concatenadas com sucesso como '{novo_nome}'")
        else:
            print("Uma ou ambas as playlists não foram encontradas.")

    elif acao == "7":
        # Gerar relatório simples
        from Streaming.analises import Analises

        print("\n=== RELATÓRIO ===")
        print(f"Total de reproduções: {Analises.total_reproducoes([usuario])}")
        print(f"Usuário mais ativo: {Analises.usuario_mais_ativo([usuario])}")
        top_musicas = Analises.top_musicas_reproduzidas(musicas, 3)
        print("Top 3 músicas:")
        for m in top_musicas:
            print(f"{m.titulo} ({m.reproducoes} reproduções)")

        # Salvando o relatório
        with open("relatorios/relatorio.txt", "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO ===\n")
            f.write(f"Usuário: {usuario.nome}\n")
            f.write(f"Total de reproduções: {Analises.total_reproducoes([usuario])}\n")
            f.write("Top músicas:\n")
            for m in top_musicas:
                f.write(f"- {m.titulo} ({m.reproducoes} reproduções)\n")
        print("Relatório salvo em relatorios/relatorio.txt")

    elif acao == "8":
        print("Voltando ao menu principal...")
        break

    else:
        print("Opção inválida. Tente novamente.")
