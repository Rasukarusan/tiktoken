from fastapi import FastAPI
from pydantic import BaseModel
import tiktoken
import urllib.parse
from typing import List

app = FastAPI()

# トークン分割後のバイト文字列を、分割されたまま復元して返す
# ex.) [b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab', b'\xe5\xa4', b'\x9c'] -> ["こんに", "夜"]
def decodeByteStrings(byte_strings) -> List[str]:
    temp_byte = b""
    result = []
    for b in byte_strings:
        try:
            temp_byte += b
            decode_str = temp_byte.decode()
            temp_byte = b""
            result.append(decode_str)
        except:
            pass
    return result

# トークン数とトークン分割文字列を取得
def get_token(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    bs = enc.decode_tokens_bytes(tokens)
    result = decodeByteStrings(bs)
    return {"token": len(tokens), "token_text": result}


class PostTokenRequest(BaseModel):
    text: str
class PostTokenResponse(BaseModel):
    token: int
    token_text: List[str]

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
