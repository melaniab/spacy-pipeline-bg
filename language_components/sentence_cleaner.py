from spacy.language import Language
import string
from language_components.token_exceptions import ABBR_DOT_END_EXC


def is_invalid_ending(token_text):
    """
    Marks innitials (such as "A.") as invalid end of sentence. 
    """
    if len(token_text) == 1 and token_text[0].isupper() and token_text not in ['!', '.', '?']: 
        return True
    else:
        return False

@Language.component("sentence_cleaner")
def sentence_cleaner(doc):
    default_punct_chars = ['!', '.', '?', '\n','\r']
    prev_is_invalid_ending = False;
    
    for sent in doc.sents:
        prev_token_ends_with_punct = False;
        
        idx = 0
        
        for token in sent:
            idx += 1
            token_text = token.text.strip()   
            
            # A sentence cannot start with an empty token.   
            if len(token_text) == 0:
                token.is_sent_start = False
                continue
                
            # A sentence cannot start with a lowercase letter.
            if token_text[0].islower():
                token.is_sent_start = False
            
            prev_token = sent[idx-2]          
            prev_is_exception = sent[idx-2].norm_.endswith('.') or sent[idx-2].norm_ != sent[idx-2].text # Marks if the previous token is an exception 

            possible_exception_endings = ABBR_DOT_END_EXC # Tokenizer exceptions ending with dot, that can be at the end of a sentence. 
            
            
            should_be_start = token_text[0].isupper() and \
                              prev_is_invalid_ending == False and \
                            (prev_token.text in default_punct_chars or \
                             (prev_is_exception == False and prev_token.text.endswith('.')) \
                                                                    or (prev_is_exception == True and prev_token.text in possible_exception_endings)) 
            
            
            if should_be_start and token.is_sent_start == False:
                token.is_sent_start = True
                
            if token_text[len(token_text) -1] in default_punct_chars:
                prev_token_ends_with_punct = True;
            else: 
                prev_token_ends_with_punct = False;
                
#             prev_is_invalid_ending = is_invalid_ending(token_text)
            prev_is_invalid_ending = is_invalid_ending(prev_token.text)
            
    return doc