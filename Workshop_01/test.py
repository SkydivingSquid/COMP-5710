import unittest
import source 
import math

class TestCalc(unittest.TestCase):

    #Tests that only numeric chars are being entered (including -, +, and .)
    def testValidityCheckOnLegalChars(self):
        self.assertEqual(True, source.validityCheck(1,-10.1), "Invalid check. Postive, negative, and decimal values should return True.")

    def testValidityCheckOnIllegalChars(self):
        self.assertEqual('Invalid Input. Please only enter numeric values.', source.validityCheck('abc',10), "Invalid check. Non-numeric char should return error message.")

    #Subtraction Tests
    def testSubtractionOnPositives(self):
        self.assertEqual(1, source.performSub(2, 1), "Invalid output. Result should be: 1")   

    def testSubtractionWithNegativePrimary(self):
        self.assertEqual(-3, source.performSub(-2, 1), "Invalid output. Result should be: -3")
    
    def testSubtractionWithNegativeSecondary(self):
        self.assertEqual(3, source.performSub(2, -1), "Invalid output. Result should be: 3")

    def testSubtractionOnFloat(self):
        self.assertEqual(2.5, source.performSub(5.5, 3), "Invalid output. Result should be: 2.5")    

    #Addition Tests
    def testAdditionOnPositive(self):
        self.assertEqual(3.1, source.performAdd(2, 1.1), "Invalid output. Result should be: 3.1")

    def testAdditionOnNegatives(self):
        self.assertEqual(-3.1, source.performAdd(-2, -1.1), "Invalid output. Result should be: 3.1")

    #Multiplication Tests
    def testMultiplyOnPositives(self):
        self.assertEqual(5, source.performMult(2.5, 2), "Invalid output. Result should be: 5")    

    def testMultiplyOnSingleNegative(self):
        self.assertEqual(-6, source.performMult(-2, 3), "Invalid output. Result should be: -6") 

    def testMultiplyOnTwoNegatives(self):
        self.assertEqual(6, source.performMult(-2, -3), "Invalid output. Result should be: 6") 

    #Division Tests
    def testDivisionOnPositives(self):
        self.assertEqual(2, source.performDiv(10.5, 5.25), "Invalid output. Result should be: 2")

    def testDivisionOnPNegatives(self):
        self.assertEqual(-2, source.performDiv(10.5, -5.25), "Invalid output. Result should be: -2")

    def testDivisionByZero(self):
        self.assertEqual('ILLEGAL OPERATION. Cannot divide by 0.', source.performDiv(10, 0), "Invalid output. Should return an error message.")

#Allows the program to run in Terminal
if __name__ == '__main__': 
    unittest.main() 