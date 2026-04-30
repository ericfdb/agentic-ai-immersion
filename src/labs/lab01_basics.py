"""Lab 1: Financial Services Advisor — agent basics."""

from .client import get_project_client
from .agent import create_agent, ask

INSTRUCTIONS = """
You are a friendly AI Financial Services Advisor for a retail bank.
You provide general information about banking products, loans, and financial services, but always:
1. Include regulatory and financial disclaimers.
2. Encourage users to consult with licensed financial advisors for personalized advice.
3. Provide general, non-personalized guidance around banking, loans, savings, and investments.
4. Clearly remind users you're not a licensed financial advisor and cannot provide investment recommendations.
5. Follow responsible banking practices and never suggest risky financial behaviors.
6. Explain concepts like APR, interest rates, credit scores, and loan terms in simple language.
"""

QUESTIONS = [
    "What factors affect my mortgage interest rate and how can I get a better rate?",
    "How is my credit score calculated and what can I do to improve it?",
    "What's the difference between a savings account, CD, and money market account?",
]


def main():
    client = get_project_client()
    print("Connected to Azure AI Foundry")

    advisor = create_agent(client, "financial-services-advisor", INSTRUCTIONS)
    print(f"Created agent: {advisor.name} v{advisor.version}")

    for q in QUESTIONS:
        print(f"\n{'='*60}")
        print(f"Q: {q}\n")
        answer = ask(client, advisor, q)
        print(f"A: {answer}")


if __name__ == "__main__":
    main()
