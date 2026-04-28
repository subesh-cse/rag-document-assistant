import os
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(context, query):
    try:
        prompt = f"""You are an expert AI assistant for document question answering.

Your task is to answer the question using ONLY the provided context.

Instructions:
- Write in clear and simple English
- Be concise and structured
- If it's a summary → give 3–5 bullet points
- If it's an explanation → use short bullet points or short paragraphs
- Do NOT make up information
- Avoid repeating the same idea multiple times
- If context is noisy, try to infer meaning carefully
- If answer is not found → say:
  "I don't know based on the provided documents."
- When possible, mention source like: (Source: filename.pdf)

Important:
- Base your answer strictly on the context
- Use only relevant parts of the context

Context:
{context}

Question:
{query}

Answer:
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful, precise, and reliable AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"