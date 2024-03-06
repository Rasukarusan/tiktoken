from fastapi import FastAPI
from pydantic import BaseModel
import tiktoken
import urllib.parse

app = FastAPI()

# トークン数取得
def get_token(text):
    # @see https://platform.openai.com/tokenizer
    # @see https://zenn.dev/microsoft/articles/3438cf410cc0b5
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    # 2024年3月6日現在 @see https://openai.com/pricing
    inputCost = 0.00001 # 1トークンあたりにかかるドル
    print(text)
    print(len(tokens))
    print(tokens)
    return {"token": len(tokens), "cost": f'{inputCost * len(tokens):.2f}', "version": "2024-03-06"}


class PostTokenRequest(BaseModel):
    text: str
class PostTokenResponse(BaseModel):
    token: int
    cost: float
    version: str

@app.get("/token/{text}")
def token(text: str) -> PostTokenResponse:
    return get_token(urllib.parse.unquote(text))

@app.post("/token")
def token(req: PostTokenRequest) -> PostTokenResponse:
    return get_token(req.text)



class EncResponse(BaseModel):
    result: bool
# /tokenのtiktoken.get_encoding()の引数に何をいれるのかを取得するためのメソッド
# 特にエンドポイントにする必要はない
@app.get("/enc")
def get_encoding() -> EncResponse:
    enc = tiktoken.encoding_for_model('gpt-4-turbo')
    print (enc)
    return { "result": True }
