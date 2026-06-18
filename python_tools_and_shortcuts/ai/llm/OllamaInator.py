import os

#from python_tools_and_shortcuts.ai.llm.token_count_estimation import estimate_token_count_by_rules_of_thumb

class OllamaInator():

    #
    # Constructor
    #
    def __init__(
        self,
        api_key = os.environ.get('OLLAMA_API_KEY'),
        host="https://ollama.com",    
    ):
        from ollama import Client
        self.client = Client(
            host = host,
            headers = {
                'Authorization' : 'Bearer ' + api_key,
            },
        )

    #
    # Run a generate query
    #
    def run_generate(
        self,
        prompt,
        model = 'gpt-oss:120b',
    ) -> dict:
        response = self.client.generate(
            model = model,
            prompt = prompt,
        )

        return {
            'tokens_prompt' : response['prompt_eval_count'],
            'tokens_response' : response['eval_count'],
            'response_text' : response['response'],
        }

def main():
    oi = OllamaInator()
    prompt = 'What is the meaning of life?'
    dict_response = oi.run_generate(prompt)

    print('Tokens (prompt):', dict_response['tokens_prompt'])
    print('Tokens (response):', dict_response['tokens_response'])
    print()
    #print(estimate_token_count_by_rules_of_thumb(dict_response['response_text'], return_consensus_only = True))
    #print(len(prompt))
    #print(len(dict_response['response_text']))
    #print()
    print(dict_response['response_text'])
    print()
    
if __name__ == '__main__':
    main()
