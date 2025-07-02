import requests
from bs4 import BeautifulSoup
import json
import sys
import instaloader
import argparse
import os
from instaloader.exceptions import ConnectionException

ASCII_BANNER = r'''
    ____           __        ____       _ _       __ 
   /  _/___  _____/ /_____ _/ __ \_____(_|_)___  / /_
   / // __ \/ ___/ __/ __ `/ / / / ___/ / / __ \/ __/
 _/ // / / (__  ) /_/ /_/ / /_/ (__  ) / / / / / /_  
/___/_/ /_/____/\__/\__,_/\____/____/_/_/_/ /_/\__/  
 
    InstaOSINT - Instagram OSINT Tool by Anchit D
'''

def extract_instagram_metadata(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        metadata = {
            "username": profile.username,
            "full_name": profile.full_name,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "bio": profile.biography,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified,
            "profile_pic_url": profile.profile_pic_url,
            "external_url": profile.external_url,
        }
        return metadata, profile
    except ConnectionException as ce:
        print("[!] Instagram is blocking access or rate-limiting. Try again later or reduce your request frequency.")
        return None, None
    except Exception as e:
        print(f"Failed to retrieve profile: {e}")
        return None, None

def download_profile_pic(profile, output_dir):
    url = profile.profile_pic_url
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f"{profile.username}_profile_pic.jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Profile picture downloaded to {file_path}")
    else:
        print("Failed to download profile picture.")

def download_recent_posts(profile, n, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    L = instaloader.Instaloader(dirname_pattern=output_dir, download_comments=False, save_metadata=False, post_metadata_txt_pattern="")
    count = 0
    try:
        for post in profile.get_posts():
            if count >= n:
                break
            print(f"Downloading post {count+1}...")
            L.download_post(post, target=profile.username)
            count += 1
        print(f"Downloaded {count} post(s) to {output_dir}")
    except ConnectionException:
        print("[!] Instagram is blocking access or rate-limiting. Could not download posts.")

def main():
    print(ASCII_BANNER)
    parser = argparse.ArgumentParser(description="InstaOSINT - Instagram OSINT Tool")
    parser.add_argument("username", nargs="?", help="Instagram username to analyze")
    parser.add_argument("--download-pic", action="store_true", help="Download profile picture")
    parser.add_argument("--download-posts", type=int, metavar="N", help="Download the most recent N posts")
    parser.add_argument("--output", type=str, default="downloads", help="Output directory for downloads")
    args = parser.parse_args()

    if not args.username:
        args.username = input("Enter Instagram username: ")

    data, profile = extract_instagram_metadata(args.username)
    if data:
        for key, value in data.items():
            print(f"{key}: {value}")
        if args.download_pic and profile:
            download_profile_pic(profile, args.output)
        if args.download_posts and profile:
            download_recent_posts(profile, args.download_posts, args.output)
    else:
        print("Failed to extract metadata.")

if __name__ == "__main__":
    main() 