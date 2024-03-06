# Tiktoken

GPTでトークン数を計算

https://github.com/openai/tiktoken

## 🛠️Mac Setup

You can skip!

```sh
pyenv install 3.12.0
pyenv global 3.12.0
pip install pipenv
pipenv install fastapi
```

## Setup

```sh
pipenv install
```

## 🚀Run

```sh
pipenv run dev
```

## 📍API Endpoints

`/token`

Request
```json
{
    "text": string
}
```

Response
```json
{
    "token": number
    "cost": number
}
```

Example
```sh
curl -XPOST 'http://localhost:8000/token' -d '{"text": "こんにちわ"}'

#
# {
#     "token": 14,
#     "cost": 0.0001
# }
#
```
