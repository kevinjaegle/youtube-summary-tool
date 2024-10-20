import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# OpenAI API-Key sicher einfügen
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print(
        "Warnung: OPENAI_API_KEY ist nicht gesetzt. Bitte füge ihn zu den Umgebungsvariablen oder zur .env Datei hinzu."
    )
else:
    client = OpenAI(api_key=api_key)


def summarize_transcript(transcript_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # oder gpt-4, wenn verfügbar
            messages=[
                {
                    "role": "user",
                    "content": f"Please provide a concise summary of the following lecture:\n{transcript_text}",
                }
            ],
            max_tokens=150,
            temperature=0.7,
        )

        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None
