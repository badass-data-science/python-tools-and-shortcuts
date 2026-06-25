# ai/llm

LLM client utilities.

## `OllamaInator`

A thin wrapper around the [`ollama`](https://github.com/ollama/ollama-python) Python client for running generate queries against an Ollama-compatible endpoint.

### Constructor

```python
OllamaInator(
    api_key: str = os.environ.get('OLLAMA_API_KEY'),
    host: str = "https://ollama.com",
)
```

| Parameter | Description |
|---|---|
| `api_key` | API key for the Ollama endpoint. Defaults to the `OLLAMA_API_KEY` environment variable. |
| `host` | Base URL of the Ollama server. Defaults to `https://ollama.com`. |

### Methods

#### `run_generate(prompt, model) -> dict`

Sends a generate request and returns a dict with:

| Key | Description |
|---|---|
| `tokens_prompt` | Number of tokens in the prompt |
| `tokens_response` | Number of tokens in the response |
| `response_text` | The generated text |

Default model is `gpt-oss:120b`.

### Example

```python
from python_tools_and_shortcuts.ai.llm.OllamaInator import OllamaInator

oi = OllamaInator()
result = oi.run_generate("What is the meaning of life?")
print(result['response_text'])
```

### Dependencies

- `ollama`
