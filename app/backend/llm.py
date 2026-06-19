import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

# Initialize Groq client
client = Groq(
    api_key=GROQ_API_KEY
)

print("GROQ LOADED...")


def generate_answer(
    question,
    retrieved_chunks
):

    # Combine chunks into context
    context = "\n\n".join(
        retrieved_chunks
    )

    # Create prompt
    prompt = f"""
You are MediAssist AI, a healthcare assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
respond with:
Information not found in the knowledge base.
"""

    # Call Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer

