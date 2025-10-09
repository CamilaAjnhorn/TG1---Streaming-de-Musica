from .arquivo_de_midia import *
from .analises import Analises
from .utils import registrar_erro

class Musica(ArquivoDeMidia):
    def __init__(self, titulo, duracao, artista, genero: str, avaliacoes: list[int] = None):
        super().__init__(titulo, duracao, artista)
        self._genero = "Desconhecido"  # atributo interno
        self.genero = genero            # usa o setter
        self._avaliacoes = list(avaliacoes) if avaliacoes else []

    # getter e setter de genero
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        try:
            permitidos = ["Rock", "Pop", "Rap", "Classico", "Desconhecido"]
            if not value or not value.strip():  # vazio ou None
                self._genero = "Desconhecido"
            elif value.strip() in permitidos:
                self._genero = value.strip()
            else:
                # aceita qualquer outro gênero do Markdown
                self._genero = value.strip()
                registrar_erro(f"[Musica] Aviso: Gênero '{self._genero}' não está na lista oficial.")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao definir gênero para '{self.titulo}': {e}")
            self._genero = "Desconhecido"

    def avaliar(self, nota: int):
        try:
            nota = int(nota)
            if 0 <= nota <= 5:
                self._avaliacoes.append(nota)
            else:
                raise ValueError("Nota fora do intervalo permitido")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao avaliar '{self.titulo}': {e}")

    def reproduzir(self):
        try:
            medias = Analises.media_avaliacoes([self])
            media = medias.get(self.titulo, 0)
            return (f"Música: {self.titulo}\n"
                    f"Artista: {self.artista}\n"
                    f"Duração: {self.duracao}\n"
                    f"{media} estrelas")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao reproduzir '{self.titulo}': {e}")
            return f"Erro ao reproduzir música '{self.titulo}'."

    def __eq__(self, other):
        try:
            return isinstance(other, Musica) and self.titulo == other.titulo and self.artista == other.artista
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao comparar músicas: {e}")
            return False

    def __str__(self):
        try:
            medias = Analises.media_avaliacoes([self])
            media = medias.get(self.titulo, 0)
            return (f"Titulo: {self.titulo}\n"
                    f"{self.duracao} min\n"
                    f"Artista: {self.artista}\n"
                    f"Genero: {self.genero}\n"
                    f"Avaliação: {media}")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao gerar __str__ de '{self.titulo}'")
            return f"[Erro ao exibir informações de '{self.titulo}']"

    def __repr__(self):
        try:
            return (f"titulo = {self.titulo} | duração = {self.duracao} | artista = {self.artista} "
                    f"| genero = {self.genero} | avaliações = {self._avaliacoes}")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao gerar __repr__: {e}")
            return f"Musica(informações indisponíveis)"
