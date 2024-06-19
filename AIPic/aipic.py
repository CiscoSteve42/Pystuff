#!/usr/bin/python3

from openai import OpenAI


client = OpenAI(api_key="your API key here")
response = client.images.generate(
    model="dall-e-3",
    prompt=input("What do you want a picture of? "),
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)
