from .arquivo_de_midia import *
from.analises import Analises
from .utils import registrar_erro

class Musica(ArquivoDeMidia):
    #inicia as instancias da classe musica
    def __init__(self, titulo, duracao, artista, 
                 genero:str, avaliacoes:list[int]):
        super().__init__(titulo, duracao, artista)
        try:
            self.genero = genero
            self._avaliacoes = list(avaliacoes) if avaliacoes else []
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao inicializar '{titulo}': {e}")
            self._avaliacoes = []

    #getter e setter de genero
    @property
    def genero (self):
        return self.genero
    #garante que o genero é um dos permitidos
    @genero.setter
    def genero (self, value):
        try:
            permitidos = ["Rock", "Pop", "Rap", "Classico"]
            if value in permitidos:
                self.genero = value
            else:
                raise ValueError(f"Gênero inválido: {value}")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao definir gênero para '{self.titulo}': {e}")
            self.genero = "Desconhecido"

    def avaliar (self, nota:int):
        try:
            nota = int(nota)
            
            if 0 <= nota <= 5:
                self._avaliacoes.append(nota)
            else:
                raise ValueError("Nota fora do intervalo permitido")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao avaliar '{self.titulo}': {e}")
        
        
        self._avaliacoes.append(nota)

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
        
    def __eq__ (self, other):
        try:
            if isinstance(other, Musica):
                if (self.titulo == other.titulo 
                    and 
                    self.artista == other.artista):
                    return True
                else:
                    return False
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao comparar músicas: {e}")
            return f"Erro ao comparar musicas"
        
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
            return (f"titulo = {self.titulo} | duração = {self.duracao}"
                    f"| artista = {self.artista} | genero = {self.genero}"
                    f"avaliações = {self._avaliacoes}")
        except Exception as e:
            registrar_erro(f"[Musica] Erro ao gerar __repr__: {e}")
            return f"Musica(informações indisponíveis)"