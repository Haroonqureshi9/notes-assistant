from google import genai
from google.genai import errors
from config import API_KEY
import time

client = genai.Client(api_key=API_KEY)


def get_response(prompt):
    result = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return result.text

def stream_response(prompt):
    for attempt in range(3):
        try:
            stream = client.models.generate_content_stream(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            for chunk in stream:
                print(chunk.text, end="", flush=True)
            print()
            return
        except errors.ServerError:
            if attempt < 2:
                print("\n[Server busy, retrying in 2 seconds...]")
                time.sleep(2)
            else:
                print("\n[Server still busy after 3 tries. Please try again later.]")