from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import osszeg


class TestOsszeg(TestCase):

    def test_03sutemenyek_feladat(self):
        aktualis = osszeg.sutes_feladat()
        elvart = 1.56
        self.assertEqual(elvart, aktualis, "A szükséges cukormennyiséget helytelenül határozta meg!")

