from model_mommy import mommy
from django.test import TestCase

class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class RecursoTestCase(TestCase):

    def setUp(self):
        self.recurso = mommy.make('Recurso')

    def test_str(self):
        self.assertEquals(str(self.recurso), self.recurso.nome)

class ClienteTestCase(TestCase):

    def setUp(self):
        self.cliente = mommy.make('Cliente')

    def test_str(self):
        self.assertEquals(str(self.cliente), self.cliente.nome)