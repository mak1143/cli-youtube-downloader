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

- Run from anywhere via `ytdl` command (no `cd` needed)
- Pass URL as argument or get prompted interactively
- Supports `youtube.com`, `youtu.be`, and `music.youtube.com` URLs
- Input validation — catches empty input, bad URLs, and unavailable videos
- Custom output directory with `-o` flag
- Progress callback during download
- Saves to `~/Downloads/` by default

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

3. Install (makes `ytdl` available globally):

With pip (recommended):
```bash
pip install -e .
```

Or with pipx (Arch Linux / PEP 668):
```bash
pipx install -e .
```

Or with uv:
```bash
uv sync
```

## Usage

```bash
ytdl [url] [-o DIR]
```

After install, run from anywhere:

```bash
# Interactive prompt
ytdl

# Pass URL directly
ytdl "https://youtube.com/watch?v=..."

# Music.youtube.com also works
ytdl "https://music.youtube.com/watch?v=..."

# Custom output directory
ytdl -o ~/Videos/ "https://youtube.com/watch?v=..."

# Show help
ytdl --help
```

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
├── ytdl.py           # CLI YouTube downloader
├── pyproject.toml    # Project configuration
├── README.md         # This file
└── uv.lock           # Dependency lock file (uv)
```

## License

MIT
