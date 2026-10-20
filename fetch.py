
from pathlib import Path
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
}


url = "https://api.sejm.gov.pl/sejm/term10/proceedings/1/2023-11-13/transcripts/1"
response = requests.get(url, timeout=30)
response.raise_for_status()

Path("data/raw").mkdir(parents=True, exist_ok=True)
Path("data/raw/p1_2023-11-13_1.html").write_text(response.text, encoding="utf-8")