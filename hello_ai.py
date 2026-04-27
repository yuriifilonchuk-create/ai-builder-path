import os

from anthropic import Anthropic
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in .env")

    client = Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Привітайся українською і коротко поясни, чим можеш мені допомогти у вивченні AI",
            }
        ],
    )

    response_text = "".join(
        block.text for block in message.content if getattr(block, "type", "") == "text"
    )
    print(response_text)


if __name__ == "__main__":
    main()
