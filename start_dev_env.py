#!/usr/bin/env python3

import os
import webbrowser
import platform
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Windows username from the .env file
username = os.getenv("WINDOWS_USERNAME")
if not username:
    raise ValueError("WINDOWS_USERNAME not set in .env file, check the README.md file for more info.")

# Function to open websites
def open_websites():

    browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))

    websites = [
        "https://github.com/",
        "https://app.clickup.com/",
        "https://figma.com/",
        "https://chatgpt.com/",
        "https://minimalist-task-tracker.netlify.app/"
    ]

    for site in websites:
        webbrowser.get('chrome').open(site)

# Function to open applications
def open_apps():
    system = platform.system()
    
    apps = [
        fr"C:\Users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        fr"C:\Users\{username}\AppData\Local\SourceTree\app-3.4.17\SourceTree.exe",
    ]

    for app in apps:
        try:
            os.startfile(app)
        except Exception as e:
            print(f"Could not open {app}: {e}")

# Main script
if __name__ == "__main__":
    print("Starting development environment...")
    open_websites()
    open_apps()
    print("All set!")
