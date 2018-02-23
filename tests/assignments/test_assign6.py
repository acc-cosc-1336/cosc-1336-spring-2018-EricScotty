import unittest
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string
#write the import for function get_count_A_C_G_and_T_in_string


class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''
        A,C,G,T = get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG')

        self.assertEqual(6,A)
        self.assertEqual(4,C)
        self.assertEqual(5,G)
        self.assertEqual(6,T)
        


    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''

        A,C,G,T = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

        self.assertEqual(20,A)
        self.assertEqual(12,C)
        self.assertEqual(17,G)
        self.assertEqual(21,T)

unittest.main(verbosity=2)
