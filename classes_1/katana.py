class katana:
    def __init__(self, mat_same, mat_saya, cor_saya, cor_sama, cortando=False, afiada=False):
        self.mat_same = mat_same
        self.mat_saya = mat_saya
        self.cor_saya = cor_saya
        self.cor_sama = cor_sama
        self.cortando = cortando
        self.afiada = afiada

    def get_mat_same(self):
        """
        método que retorna o material da same(cobertura do cabo).
        :return: mat_same
        """
        return self.mat_same


    @classmethod
    def documentacao(cls):
        try:
            open('c:\\users\\clari\\desktop\\katana.txt', 'x').write('Classe que indica o objeto katana.'
                                                                 '\n Essa classe cria um objeto que tem'
                                                                 ' o material da same (cobertura do cabo) '
                                                                 ', o material da saya (bainha) e a cor '
                                                                 'desses dois itens.')
        except FileExistsError:
            print('O arquivo já existe.')
            open('c:\\users\\clari\\desktop\\katana.txt', 'w').write('Classe que indica o objeto katana.'
                                                                     '\n Essa classe cria um objeto que tem'
                                                                     ' o material da same (cobertura do cabo) '
                                                                     ', o material da saya (bainha) e a cor '
                                                                     'desses dois itens.')
        finally:
            open('c:\\users\\clari\\desktop\\katana.txt').close()
            print('arquivo de documentação criado')

    @staticmethod
    def fatorial(numero):
        x = cont = numero
        fat = 0
        while cont > 1:
            cont -= 1
            fat = x * (cont)
            x = fat
        return fat


if __name__ == '__main__':  # ← se estiver executando dentro do próprio módulo.
    espada = katana('arraia', 'osso', 'branco', 'cinza')  # ← instanciando uma classe
    print(espada.get_mat_same())  # ← executando um método daquela classe
    espada.mat_same = 'javali'
    print(espada.get_mat_same())
    print(espada.cortando)
    if espada.cortando:
        print('A katana está cortando algo')
    else:
        print('A katana está em repouso')
    katana.documentacao()
    print(katana.fatorial(6))  # ← executando o static method a partir da classe, sem precisar de objeto
    print(espada.fatorial(5)) # ← executando o static method a partir da instância da classe.

