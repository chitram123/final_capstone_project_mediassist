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

def determine_source(question):

    prompt = f"""
You are a router.

Available Sources:

1. RAG
- Medical knowledge
- Hospital policies
- SOPs
- Uploaded documents

2. MCP
- Patient history
- Lab results
- Billing
- Payments

3. MULTIMODAL
Use when the question refers to an uploaded prescription or uploaded medical report.

Examples:
- What medicines are prescribed?
- What dosage is mentioned?
- How often should the medicine be taken?
- Summarize this prescription.
- Explain this report.
- What abnormalities are present in the uploaded report?

Question:
{question}

Return ONLY one word:

RAG
or
MCP
or
MULTIMODAL
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    source = response.choices[0].message.content.strip()

    return source

def determine_mcp_tool(question):

    prompt = f"""
You are an MCP tool selector.

Available tools:

1. search_patient
   - Search patient by name
   - patient details

2. patient_history
   - Get patient details/history

3. lab_results
   - Get lab reports

4. payment_summary
   - Get billing/payment information

Question:
{question}

Return ONLY one tool name.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()

def extract_patient_id(question):

    prompt = f"""
Extract the patient ID from the question.

Return only the numeric patient ID.
Do not return any explanation.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    patient_id = response.choices[0].message.content.strip()

    return int(patient_id)

def generate_mcp_answer(question, mcp_result):

    prompt = f"""
You are MediAssist AI.

The user asked:

{question}

The MCP tool returned:

{mcp_result}

Convert the raw data into a clear, user-friendly response.

Do not show raw arrays.
Summarize the information in readable language.
"""

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

    return response.choices[0].message.content

def generate_report_analysis(report_text):

    prompt = f"""
You are MediAssist AI.

Analyze the following medical prescription or medical report.

Your responsibilities:

1. If it is a prescription, extract:
   - Medicines
   - Dosage
   - Frequency

2. If it is a laboratory report,
   summarize the observations.

3. Explain only what is present in the document.

IMPORTANT:
- Do NOT diagnose diseases.
- Do NOT recommend medicines.
- Do NOT suggest treatments.
- Do NOT add information that is not present in the document.

Medical Document:

{report_text}
"""

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

    return response.choices[0].message.content

def generate_multimodal_answer(
    question,
    prescription_context
):

    prompt = f"""
You are MediAssist AI.

The user has uploaded the following prescription or medical report.

Prescription:

{prescription_context}

Answer ONLY using the uploaded prescription.

If the answer is not present in the prescription,
reply:

"The uploaded prescription does not contain this information."

Question:

{question}
"""

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

    return response.choices[0].message.content