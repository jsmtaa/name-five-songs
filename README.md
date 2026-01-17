# So you wear a band shirt? Name five songs.

A small Python program inspired by the “name five songs” meme.

Ever encountered an "avid music lover" who doesn't really want their favorite artists to be known?
They're called gatekeepers, and they seem to not want some artists to have food on their table.

This program solves it for you.  
You enter an artist or band name, and it attempts to list **five songs by that artist** using the iTunes Search API.

If it can’t confidently find five matching tracks, you lose (and completely make the artist go broke).

---

## How It Works

- Prompts the user for a band or artist name
- Fetches song results from the iTunes Search API
- Filters results to match the artist name
- Displays up to five valid tracks
- Falls back if not enough matches are found

---

## Requirements

- Python 3
- `requests` library

Install dependencies:
```bash
pip install requests
```
