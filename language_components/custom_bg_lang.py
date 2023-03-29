import spacy
from spacy.lang.bg import Bulgarian

from spacy.lang.bg.stop_words import STOP_WORDS

from spacy.util import update_exc
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS

from spacy.lang.en.syntax_iterators import SYNTAX_ITERATORS
from spacy.language import Language
from spacy.tokens import Doc

from language_components.stop_words import BAN_STOP_WORDS
from language_components.token_exceptions import TOKENIZER_EXCEPTIONS 
from language_components.sentence_cleaner import is_invalid_ending, sentence_cleaner

# from stop_words import BAN_STOP_WORDS
# from token_exceptions import TOKENIZER_EXCEPTIONS 
# from sentence_cleaner import is_invalid_ending, sentence_cleaner

class CustomBulgarianDefaults(Bulgarian.Defaults):
    syntax_iterators = SYNTAX_ITERATORS
    stop_words = set.union(STOP_WORDS, BAN_STOP_WORDS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    
    
@spacy.registry.languages("custom_bg")
class CustomBulgarian(Bulgarian):
    lang = "custom_bg"
    Defaults = CustomBulgarianDefaults
    
from spacy.util import registry

@registry.callbacks("add_custom_components")
def make_add_custom_components():
    def add_custom_components(nlp):
        default_punct_chars = ['!', '.', '?','\n','\r']
        config_sentencizer = {"punct_chars": default_punct_chars}
        custom_bg_stopwords = nlp.Defaults.stop_words
        # Converting set to dictionary
        stop_words_dict = { }
        for stop_word in custom_bg_stopwords:
            stop_words_dict[stop_word] = [nlp(stop_word)[0].pos_]
        nlp.add_pipe("sentencizer", before='parser', config=config_sentencizer)
        nlp.add_pipe("sentence_cleaner", after='sentencizer')
    return add_custom_components