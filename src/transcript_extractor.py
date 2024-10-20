import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(youtube_url):
    video_id_regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(video_id_regex, youtube_url)
    if match:
        return match.group(1)
    else:
        return None


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text_list = [transcript[i]["text"] for i in range(len(transcript))]
        transcript_text = "\n".join(text_list)
        return transcript_text
    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return None
