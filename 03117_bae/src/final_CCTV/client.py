import requests

def fetch_video_stream(url):
    """
    Fetch the video stream from the server without visualization.
    """
    stream = requests.get(url, stream=True)

    if stream.status_code != 200:
        print("Failed to connect to the video stream.")
        return

    for chunk in stream.iter_content(chunk_size=1024):
        if chunk:
            # Process the video data as needed
            # print(f"Received {len(chunk)} bytes of video data.")
            pass

if __name__ == "__main__":
    SERVER_URL = "http://192.168.0.9:8000" 

    print("Starting video stream fetch...")
    fetch_video_stream(f"{SERVER_URL}/video_feed")
