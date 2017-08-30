"""
intel.py: Classe responsável por realizar a coleta das ações da intel.
"""
from seriestemporais.stack_empresas.crawler import *
from seriestemporais.stack_empresas.empresa import *

__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "1.0"

class Intel(Empresa):

    def __init__(self):
        self.nome_empresa = 'intel'
        self.codigo = 'INTC'
        self.executa_busca()

    def executa_busca(self):                                    # OVERRIDE
        crawler = Crawler(self.nome_empresa, self.codigo)
        crawler.executa_busca()