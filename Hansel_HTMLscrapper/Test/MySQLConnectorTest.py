import unittest
import Hansel_HTMLscrapper.MySqlConnector as ms

class MySQLConnectorClass(unittest.TestCase):
    def testAnnotationtypID(self):
        self.assertEqual(1, ms.getAnnotationType("intergenic"))

    def testAnnotationtypID2(self):
        self.assertEqual(4, ms.getAnnotationType("fault"))

    def testAnnotationtypID3(self):
        self.assertEqual(2, ms.getAnnotationType("coding"))


if __name__ == '__main__':
    unittest.main()
