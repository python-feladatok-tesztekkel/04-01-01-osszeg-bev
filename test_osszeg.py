from unittest import TestCase

from osszeg import bevetel_feladat
from osszeg import vasarlas_feladat
from osszeg import sutes_feladat
from osszeg import almaszedes_feladat

class TestOsszeg(TestCase):
    def test_bevetel_feladat(self):
        aktualis = bevetel_feladat()
        elvart = 958
        self.assertEqual(elvart, aktualis, "A cég első féléves bevételét helytelenül határozta meg!")

    def test_vasarlas_feladat(self):
        aktualis = vasarlas_feladat()
        elvart = 9670
        self.assertEqual(elvart, aktualis, "A vásárolt termékek árát helytelenül határozta meg!")

    def test_sutemenyek_feladat(self):
        aktualis = sutes_feladat()
        elvart = 1.56
        self.assertEqual(elvart, aktualis, "A szükséges cukormennyiséget helytelenül határozta meg!")

    def test_almaszedes_feladat(self):
        aktualis = almaszedes_feladat()
        elvart = 78.9
        self.assertEqual(elvart, aktualis, "A szedett alma mennyiséget helytelenül határozta meg!")