<p align="center">
  <img
    width="250"
    alt="pytubefix_logo"
    src="https://github.com/user-attachments/assets/f57a840f-9fa7-465c-997b-17bdf8f8be2e"
  />
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/dm/pytubefix">
  <img src="https://img.shields.io/github/sponsors/juanbindez">
  <img src="https://img.shields.io/pypi/l/pytubefix">
  <img src="https://img.shields.io/readthedocs/pytubefix">
  <img src="https://img.shields.io/github/v/tag/JuanBindez/pytubefix?include_prereleases">
  <img src="https://img.shields.io/pypi/v/pytubefix">
  <img src="https://img.shields.io/pypi/pyversions/pytubefix.svg">
</p>

<h2 align="center">
  Python3 Library for Downloading YouTube Videos
</h2>

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
git clone https://github.com/mak1143/cli-youtube-downloader.git
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
usage: `ytld [url] [-o DIR] [-a]`

### Option 1: Run directly
```bash 
run ytdl <url> from anywhere

```
## How It Works
|> Works from anywhere
* `ytdl "https://youtube.com/watch?v=.."`
* `ytdl -a "https://youtube.com/watch?v=.."`  # audio-only
* `ytdl -o ~/Videos/ "https://youtube.com/watch?v=.."` 
* `ytdl` # prompts for URL interactively 


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
