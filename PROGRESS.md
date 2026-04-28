# AI Learning Progress

## День 1 — 25 квітня 2026

### Що зроблено
- Встановлено Homebrew, Python 3.14.4, Git, VS Code
- Налаштовано Git (user.name, user.email)
- Встановлено Python + Pylance extensions у VS Code
- Створено папку проєкту `~/ai-freelancer-path`
- Створено і активовано virtual environment (`venv`)

### Що зрозумів
- Термінал — основний інструмент розробника
- Homebrew ставить програми на рівень macOS (`brew install`)
- pip ставить Python-бібліотеки в активний venv (`pip install`)
- venv ізолює проєкт — індикатор `(venv)` зліва у підказці
- Початок сесії: `cd ~/ai-freelancer-path` → `source venv/bin/activate`

### Питання, які залишились туманними
- (заповни сам, якщо є щось)

### Наступна сесія
- GitHub-акаунт + перший репозиторій
- Anthropic API key + поповнення $5
- Перший скрипт `hello_ai.py` — твій перший AI-запит з Python

## День 2 — 26 квітня 2026

### Що зроблено
- Перейменував проєкт на ai-builder-path
- Встановив Cursor як основний редактор + Claude Pro
- Створив GitHub репо ai-builder-path (public)
- Отримав Anthropic API key, поповнив $5
- Перший AI-скрипт hello_ai.py працює — Claude відповідає українською
- Налаштував .gitignore, перший commit + push

### Що зрозумів
- venv ламається при перейменуванні папки — треба перестворювати
- API key показується ОДИН раз — копіювати одразу
- Дублювати ключ при copy-paste = 401 error
- .gitignore ДО першого коміту — інакше секрети витечуть на GitHub
- Cursor + Cmd+L = AI-coding workflow, не просто автокомпліт

### Питання, які залишились туманними
- (заповни сам)

### Наступна сесія
- Module 1: Python для AI
- Перший проєкт: CLI persona bot

## Модуль 1 завершено — 27 квітня 2026

### Скрипти на GitHub
- hello_ai.py — перший API call
- cli_chat.py — інтерактивний чат з пам'яттю + sliding window
- bot_mentor.py — Сократ-персонаж (питання у відповідь)
- bot_critic.py — суворий код-рев'ювер
- bot_stand-up.py — комедіант

### Personal prompts library (prompts/)
- create_first_ai_script.md
- cli_chat_with_memory.md
- sliding_window_history.md
- system_prompt_personas.md

### Технічні концепції
- API vs Claude.ai (різниця, моделі оплати)
- Stateless природа LLM, persistent storage через JSON
- System prompts як інструмент програмування характеру
- Token economics (квадратичний ріст витрат)
- Sliding window як захист від token blow-up
- Cursor + Cmd+L AI-coding workflow
- Git workflow: add → commit → push
- .gitignore як захист API key

### Бізнес-розуміння
- SaaS-бізнес-модель, MRR/ARR/churn/LTV/CAC
- Реалістичні шанси досягти $10K MRR (1-3% за рік)
- Як побудовані PhotoAI, Cursor, Lovable

### Що далі
- Модуль 2: streaming, structured outputs, tool use, multi-model
