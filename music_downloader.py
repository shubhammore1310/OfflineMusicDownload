
from pathlib import Path
import yt_dlp
OUTPUT_DIR = Path("/storage/emulated/0/Music/termaxDownload")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def download_audio(url: str):
    options = {
        "format": "bestaudio/best",
        "outtmpl": str(OUTPUT_DIR / "%(id)s.%(ext)s"),
        "noplaylist": True,
        "windowsfilenames": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }],
    }

    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.download([url])
        print(f"\nFinished. Check: {OUTPUT_DIR}")
    except Exception as exc:
        print(f"Download failed: {exc}")


if __name__ == "__main__":
    url = input("Paste an authorized audio URL: ").strip()

    if url.startswith(("https://", "http://")):
        download_audio(url)
    else:
        print("Please enter a valid HTTP(S) URL.")
