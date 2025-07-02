# InstaOSINT

Instagram OSINT tool for extracting public profile metadata.

## Features
- Extracts public metadata from Instagram profiles
- Command-line interface (CLI)
- Download profile picture
- Download recent posts

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ianchitdas/instaosint.git
   cd instaosint
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install the package:**
   ```sh
   pip install .
   ```
   If you want to install in development mode (editable):
   ```sh
   pip install -e .
   ```

## Usage

After installation, run the tool from your terminal:

```sh
python -m instaosint.main <username> [OPTIONS]
```

### CLI Options
- `--download-pic` : Download the profile picture of the user
- `--download-posts N` : Download the most recent N posts
- `--output DIR` : Specify the output directory for downloads (default: downloads)

### Example Usage
- Show metadata only:
  ```sh
  python -m instaosint.main instagram_username
  ```
- Download profile picture:
  ```sh
  python -m instaosint.main instagram_username --download-pic
  ```
- Download the 3 most recent posts:
  ```sh
  python -m instaosint.main instagram_username --download-posts 3
  ```
- Download both profile picture and 5 recent posts to a custom directory:
  ```sh
  python -m instaosint.main instagram_username --download-pic --download-posts 5 --output myfolder
  ```

You will be prompted to enter an Instagram username if not provided as an argument. The tool will display public metadata for that profile, including the last active date (most recent post).

## Requirements
- Python 3.6+
- `requests`
- `beautifulsoup4`
- `instaloader`

All dependencies are installed automatically with the above `pip install -r requirements.txt` command.

## Notes
- This tool only extracts public information from Instagram profiles.
- For private profiles, only limited metadata will be available.

## License
MIT
