# YouTube Lecture Summarizer

## Project Description

The **YouTube Lecture Summarizer** is a tool designed to simplify YouTube lectures by generating automatic summaries. Users can enter a YouTube link and receive a concise summary of the content without needing to watch the entire lecture. The application uses `Flask` for the web interface and the OpenAI API to generate text summaries automatically.

### Features

- Extracts the transcript of YouTube videos using the `youtube-transcript-api`.
- Processes the transcript with the OpenAI API (`gpt-4o-mini` or `gpt-4`) to generate a concise summary.
- User-friendly web interface built with `Flask`, making it easy to input YouTube links and view summaries directly.

## Prerequisites

- **Python 3.7+**
- **OpenAI API Key**: Required to generate summaries using language models.
- **Virtual Environment** (optional but recommended): To manage dependencies in an isolated manner.

## Installation

1. **Clone the project**
   ```sh
   git clone https://github.com/your-username/youtube-summary-tool.git
   cd youtube-summary-tool
   ```

2. **Create a virtual environment** (optional)
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # for Windows
   source .venv/bin/activate  # for Linux/Mac
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**
   Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Start the web application**
   ```sh
   python src/app.py
   ```
   The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Generate a summary**
   - Open the web app in your browser.
   - Enter the YouTube link in the input field.
   - Click on "Generate Summary".
   - The summary will be displayed once the process is complete.

## Project Structure
```
youtube-summary-tool/
│
├── src/
│   ├── app.py                 # Flask web application
│   ├── summarizer.py          # Summarization using OpenAI API
│   ├── transcript_extractor.py # Transcript extraction from YouTube
│   └── templates/
│       └── index.html         # HTML template for the web interface
├── requirements.txt           # Python dependencies
└── README.md                  # Project description
```

## Required Libraries

- **Flask**: For the web interface.
- **openai**: To interact with the OpenAI API.
- **python-dotenv**: To load environment variables from the `.env` file.
- **youtube-transcript-api**: To extract transcripts from YouTube videos.

The required dependencies are listed in the `requirements.txt` file and can be installed using the following command:
```sh
pip install -r requirements.txt
```

## Notes

- Not all YouTube videos have transcripts. The tool only works with videos that have an available transcript.
- Make sure your API key is kept secure and not shared publicly.

## Future Enhancements

- **Batch Processing**: Add the ability to upload multiple YouTube links at once.
- **Sentiment Analysis**: Implement sentiment analysis of the lecture content.
- **Translation**: Automatically translate the summary into another language.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

Enjoy using the YouTube Lecture Summarizer! If you have suggestions or feedback, feel free to create an issue on GitHub.


