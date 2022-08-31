# type import
from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4

# import cors headers
from fastapi.middleware.cors import CORSMiddleware

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

from fastapi import FastAPI, HTTPException
from models import UserRequest, Phrase

app = FastAPI()

# cors urls
origins = ["http://localhost:3000"]
# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


# BUG working with Postman, not frontend
@app.get("/api/phrases")
def fetch_all():
    return "data from server"


# working with Postman, not frontend
@app.post("/api/phrases")
async def translate_request(req: UserRequest):
    print("req", req)
    target = req.lang
    text = req.string
    translated = translate_text(target, text)
    phrases.append(translated)
    return phrases


# example response from Google
# [
#   {
#     "translatedText": "車",
#     "detectedSourceLanguage": "en",
#     "input": "car"
#   }
# ]
