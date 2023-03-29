# Bulgarian spaCy natural language processing pipeline

## Pipeline components 

The pipeline consists of the following steps:
- Tokenization
- Sentence Splitting
- Lemmatization
- Part-of-speech Tagging
- Dependency Parsing 
- Word Sense Disambiguation 


## Spacy project structure
 

The project consists of the following folders: 
- `configs/` - configuration files,
- `corpus/` - train/dev/test dataset in .spacy format,
- `language_components/` - files for the custom language components (tokenizer, sentencizer, and connected files), 
- `metrics/` - evaluation metrics on the test set (with timestamp),
- `models/` - trained pipeline models, 
- `packages/` - packaged pipeline models,
- `tests/` - unittests for the custom components, 
- `vectors/` - pretrained word embeddings (fasttext), 
- `visualiations/` - dependency parsing visualizations on the test set.


## Tokenization 
Tokeninzation is the first step of the pipeline.  

### Rules 
The rules for the rule-based tokenizer are in the file language_components/custom_tokenizer.py. They are defined by the following regular exceptions: 

```python
prefix_re = re.compile(r'''^[\[\("'“„]''')
suffix_re = re.compile(r'''[\]\)"'\.\?\!,:%$€“„]$''')
infix_re = re.compile(r'''[~]''')
simple_url_re = re.compile(r'''^https?://''')
```

### Exceptions

Tokenizer exceptions are in the file  `language_components/token_exceptions.py.`
They are grouped in the following variables: 
- `METRICS_NO_DOT_EXC` - units of measure
- `DASH_ABBR_EXC` - abbreviations with an inner dash
- `DASH_ABBR_TITLE_EXC` - Abbreviations with an inner dash, capitalized
- `ABBR_DOT_MIDDLE_EXC` - abbreviations with a dot that cannot be at the end of the sentence
- `ABBR_DOT_MIDDLE_TITLE_EXC` - the same with a capital letter
- `ABBR_DOT_END_EXC` - abbreviations with a dot that may be at the end of the sentence
- `ABBR_UPPERCASE_EXC` - Uppercase abbreviations 

### Stopwords 
In the file `language_components/stopwords.py.` Stopwords are taken from here: http://bultreebank.org/bg/resources/. 