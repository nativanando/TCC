"""
apple.py: Classe responsável por realizar a coleta das ações da apple.
"""
from seriestemporais.stack_empresas.crawler import *
from seriestemporais.stack_empresas.empresa import *

__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "0.0.1"

class Apple(Empresa):

    def __init__(self):
        self.nome_empresa = 'apple'
        self.codigo = 'AAPL'
        self.executa_busca()

    def executa_busca(self):                                    # OVERRIDE
        crawler = Crawler(self.nome_empresa, self.codigo)
        crawler.executa_busca()
