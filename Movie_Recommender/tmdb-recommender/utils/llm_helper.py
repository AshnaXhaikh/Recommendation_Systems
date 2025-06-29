# llm_helper.py

import os
import openai

api_key ='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'


def get_llm_response(prompt):
    client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
    )
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {"role": "system", "content": "You are a helpful movie assistant, which provides movie recommendations and insights in a brief and concise manner."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    try:
        if response and response.choices and response.choices[0].message:
            return response.choices[0].message.content
        else: 
            return "❌ No valid response received from the LLM."
    except Exception as e:
        return f"LLM  Error: {str(e)}"