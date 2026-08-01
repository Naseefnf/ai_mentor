import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_system_prompt(profile) -> str:
    meta_prompt = f"""You are configuring an AI tutor for a specific student. Based on their profile below, write a system prompt (2-4 sentences) that instructs an AI mentor how to teach this student. Output ONLY the system prompt text itself, nothing else — no preamble, no explanation.

Student profile:
- Subject: {profile.subject}
- Skill level: {profile.skill_level}
- Goals: {profile.goals}
- Learning style: {profile.learning_style}
- Feedback style preference: {profile.feedback_style}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": meta_prompt}],
    )
    return response.choices[0].message.content