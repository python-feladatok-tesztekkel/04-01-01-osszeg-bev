from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import osszeg

class TestOsszeg(TestCase):

    def test_02vasarlas_feladat(self):
        aktualis = osszeg.vasarlas_feladat()
        elvart = 9670
        self.assertEqual(elvart, aktualis, "A vásárolt termékek árát helytelenül határozta meg!")