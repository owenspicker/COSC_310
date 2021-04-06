import unittest
import pos_tag_functions
import polarity


#this file is to test the functions created in Assignment 3
#the inputs span from general cases to edge cases

class TestChatBot(unittest.TestCase):
  
    
    #this first function tests the polarity function (sentiment analysis)
    def test_checkPolarity(self):
          self.assertEqual(polarity.checkPolarity("I hate you"), True)
          self.assertEqual(polarity.checkPolarity("Soccer is terrible"), True)
          self.assertEqual(polarity.checkPolarity("I love you"), False)
          self.assertEqual(polarity.checkPolarity("Curling is boring"), True)
          self.assertEqual(polarity.checkPolarity("You couldn't beat me"), False)
          self.assertEqual(polarity.checkPolarity("Crosby is bad at hockey"), True)
          self.assertEqual(polarity.checkPolarity("Messi is a great guy"), False)
          self.assertEqual(polarity.checkPolarity("Hi how are you?"), False)
          self.assertEqual(polarity.checkPolarity("No you could not"), False) 
          
          
     #this function tests the check for currency (pos tagging)     
    def test_checkForCurrency(self):
          self.assertEqual(pos_tag_functions.checkForCurrency("Can I go to a game for $100?"), True)
          self.assertEqual(pos_tag_functions.checkForCurrency("£100"), False) 
          self.assertEqual(pos_tag_functions.checkForCurrency("one hundred dollars"), False)
          self.assertEqual(pos_tag_functions.checkForCurrency("is messi worth $100 mil?"), True)

    #this function tests the check for year (pos tagging)
    def test_checkForNum(self):
          self.assertEqual(pos_tag_functions.checkForNum("Who won in 1900?"), True)
          self.assertEqual(pos_tag_functions.checkForNum("Who won in 2000?"), True)
          self.assertEqual(pos_tag_functions.checkForNum("Who won in 3000?"), False)
          self.assertEqual(pos_tag_functions.checkForNum("Who won in 19000?"), False)
          self.assertEqual(pos_tag_functions.checkForNum("Who won in 190?"), False)

    
    
if __name__ == '__main__':
     unittest.main()
  
    
  
      
