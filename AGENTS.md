# AGENTS.md - Development Guidelines

## Project Overview
Python CLI YouTube video downloader using `pytubefix` library. Python 3.14+ required.

## Commands

### Running the Application
```bash
python main.py
python youtube.py
```

### Testing (pytest)
```bash
pytest                          # Run all tests
pytest tests/test_youtube.py    # Run single test file
pytest tests/test_youtube.py::test_download_video  # Run single test
pytest -k "test_download"       # Run tests matching pattern
pytest -v                        # Verbose output
pytest --cov=.                   # With coverage
```

### Linting and Formatting (Ruff)
```bash
pip install ruff
ruff check .                     # Check issues
ruff check . --fix               # Auto-fix
ruff format .                    # Format code
```

### Type Checking (pyright)
```bash
pip install pyright
pyright .                        # Check all files
pyright youtube.py               # Check specific file
```

### Run All Checks
```bash
ruff check . && ruff format . && pyright . && pytest
```

## Code Style Guidelines

### General
- Follow PEP 8, max 100 characters per line
- 4 spaces for indentation, no tabs
- Use descriptive names

### Imports (3 groups, blank lines between, alphabetical)
```python
import os
import sys
from pathlib import Path

import requests
from flask import Flask

from youtube import download_video
from utils import format_size
```

### Type Hints
Use type hints for all arguments and returns. Use `None` instead of `Optional[type]` in Python 3.14+:
```python
def download_video(url: str, output_path: str | None = None) -> bool: ...
def get_video_info(yt: YouTube) -> dict[str, str]: ...
```

### Naming Conventions
- Functions/variables: `snake_case` (download_video)
- Classes: `PascalCase` (VideoDownloader)
- Constants: `UPPER_SNAKE_CASE` (MAX_RETRIES)
- Private: leading underscore (_internal_function)

### Error Handling
Use specific exceptions with meaningful messages:
```python
try:
    yt = YouTube(url)
except Exception as e:
    print(f"Failed to create YouTube object: {e}")
    return False
```

### Function Design
- Keep functions small (under 30 lines)
- Use explicit return types
- Avoid mutable default arguments:
```python
def process_video(url: str, options: dict[str, bool] | None = None) -> bool:
    options = options or {}
```

### Docstrings
Use Google-style for public functions/classes:
```python
def download_video(url: str, output_path: str) -> bool:
    """Download a YouTube video.

    Args:
        url: The YouTube video URL.
        output_path: Directory where the video will be saved.

    Returns:
        True if download succeeded, False otherwise.

    Raises:
        ValueError: If URL is invalid.
    """
```

### File Structure
```
.
├── main.py           # Entry point
├── youtube.py        # Core download functionality
├── utils/            # Utility modules (if needed)
│   └── __init__.py
├── tests/            # Test files (test_*.py)
├── pyproject.toml    # Project configuration
└── AGENTS.md         # This file
```

### Testing Guidelines
- Tests in `tests/` directory, `test_*.py` naming
- Descriptive names: `test_<function>_<expected_behavior>`
- Mock external dependencies (network, file system)

```python
import pytest
from unittest.mock import patch, Mock

def test_download_video_success():
    """Test successful video download."""
    with patch('youtube.YouTube') as mock_yt:
        mock_yt.return_value.title = "Test Video"
        mock_yt.return_value.streams.get_highest_resolution.return_value = Mock()
        
        result = download_video("https://youtube.com/watch?v=...")
        
        assert result is True
```

### Common Patterns

#### CLI (argparse)
```python
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Download YouTube videos")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", default="~/Downloads", help="Output directory")
    args = parser.parse_args()
    download_video(args.url, args.output)
```

#### Path Handling (pathlib)
```python
from pathlib import Path

output_dir = Path("~/Downloads").expanduser()
output_dir.mkdir(parents=True, exist_ok=True)
```

### Dependencies (pyproject.toml)
```toml
[project]
dependencies = [
    "pytubefix>=10.3.6",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.8.0",
    "pyright>=1.1.0",
]
```
