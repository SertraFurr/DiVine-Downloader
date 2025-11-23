import websocket
import json
import sys
import re
import requests

final_url = None

RELAY_URL = "wss://relay.divine.video/"

def extract_id(url_or_id: str):
    url_or_id = url_or_id.strip()
    if re.fullmatch(r"[0-9a-f]{64}", url_or_id):
        return url_or_id
    m = re.search(r"/video/([0-9a-f]{64})", url_or_id)
    if m:
        return m.group(1)
    sys.exit("Error: Invalid URL or event ID")

def on_message(ws, message):
    global final_url
    data = json.loads(message)
    if data[0] == "EVENT":
        event = str(data[2]["tags"][1][1].strip())
        final_url = event.split(" ")[1]

        ws.close()

def on_open(ws):
    event_id = extract_id(sys.argv[1])
    sub = [
        "REQ",
        "SuperTemporaryID",
        {"ids": [event_id], "kinds": [34236], "limit": 1}
    ]
    ws.send(json.dumps(sub))

def create_directory():
    import os
    directory = "./DiVine"
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_video(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        filename = url.split("/")[-1]

        with open("./DiVine/"+filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Video downloaded successfully as {filename}")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url or id>")
        sys.exit(1)

    print("Connecting to relay...", RELAY_URL)
    ws = websocket.WebSocketApp(
        RELAY_URL,
        on_open=on_open,
        on_message=on_message
    )
    ws.run_forever()
    try:
        create_directory()
    except Exception as e:
        print(f"Error creating directory: {e}")

    if final_url:
        print("Video URL:", final_url)
        print("Trying to download video...")
        try:
            download_video(final_url)
            print("Download completed. Saved in ./DiVine/")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: Video URL not found.")
