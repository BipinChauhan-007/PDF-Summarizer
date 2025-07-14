import cohere
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
cohere_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_key)

def generate_questions(text):
    prompt = f"""You are a quiz generator. Based on the following text, generate exactly 5 multiple choice questions (MCQs).
Each question must have:
- A numbered question (e.g., 1. What is...)
- Four options (A to D)
- Answer marked as 'Answer: X'

Text:
\"\"\"
{text}
\"\"\"

Output format:
1. Sample question?
   A) Option A
   B) Option B
   C) Option C
   D) Option D
   Answer: A

Only return 5 such MCQs in this format.
"""

    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=700,
        temperature=0.7
    )

    return response.generations[0].text.strip()


def parse_questions(raw_text):
    questions = []
    blocks = raw_text.strip().split("\n\n")

    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        if len(lines) >= 6:
            try:
                q = {
                    "question": lines[0],
                    "options": {
                        "A": lines[1][3:].strip(),
                        "B": lines[2][3:].strip(),
                        "C": lines[3][3:].strip(),
                        "D": lines[4][3:].strip()
                    },
                    "answer": lines[5].split(":")[-1].strip().upper()
                }
                questions.append(q)
            except Exception:
                continue

    return questions[:5]
