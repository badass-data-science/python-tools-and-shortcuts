# nlp

Natural language processing utilities built on [NLTK](https://www.nltk.org/).

## `calculate_part_of_speech_tags`

Tokenizes a string and returns a list of Penn Treebank part-of-speech tags for each token.

```python
calculate_part_of_speech_tags(text: str) -> list | None
```

Downloads the required NLTK datasets (`punkt_tab`, `averaged_perceptron_tagger_eng`) automatically on first use.

Returns a list of POS tag strings (e.g. `['NNP', 'VBZ', 'DT', 'NN']`), or `None` on failure. Tags follow the [Penn Treebank tagset](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).

### Common POS tags

| Tag | Description |
|---|---|
| `NN` | Noun, singular |
| `NNS` | Noun, plural |
| `NNP` | Proper noun, singular |
| `VB` | Verb, base form |
| `VBZ` | Verb, 3rd person singular present |
| `JJ` | Adjective |
| `RB` | Adverb |
| `DT` | Determiner |
| `IN` | Preposition or subordinating conjunction |

### Example

```python
from python_tools_and_shortcuts.nlp.parts_of_speech import calculate_part_of_speech_tags

tags = calculate_part_of_speech_tags("The quick brown fox jumps over the lazy dog.")
print(tags)
# ['DT', 'JJ', 'JJ', 'NN', 'VBZ', 'IN', 'DT', 'JJ', 'NN', '.']
```

### Dependencies

- `nltk`
