from unittest import TestCase

from osszeg import vasarlas_feladat

class TestOsszeg(TestCase):

    def test_vasarlas_feladat(self):
        aktualis = vasarlas_feladat()
        elvart = 9670
        self.assertEqual(elvart, aktualis, "A vásárolt termékek árát helytelenül határozta meg!")