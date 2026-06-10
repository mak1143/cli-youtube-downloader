# CLI YouTube Downloader

A simple command-line tool to download YouTube videos in high resolution using Python.

## Features

- Download videos from YouTube in highest available resolution
- Progress callback during download
- Saves to `~/Downloads/` by default
- Simple CLI interface

## Requirements

- Python 3.14+
- [pytubefix](https://github.com/ypxl/pytubefix) >= 10.3.6

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cli-youtube-downloader.git
cd cli-youtube-downloader
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

Or with uv:
```bash
uv sync
```

## Usage

### Option 1: Run directly
```bash
python youtube.py
```

### Option 2: Run via main
```bash
python main.py
```

## How It Works

1. Run the script
2. Enter a YouTube URL when prompted
3. Video downloads automatically to `~/Downloads/`
4. Progress is shown during download

```
Please use youtube music for audio
please enter youtube url>: https://youtube.com/watch?v=example
Downloading: Video Title
Completed! Video Title >: file saved to: ~/Downloads/
```

## Note

For audio-only downloads, use [YouTube Music](https://music.youtube.com) URLs with the same library.

## Development

### Run tests
```bash
pytest
```

### Lint and format
```bash
ruff check . && ruff format .
```

### Type check
```bash
pyright .
```

### Run all checks
```bash
ruff check . && ruff format . && pyright . && pytest
```

## Project Structure

```
.
├── main.py           # Entry point
├── youtube.py        # Core download functionality
├── pyproject.toml    # Project configuration
├── README.md         # This file
└── AGENTS.md         # Development guidelines
```

## License

MIT