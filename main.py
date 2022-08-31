# type import
from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

from fastapi import FastAPI, HTTPException
from models import UserRequest, Phrase

app = FastAPI()

phrases = []

# Google Translate - Client API
def translate_text(target, text):
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result


@app.get("/api/phrases")
def fetch_all():
    return phrases


# @app.get("/phrases/request")
# async def add_phrases(phrase: UserRequest):
#     return phrases


# doesn't work if I include await for translate function!
@app.post("/api/phrases/request")
async def translate_request(req: UserRequest):
    print(req)
    target = req.request_lang
    text = req.request_string
    translated = translate_text(target, text)
    phrases.append(translated)
    return phrases


# [
#   {
#     "translatedText": "車",
#     "detectedSourceLanguage": "en",
#     "input": "car"
#   }
# ]
