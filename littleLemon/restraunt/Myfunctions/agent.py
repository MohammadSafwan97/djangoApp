import openai
import os

# Make sure your API key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=50,
    )
    return response.choices[0].message.content
guide=" Only answer the question if it is about cricket if any other question is asked just simply say ask questions related to cricket only"
# Your text
prompt=input("What do you want to search")+guide





response = get_completion(prompt)
print(response)
