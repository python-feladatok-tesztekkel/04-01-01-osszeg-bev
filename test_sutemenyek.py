from unittest import TestCase

from osszeg import sutes_feladat


class TestOsszeg(TestCase):

    def test_sutemenyek_feladat(self):
        aktualis = sutes_feladat()
        elvart = 1.56
        self.assertEqual(elvart, aktualis, "A szükséges cukormennyiséget helytelenül határozta meg!")

