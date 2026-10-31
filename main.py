from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

system_prompt = """
You are a helpful customer support assistant
for a Matatu SACCO based in Thika, Kenya.

Answer members' questions politely and clearly.

SACCO INFORMATION (DEMONSTRATION DATA):

1. General outstanding balance: KES 2,500.
2. Next meeting: Saturday, 7 November 2026,
   at 10:00 AM.
3. Membership registration fee: KES 5,000.

BALANCE QUESTION RULES:
- When a member asks for the general outstanding
  balance, state that the demonstration balance
  is KES 2,500.
- Explain that this is sample information and
  not a verified individual account balance.
- If a member asks for their personal account
  balance, direct them to the SACCO secretary
  for verification.
- Never claim to know an individual's actual
  outstanding balance.

IMPORTANT:
- Only answer questions on general outstanding balance, next meetings and registration fees.
- These are demonstration figures, not verified
  SACCO records.
- Do not invent information.
- Direct questions about individual account
  balances to the SACCO secretary for verification.
- Use Kenyan Shillings.
- Be concise and professional.
"""
def validate_question(user_question):

    if not user_question.strip():
        return False

    if user_question.isdigit():
        return False

    return True

def ask_assistant(user_question):
    try:
        message = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens = 300,
            system =system_prompt,
            messages = [
                {
                    "role": "user",
                    "content": user_question
                }
            ]
            
        )
        return message.content[0].text
    except Exception as error:
        return f"An error occured: {error}"
    


print("Welcome to Matatu SACCO Member Assistant")

user_question = input("Kindly type your question: ")
if validate_question(user_question):

    answer = ask_assistant(user_question)

    print("\nSACCO Assistant:")
    print(answer)

else:
    print("Please enter a valid question")
