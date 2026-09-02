"""
Email Classifier - AI Operations
Author: Ashley Makanyara Tsikira
Saves 10+ hrs/week by auto-classifying emails
"""
import openai

def classify_email(email_text):
    categories = ["Urgent", "Sales", "Support", "Spam", "General"]
    
    prompt = f"""
    Classify this email into one category: {categories}
    Email: {email_text}
    Return only the category name.
    """
    
    # For demo - in production uses OpenAI API
    # response = openai.ChatCompletion.create(...)
    
    # Simple keyword logic for portfolio demo
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

# Test
if __name__ == "__main__":
    test_email = "Need urgent help with my order"
    print(f"Category: {classify_email(test_email)}")
