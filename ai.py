from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)


def get_response(prompt):
    result = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return result.text

def stream_response(prompt):
    stream = client.models.generate_content_stream(
        model = "gemini-2.5-flash",
        contents = prompt,
    )
    for chunk in stream:
        print(chunk.text, end ="", flush=True)
        print()
    