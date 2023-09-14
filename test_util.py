"""
This is utility module which provides a terminal interface to perform HTTP calls to LLM and Embedding endpoints
"""
import sys
import time
import math
import argparse
import requests


EMBEDDING_ENDPOINT = "http://127.0.0.1:8090/embeddings/"
LLM_ENDPOINT = "http://127.0.0.1:8090/llm/"
API_TIMEOUT = 300  # 5 minutes


def time_tracker(func):
    """
    Decorator function which will be used to track time-taken for the endpoints to respond
    """
    def wrapper(prompt: str):
        start_time = time.time()
        func(prompt)
        end_time = time.time()
        print(f"\n\nAPI call took {int(math.ceil(end_time - start_time))} seconds")

    return wrapper


@time_tracker
def perform_llm_call(prompt: str):
    """
    Make a HTTP call to LLM endpoint and print the response string
    """
    response = requests.post(url=LLM_ENDPOINT, json=prompt, timeout=API_TIMEOUT)
    response.raise_for_status()
    print(response.json()['text'])


@time_tracker
def perform_emb_call(prompt: str):
    """
    Make a HTTP call to Embedding endpoint and print the response list-of-decimals
    """
    response = requests.post(url=EMBEDDING_ENDPOINT, json=prompt, timeout=API_TIMEOUT)
    response.raise_for_status()
    print(response.json())


def main():
    """
    Main function which run CMD utility
    """
    while True:
        try:
            prompt = input("> ")
            ep_fn(prompt)
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='LLM-and-Embedding-Test-Utility',
        description='It is a CMD program which helps to perform Q&A using the LLM deployed using this Repository. It also helps to generate Embeddings from your prompt',
        epilog='It is a CMD program which helps to perform Q&A using the LLM deployed using this Repository. It also helps to generate Embeddings from your prompt'
    )

    parser.add_argument('-ep', '--endpoint', choices=["LLM", "Embedding"], help="Choose one of LLM/Embedding", required=True)

    args = parser.parse_args()

    ep_fn = perform_llm_call if args.endpoint == "LLM" else perform_emb_call

    main()
