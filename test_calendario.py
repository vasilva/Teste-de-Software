import unittest
from calendario import Mes
from calendario import Ano


class TestCalendario(unittest.TestCase):
    def test_12_meses_no_ano(self):
        cal = Ano(12)
        self.assertEqual(len(cal.calendario), 12)

    def test_fevereiro_numero_dias(self):
        feb = Mes(2023, 2)
        self.assertEqual(max(max(feb.calendario)), 28)

    def test_fevereiro_bissexto(self):
        feb = Mes(2024, 2)
        self.assertEqual(max(max(feb.calendario)), 29)

    def test_add_event(self):
        cal = Ano(2023)
        cal.add_evento(dia=12, mes=3, evento_str="Evento teste")
        self.assertEqual(cal.get_evento(12, 3), ["Evento teste"])
        self.assertEqual(cal.count, 1)
    
    def test_add_2_events(self):
        cal = Ano(2023)
        cal.add_evento(dia=12, mes=3, evento_str="Evento 1")
        cal.add_evento(dia=2, mes=9, evento_str="Evento 2")
        self.assertEqual(cal.count, 2)
    
    def test_clear_events(self):
        cal = Ano(2023)
        cal.add_evento(2, 3, "Evento")
        cal.remove_evento(2, 3)
        self.assertEqual(cal.count, 0)


if __name__ == "__main__":
    unittest.main()
