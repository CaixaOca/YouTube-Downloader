import tkinter as tk
from tkinter import filedialog
import os
import subprocess

# Create the Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw() # hides the root window because we're only interested in the file dialog.

while True:
    print("YouTube downloader by CaixaOca");
    link = input("YouTube link: ")
    downloadFormat = input("Download format (audio/video): ").lower()
    if downloadFormat != "audio" and downloadFormat != "video": 
        print("Invalid format")
        continue
    
    downloadFolder = filedialog.askdirectory(title="Select Download Folder")

    # check if download folder exists
    if os.path.exists(downloadFolder) and os.path.isdir(downloadFolder):
        # if downloadformat == video command = x else command = y
        if downloadFormat == "video": subprocess.run("yt-dlp " + link + " --format bv*+ba/b --paths \"" + downloadFolder + "\"")
        if downloadFormat == "audio": subprocess.run("yt-dlp " + link + " --format ba --extract-audio --audio-format mp3 --audio-quality 0 --embed-metadata --embed-thumbnail --no-keep-video --paths \"" + downloadFolder + "\"")
    else: 
        print("Invalid Folder")
        continue
