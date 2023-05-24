import openai
import os
import googletrans
from googletrans import Translator

# Replace 'your_api_key' with your actual API key
openai.api_key = "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"

def ask_gpt_35(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": prompt}])

    answer = completion.choices[0].message.content
    return answer

def personal_assistant():
    print("Hello! I am your personal assistant powered by GPT-3.5. How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Response: Goodbye! Have a great day!")
            break

        prompt = user_input
        response = ask_gpt_35(prompt)
        print(f"Response: {language_detection(user_input, response)}")


def language_detection(input, response):
    translator = googletrans.Translator()
    if translator.detect(input).lang.lower()=='co':
        return translator.translate(response, dest='corsican').text
    else:
        return response


if __name__ == "__main__":
    personal_assistant()

