import unittest
from mes import Mes
from calendario import Ano


class TestMes(unittest.TestCase):
    def setUp(self):
        self.mes = Mes(2023, 1)

    def test_fevereiro_numero_dias(self):
        feb = Mes(2023, 2)
        self.assertEqual(max(max(feb.calendario)), 28)

    def test_fevereiro_bissexto(self):
        feb = Mes(2024, 2)
        self.assertEqual(max(max(feb.calendario)), 29)

    def test_add_evento(self):
        self.mes.add_evento(12, "Evento teste")
        self.assertIn("Evento teste", self.mes.get_evento(12))
        self.assertEqual(self.mes.count, 1)

    def test_add_2_eventos(self):
        self.mes.add_evento(12, "Evento 1")
        self.mes.add_evento(12, "Evento 2")
        self.assertIn("Evento 1", self.mes.get_evento(12))
        self.assertIn("Evento 2", self.mes.get_evento(12))
        self.assertEqual(self.mes.count, 2)

    def test_remove_evento(self):
        self.mes.add_evento(12, "Evento 1")
        self.mes.remove_eventos(12)
        self.assertEqual(self.mes.count, 0)

    def test_remove_todos_eventos(self):
        self.mes.add_evento(1, "Evento 1")
        self.mes.add_evento(2, "Evento 2")
        self.mes.clear_eventos()
        self.assertEqual(self.mes.count, 0)


class TestCalendario(unittest.TestCase):
    def setUp(self):
        self.ano = Ano(2023)

    def test_12_meses_no_ano(self):
        self.assertEqual(len(self.ano.calendario), 12)

    def test_add_evento(self):
        self.ano.add_evento(dia=12, mes=3, evento_str="Evento teste")
        self.assertIn("Evento teste", self.ano.get_evento(12, 3))
        self.assertEqual(self.ano.count, 1)

    def test_add_2_eventos(self):
        self.ano.add_evento(dia=12, mes=3, evento_str="Evento 1")
        self.ano.add_evento(dia=2, mes=9, evento_str="Evento 2")
        self.assertEqual(self.ano.count, 2)

    def test_remove_evento(self):
        self.ano.add_evento(2, 3, "Evento")
        self.ano.remove_evento(2, 3)
        self.assertNotIn("Evento", self.ano.get_evento(2, 3))
        self.assertEqual(self.ano.count, 0)

    def test_clear_todos_eventos(self):
        self.ano.add_evento(1, 1, "Evento 1")
        self.ano.add_evento(31, 12, "Evento 2")
        self.ano.clear_eventos()
        self.assertNotIn("Evento 1", self.ano.get_evento(1, 1))
        self.assertNotIn("Evento 2", self.ano.get_evento(31, 12))
        self.assertEqual(self.ano.count, 0)


if __name__ == "__main__":
    unittest.main()
