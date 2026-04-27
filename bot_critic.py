import os
import json

from anthropic import Anthropic
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=api_key)

    history_path = "ccritic_history.json."
    if os.path.exists(history_path):
        with open(history_path, "r", encoding="utf-8") as file:
            messages: list[dict[str, str]] = json.load(file)
    else:
        messages = []
    system_prompt = (
    "Ти — суворий код-рев'ювер з 20 роками досвіду. "
    "Ти прискіпливий до якості коду, безпеки і архітектури. "
    "Завжди знаходиш мінімум 3 проблеми навіть у простому коді. "
    "Відповідай українською. Без сюсюкання, без 'молодець'. "
    "Прямо і конкретно."
)

    while True:
        user_input = input("Ти: ")

        if user_input.lower() in {"exit", "quit"}:
            with open(history_path, "w", encoding="utf-8") as file:
                json.dump(messages, file, ensure_ascii=False, indent=2)
            print("Бувай!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system=system_prompt,
            messages=messages,
        )

        assistant_text = "".join(
            block.text for block in response.content if getattr(block, "type", "") == "text"
        )
        print("Claude:", assistant_text)

        messages.append({"role": "assistant", "content": assistant_text})
        with open(history_path, "w", encoding="utf-8") as file:
            json.dump(messages, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
