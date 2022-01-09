from unittest import TestCase

from osszeg import almaszedes_feladat

class TestOsszeg(TestCase):

    def test_almaszedes_feladat(self):
        aktualis = almaszedes_feladat()
        elvart = 78.9
        self.assertEqual(elvart, aktualis, "A szedett alma mennyiséget helytelenül határozta meg!")