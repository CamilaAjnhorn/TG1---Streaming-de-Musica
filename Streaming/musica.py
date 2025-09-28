from .arquivo_de_midia import *

class Musica(ArquivoDeMidia):
    #inicia as instancias da classe musica
    def __init__(self, titulo, duracao, artista, 
                 genero:str, avaliacoes:list[int]):
        super().__init__(titulo, duracao, artista)
        self.genero = genero
        self._avaliacoes = list(avaliacoes) if avaliacoes else []

    #getter e setter de genero
    @property
    def genero (self):
        return self.genero
    #garante que o genero é um dos permitidos
    @genero.setter
    def genero (self, value):
        permitidos = ["Rock", "Pop", "Rap", "Classico"]
        if value in permitidos:
            self.genero = value

    def avaliar (self, nota:int):
        nota = int(nota)
        self._avaliacoes.append(nota)

    def reproduzir(self):
        return (f"Música: {self.titulo}\n"
                f"Artista: {self.artista}\n"
                f"Duração: {self.duracao}\n"
                f"{len(self._avaliacoes)/sum(self._avaliacoes)} estrelas")
    
    def __eq__ (self, other):
        if isinstance(other, Musica):
            if (self.titulo == other.titulo 
                and 
                self.artista == other.artista):
                return True
            else:
                return False
    
    def __str__(self):
        return (f"Titulo: {self.titulo}\n"
                f"{self.duracao} min\n"
                f"Artista: {self.artista}\n"
                f"Genero: {self.genero}\n"
                f"Avaliação: {sum(self._avaliacoes)/len(self._avaliacoes)}")
    
    def __repr__(self):
        return (f"titulo = {self.titulo} | duração = {self.duracao}"
                f"| artista = {self.artista} | genero = {self.genero}"
                f"avaliações = {self._avaliacoes}")