from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import osszeg

class TestOsszeg(TestCase):
    def test_01bevetel_feladat(self):
        aktualis = osszeg.bevetel_feladat()
        elvart = 958
        self.assertEqual(elvart, aktualis, "A cég első féléves bevételét helytelenül határozta meg!")

