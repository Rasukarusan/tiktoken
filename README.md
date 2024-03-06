# Tiktoken

GPTでトークン数を計算

https://github.com/openai/tiktoken

## 🛠️Setup
```sh
pyenv install 3.12.0
pyenv global 3.12.0
pip install pipenv
pipenv install fastapi
```

## 🚀Run

```sh
uvicorn main:app --reload
```

## 📍API

body
```json
{
    "text": string
}
```

response
```json
{
    "token": number
    "cost": number
}
```

example
```sh
curl -XPOST http://localhost:8080 -d '{"text": "こんにちわ"}'

#
# {
#     "token": 14,
#     "cost": 0.0001
# }
#
```
