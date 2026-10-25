
import json
import re

def load_faqs():
    try:
        with open("faq.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Bot: FAQ file is missing or invalid.")
        return {}

def main():
    faqs = load_faqs()

    patterns = {
        "hours": r"\b(hours|timing|open|close)\b",
        "price": r"\b(price|cost|product)\b",
        "return": r"\b(returns?|refunds?|exchange)\b",
        "delivery": r"\b(delivery|shipping|order)\b"
    }

    print("=" * 35)
    print("CUSTOMER SUPPORT CHATBOT")
    print("=" * 35)
    print("Ask about hours, price, returns, or delivery.")
    print("Type bye, exit, or quit to stop.")

    while True:
        try:
            text = input("You: ").strip().lower()

            if not text:
                print("Bot: Please enter a question.")
                continue

            if re.fullmatch(r"(bye|exit|quit)", text):
                print("Bot: Thank you for chatting. Goodbye!")
                break

            found = False

            if re.search(r"\b(hello|hi|hey)\b", text):
                print("Bot: Hello! Welcome to our support assistant.")
                found = True

            for key, pattern in patterns.items():
                if re.search(pattern, text) and key in faqs:
                    print("Bot:", faqs[key])
                    found = True

            if re.search(r"\b(thanks|thank you)\b", text):
                print("Bot: You're welcome!")
                found = True

            if not found:
                print("Bot: Sorry, I didn't understand. Ask about hours, price, returns, or delivery.")

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    main()
