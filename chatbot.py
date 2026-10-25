
import re

faqs = {
    "hours": (
        r"\b(hours|timing|open|close)\b",
        "Our business hours are Monday to Saturday, 9 AM to 6 PM."
    ),
    "price": (
        r"\b(price|cost|product)\b",
        "Please check our product page for the latest prices."
    ),
    "return": (
        r"\b(returns?|refunds?|exchange)\b",
        "You can request a return within 7 days of purchase."
    ),
    "delivery": (
        r"\b(delivery|shipping|order)\b",
        "Orders usually arrive within 3-5 business days."
    )
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

        for pattern, answer in faqs.values():
            if re.search(pattern, text):
                print("Bot:", answer)
                found = True

        if re.search(r"\b(thanks|thank you)\b", text):
            print("Bot: You're welcome!")
            found = True

        if not found:
            print(
                "Bot: Sorry, I didn't understand. Ask about "
                "hours, price, returns, or delivery."
            )

    except (EOFError, KeyboardInterrupt):
        print("\nBot: Goodbye!")
        break
    except Exception:
        print("Bot: Something went wrong. Please try again.")
