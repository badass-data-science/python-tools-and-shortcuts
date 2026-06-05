import nltk
from nltk.tokenize import word_tokenize

def calculate_part_of_speech_tags(text : str) -> list | None:

    # Download required datasets
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')

    # tokenize the text
    tokens = word_tokenize(text)

    # add POS tags
    tagged_text = nltk.pos_tag(tokens)

    # We only want the POS tags, not the original words
    list_pos_tags = [x[1] for x in tagged_text]

    return list_pos_tags
