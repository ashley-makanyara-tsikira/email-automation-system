
"""
Email Classifier - AI Operations
Author: Ashley Makanyara Tsikira
Saves 10+ hrs/week by auto-classifying emails
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CATEGORIES = ["Urgent", "Sales", "Support", "Spam", "General"]

def classify_email(email_text: str) -> str:
    categories = ["Urgent", "Sales", "Support", "Spam", "General"]

    prompt = f"""
    Classify this email into one category: {categories}
    Email: {email_text}
    Return only the category name.
    """

    # Production: Use OpenAI if key exists
    if os.getenv("OPENAI_API_KEY"):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            result = response.choices[0].message.content.strip()
            if result in CATEGORIES:
                return result
        except Exception as e:
            print(f"AI failed: {e}")

    # Demo fallback - lets anyone run your GitHub without an API key
    text = email_text.lower()
    if "urgent" in text or "asap" in text:
        return "Urgent"
    elif "buy" in text or "price" in text:
        return "Sales"
    elif "help" in text or "issue" in text:
        return "Support"
    elif "lottery" in text or "win" in text:
        return "Spam"
    else:
        return "General"

if __name__ == "__main__":
    test_email = "Need urgent help with my order"
    print(f"Category: {classify_email(test_email)}")
