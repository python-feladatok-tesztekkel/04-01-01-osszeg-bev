from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import osszeg

class TestOsszeg(TestCase):

    def test_04almaszedes_feladat(self):
        aktualis = osszeg.almaszedes_feladat()
        elvart = 78.9
        self.assertEqual(elvart, aktualis, "A szedett alma mennyiséget helytelenül határozta meg!")
