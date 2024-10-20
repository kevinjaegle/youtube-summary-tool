from flask import Flask, request, render_template
from transcript_extractor import extract_video_id, get_transcript
from summarizer import summarize_transcript

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    youtube_url = request.form["youtube_url"]
    video_id = extract_video_id(youtube_url)
    if video_id:
        transcript_text = get_transcript(video_id)
        if transcript_text:
            summary = summarize_transcript(transcript_text)
            if summary:
                return render_template("index.html", summary=summary)
            else:
                return render_template(
                    "index.html", error="Failed to generate summary."
                )
        else:
            return render_template("index.html", error="Failed to extract transcript.")
    else:
        return render_template("index.html", error="Invalid YouTube URL.")


if __name__ == "__main__":
    app.run(debug=True)
