from unittest import TestCase

from osszeg import bevetel_feladat

class TestOsszeg(TestCase):
    def test_bevetel_feladat(self):
        aktualis = bevetel_feladat()
        elvart = 958
        self.assertEqual(elvart, aktualis, "A cég első féléves bevételét helytelenül határozta meg!")

