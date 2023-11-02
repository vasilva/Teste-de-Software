import unittest
from lembrete import Calendario

class TestCalendario(unittest.TestCase):
    def test_event(self):
        cal = Calendario(2023, 2)
        cal.add_evento(12, "Evento")
        self.assertEqual(cal.get_evento(12), ['Evento'])

if __name__ == "__main__":
    unittest.main()