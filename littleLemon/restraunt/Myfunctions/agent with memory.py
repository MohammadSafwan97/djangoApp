import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize memory as a list
conversation_memory = [
    {"role": "system", "content": "You are a math teacher. Only solve math problems and give answers. If the question is not related to math, respond: 'Please ask only math-related questions.'"}
]

def get_completion(user_prompt, model="gpt-3.5-turbo"):
    # Append user message to memory
    conversation_memory.append({"role": "user", "content": user_prompt})
    
    response = openai.chat.completions.create(
        model=model,
        messages=conversation_memory,
        temperature=0,
        max_tokens=50
    )
    
    # Append assistant's reply to memory
    assistant_reply = response.choices[0].message.content
    conversation_memory.append({"role": "assistant", "content": assistant_reply})
    
    return assistant_reply

# Example usage
while True:
    user_input = input("Ask a math question: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    answer = get_completion(user_input)
    print(answer)
