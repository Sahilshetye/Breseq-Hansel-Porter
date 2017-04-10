import unittest
import Hansel_HTMLscrapper.Gene as g
class GeneCodetest1(unittest.TestCase):
    def test_type(self):
        self.assertEqual(str, type(g.getGeneDetailsfromSoup(u"CAETHG_0085 \u2190  / \u2190 CAETHG_0086")))


    def test_type1(self):
        self.assertEqual(str,type(g.getGeneDetailsfromSoup(123)))

    def test_type2(self):
        self.assertEqual(str,type(g.getGeneDetailsfromSoup("whoaa")))


if __name__ == '__main__':
    unittest.main()
