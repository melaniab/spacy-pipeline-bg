# Bulgarian spaCy natural language processing pipeline

Paper: [An Improved Bulgarian Natural Language Processing Pipeline](https://www.researchgate.net/profile/Melania-Berbatova/publication/371081880_An_Improved_Bulgarian_Natural_Language_Processing_Pipeline/links/64787b68b3dfd73b7758815e/An-Improved-Bulgarian-Natural-Language-Processing-Pipeline.pdf), 
proceedings of [International Conference on Information Systems, Embedded Systems and Intelligent Applications (ISЕSIA) 2023](https://isesia.fmi.uni-sofia.bg/).


# Usage 
First, the pretrained models need to be downloaded into the repo folder from [Google Drive](https://drive.google.com/file/d/1xX3ZIX7-_T-_xV2gsZwotOAfZBlWLZ3L/view?usp=sharing). 

In order to use the pipeline, it should be installed as a local Python package:

```shell
python -m spacy package ./models_v3.3/model-best/ packages --name bg --version 1.0.0 --code language_components/custom_bg_lang.py
pip install packages/bg_bg-1.0.0/dist/bg_bg-1.0.0.tar.gz

```
You can check if the pipeline was correctly installed with the `pip list` command. 
 
After a successful installation, the pipeline can be opened in a Python file as a spaCy language model. The tokenizer needs to be added manually. 
```python
import spacy
nlp = spacy.load("bg_bg")
from language_components.custom_tokenizer import *
nlp.tokenizer = custom_tokenizer(nlp)
```
For more details on how to use the pipeline, please take a look at the [Model loading and usage notebook](https://github.com/melaniab/spacy-pipeline-bg/blob/master/Model_loading_and_usage.ipynb) and [the official spaCy documentation](https://spacy.io/usage/models). 


# Project structure and details 

## Pipeline components 

The pipeline consists of the following steps:
- Tokenization
- Sentence Splitting
- Lemmatization
- Part-of-speech Tagging
- Dependency Parsing 
- Word Sense Disambiguation (available upon request)

## Pretrained vectors

Pretrained fastText vectors for Bulgarian language can be downloaded from [the fasttext website](https://fasttext.cc/docs/en/crawl-vectors.html) and put into the `vectors/` folder.



## Spacy project structure

After downloading the pretrained word vectors and the pretrained models, the project should consists of the following folders: 
- `configs/` - configuration files,
- `corpus/` - train/dev/test dataset in .spacy format,
- `language_components/` - files for the custom language components (tokenizer, sentencizer, and connected files), 
- `models_v3.3/` - trained pipeline models in spaCy 3.3, 
- `models_v3.4/` - trained pipeline models in spaCy 3.4,
- `tests/` - unittests for the custom components, 
- `vectors/` - pretrained word embeddings (fastText), 
- `visualiations/` - dependency parsing visualizations on the test set.

## Tokenization 
Tokenization is the first step of the pipeline. The Bulgarian tokenizer consists of custom rules, exceptions and stopwords. It can be used separately from the rest of the pipeline. 

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
In the file `language_components/stopwords.py`. Stopwords are taken from [the BulTreeBank website](http://bultreebank.org/bg/resources/). 

## Other components 
Please refer to [the paper](https://www.researchgate.net/publication/371081880_An_Improved_Bulgarian_Natural_Language_Processing_Pipeline) for details about the rest of the components in the pipeline. 

# Reference 

If you use the pipeline in your academic project, please cite as: 

```bibtex
@article{berbatova2023improved,
  title={An Improved Bulgarian Natural Language Processing Pipeline},
  author={Berbatova, Melania and Ivanov, Filip},
  year={2023}
}
```
MIT License       
Copyright (c) 2023 Melania Berbatova
