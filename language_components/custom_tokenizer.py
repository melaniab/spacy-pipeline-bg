import re
from spacy.tokenizer import Tokenizer 
from language_components.token_exceptions import TOKENIZER_EXCEPTIONS

prefix_re = re.compile(r'''^[\[\("'“„]''')
suffix_re = re.compile(r'''[\]\)"'\.\?\!,:%$€“„]$''')
infix_re = re.compile(r'''[~]''')
simple_url_re = re.compile(r'''^https?://''')

def custom_tokenizer(nlp):
    return Tokenizer(nlp.vocab, 
                     rules=TOKENIZER_EXCEPTIONS,
                     prefix_search=prefix_re.search,
                     suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer,
                    url_match=simple_url_re.match, 
                     )