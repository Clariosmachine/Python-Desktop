class livro():
    def __init__(self, autor, ano, tema):
        self.autor = autor
        self.ano = ano
        self.tema = tema

    def tit_autor(self):
        self.autor = self.autor.upper()

    def get_ano(self):
        return self.ano

    @property
    def ano(self):
        return self._ano + '_getter'

    @ano.setter
    def ano(self, atributo):
        if len(str(atributo)) < 4:
            self._ano = str(atributo)+'0'+'_setter'
        else:
            self._ano = str(atributo) + '_setter'


livro1 = livro('Arthur Conon Doyle', 180, 'Policial')
# ↑ 180 foi propositalmente para verificar os métodos getter e setter
livro1.tit_autor()
print(livro1.autor)
print(livro1.ano)
print(livro1.get_ano())