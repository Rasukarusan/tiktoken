# Tiktoken

[tiktoken](https://github.com/openai/tiktoken)でトークン数とトークン分割された文字配列を取得

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

https://tiktoken-ten.vercel.app/docs

`POST /token`

Example

```sh
curl -sXPOST 'http://localhost:8000/token' -d '{"text": "こんにちわ"}' -H 'Content-Type:application/json' | jq
# {
#   "token": 3,
#   "token_text": [
#     "こんに",
#     "ち",
#     "わ"
#   ]
# }
```
