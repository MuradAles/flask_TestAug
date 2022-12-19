import os
import openai

from tqdm import trange
from testaug.testaug.testaug import query_gpt


def generate_gpt3_test_suite(
    texts,
    query_budget=5,
    n_per_query=1,
):
    def parse(output):
        texts = list()
        for text in output.split("}"):
            texts.append(text.replace("}", "").replace("{", ""))
        return [text for text in texts if text]

    # openai.api_key = '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'
    # openai.api_key = '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'
    # openai.api_key = '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'
    openai.api_key = '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'
    prompt = "\n".join(["- {{{}}}\n".format(text) for text in texts])
    prompt += "\n- {"

    extracted_texts = list()
    for _ in trange(query_budget):
        response = query_gpt(model="text-davinci-003",
                             prompt=prompt, n_per_query=n_per_query)

        for choice in response.choices:
            extracted_texts.extend(parse(choice.text))

    return extracted_texts


# texts = [
#     "i love pepperoni pizza",
#     "i like udon noodles",
#     "my favorite food is steak"
# ]

# output = generate_gpt3_test_suite(texts)

# print(output)
