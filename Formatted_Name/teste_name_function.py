#caso de teste para verificar se a função get_formated_name está correta, quando recebe um primeiro nome e sobrenome

#importe o modulo de teste de unidade

import unittest

#importe o arquivo e o nome da função
from name_function import get_fomarted_name

#criando uma classe que terá testes de unidades para get_formated_name
class NameTestCase(unittest.TestCase):
    """Testes para name_function.py"""

def test_first_last_name(self):
    """Names como 'janis joplin' funcionam?"""
    formated_name = get_fomarted_name('janis', 'joplin')
    #compare o valor em formated_name com a string 'janis joplin' se forem iguais
    #oka, senão me avise
    self.asserEqual(formated_name, 'janis joplin')
    unittest.main()