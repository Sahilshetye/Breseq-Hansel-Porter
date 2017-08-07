import unittest
import Hansel_HTMLscrapper.Evidence as Ev

class EvidenceTestCase(unittest.TestCase):
    def test_EvidenceType(self):
        self.assertNotEqual(str,type(Ev.getEvidenceDetailsfromSoup("RA","Not important")))

    def test_Evidence1(self):
        self.assertEqual(2, Ev.getEvidenceDetailsfromSoup("RA","Not important"))

    def test_Evidence2(self):
        self.assertEqual(0, Ev.getEvidenceDetailsfromSoup("RAR","Not important"))

    def test_Evidence3(self):
        self.assertNotEqual(0,Ev.getEvidenceDetailsfromSoup("RA","Not important"))

if __name__ == '__main__':
    unittest.main()
