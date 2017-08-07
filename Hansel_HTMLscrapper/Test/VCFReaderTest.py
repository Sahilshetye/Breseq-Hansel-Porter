import unittest
import Hansel_HTMLscrapper.VCFReader as vc

class VCReaderTest(unittest.TestCase):
    def test_VCFReader_REF(self):
        self.assertEqual("CT",vc.getREF('/data1/Test folder',306073,'LTMG3'))

    def test_VCFReader_ALT(self):
        self.assertEqual("C",vc.getALT('/data1/Test folder',306073,'LTMG3'))

    def test_VCFReadertype_ALT(self):
        self.assertEqual(str,type(vc.getALT('/data1/Test folder',306073,'LTMG3')))


    def test_VCFReadertype_REF(self):
        self.assertEqual(str,type(vc.getALT('/data1/Test folder',306073,'LTMG3')))

if __name__ == '__main__':
    unittest.main()
