# -*- coding: utf-8 -*-

import unittest
# import os
# os.chdir("../language_components/")
import sys
sys.path.append('../language_components/')
 
from custom_tokenizer import custom_tokenizer

def get_token_list(text): 
    doc = nlp(text)
    tokens = [t.text for t in doc]
    return tokens

from spacy.vocab import Vocab
from spacy.language import Language
nlp = Language(Vocab())
nlp.tokenizer = custom_tokenizer(nlp)

class TestCustonTokenizer(unittest.TestCase):
      
    def test_duplicates(self): 
        pass 
    #Test punctuation
#     def test_punctuation(self):        
#         self.assertEqual(get_token_list("    Честита      нова       година  !   "), ['Честита', 'нова', 'година', '!'])
  
    # Test whitespaces
    def test_whitespaces(self):
        self.assertEqual(get_token_list("Честита нова година!"), ['Честита', 'нова', 'година', '!'])
        
    # Test infixes
    def test_infixes(self):
        self.assertEqual(get_token_list("За едни по-добра, за други по-лоша."), ['За', 'едни', 'по-добра', ',', 'за', 'други', 'по-лоша', '.'])
  
    # Test dates 
    def test_dates(self):        
        self.assertEqual(get_token_list("24.04.1939 г."), ['24.04.1939', 'г.'])
        self.assertEqual(get_token_list("60-те години."), ['60-те', 'години', '.'])
  
    # Test exceptions 
    def test_exceptions(self):        
        self.assertEqual(get_token_list("Св. св. Кирил и Методий"), ['Св.', 'св.', 'Кирил', 'и', 'Методий'])
        
    # Test line abbr     
    def test_exceptions(self):        
        self.assertEqual(get_token_list("П-в Пелопонес"), ['П-в', 'Пелопонес'])

if __name__ == '__main__':
    unittest.main()