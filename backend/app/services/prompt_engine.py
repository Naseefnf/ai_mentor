# app/services/prompt_engine.py
import os
import time
from dotenv import load_dotenv
from groq import Groq, APIError

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

_prompt_cache = {}  # {user_id: (prompt, generated_at_timestamp)}
CACHE_DURATION_SECONDS = 30 * 60  # 30 minutes

def generate_system_prompt(profile) -> str:
    meta_prompt = f"""You are configuring an AI tutor for a specific student. Based on their profile below, write a system prompt (2-4 sentences) that instructs an AI mentor how to teach this student. Output ONLY the system prompt text itself, nothing else — no preamble, no explanation.

Student profile:
- Subject: {profile.subject}
- Skill level: {profile.skill_level}
- Goals: {profile.goals}
- Learning style: {profile.learning_style}
- Feedback style preference: {profile.feedback_style}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": meta_prompt}],
        )
        return response.choices[0].message.content
    except APIError:
        # Fallback: simple template-based prompt if the LLM call fails
        return (
            f"You are a patient AI mentor teaching {profile.subject} to a "
            f"{profile.skill_level} student. Their goal: {profile.goals}. "
            f"They prefer {profile.learning_style} learning and "
            f"{profile.feedback_style} feedback."
        )
    

def get_cached_or_generate_prompt(user_id: int, profile) -> str:
    now = time.time()

    if user_id in _prompt_cache:
        cached_prompt, generated_at = _prompt_cache[user_id]
        if now - generated_at < CACHE_DURATION_SECONDS:
            return cached_prompt

    new_prompt = generate_system_prompt(profile)
    _prompt_cache[user_id] = (new_prompt, now)
    return new_prompt