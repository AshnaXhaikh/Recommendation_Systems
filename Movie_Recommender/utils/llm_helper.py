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
