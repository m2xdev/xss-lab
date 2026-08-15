# xss-lab

Учебный полигон для демонстрации XSS-атак и защиты от них с помощью [xss-shield](https://github.com/m2xdev/xss-shield) (nh3).

## Что это

Флеск-приложение с парами маршрутов: уязвимая версия и защищённая версия рядом,
чтобы наглядно показать, как `strip_xss()` из xss-shield блокирует реальные payload'ы.

| Маршрут | Что показывает |
|---|---|
| `/vuln/reflected` | Reflected XSS без защиты |
| `/secure/reflected` | Тот же поиск, но через `strip_xss()` |
| `/vuln/stored` | Stored XSS — комментарии без очистки |
| `/secure/stored` | Комментарии, очищенные через `strip_xss()` |
| `/vuln/dom` | DOM-based XSS (nh3 её **не** закрывает — санитизация нужна на клиенте) |

## Запуск

```bash
git clone https://github.com/m2xdev/xss-lab
cd xss-lab
pip install -r requirements.txt
python app.py
```

Открыть в браузере: `http://127.0.0.1:5000`

Тестовые payload'ы — прямо на страницах уязвимых маршрутов.

## ⚠️ Дисклеймер / Disclaimer

### Русская версия

Этот репозиторий содержит **намеренно уязвимый код** и предназначен исключительно
для обучения и демонстрации механизмов XSS-атак и защиты от них.

- Запускайте только локально или в изолированной среде (Docker/VM), никогда — на
  публичном сервере или в общей сети.
- Не используйте код из `/vuln/*` маршрутов как образец для реальных проектов —
  это намеренные антипримеры.
- Не тестируйте техники, показанные здесь, на чужих сайтах или системах без
  явного разрешения — это может быть незаконно.

Программное обеспечение предоставляется **«КАК ЕСТЬ»**, без каких-либо явных
или подразумеваемых гарантий. Используя данный код, вы самостоятельно несёте
ответственность за его применение и любые последствия. Автор не несёт
ответственности за ущерб, возникший в результате использования данного ПО.

### English version

This repository contains **intentionally vulnerable code** and is intended
solely for educational purposes — to demonstrate XSS attack and defense
mechanisms.

- Run locally or in an isolated environment (Docker/VM) only — never on a
  public server or shared network.
- Do not use the code in `/vuln/*` routes as a template for real projects —
  these are deliberate anti-patterns.
- Do not test the techniques shown here against third-party sites or systems
  without explicit authorization — doing so may be illegal.

The software is provided **"AS IS"**, without warranty of any kind, express
or implied. By using this code, you are solely responsible for its use and
any resulting consequences. The author is not liable for any damages arising
from the use of this software.

## Связанные проекты

- [xss-shield](https://github.com/m2xdev/xss-shield) — сама библиотека защиты, которую тестирует эта лаба
