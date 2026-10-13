import yt_dlp
import os
import time



def ydl_download(ydl_opts, url):
    i = 0
    while True:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("-Done-")
            break
        except:
            print("-Error-")
            if i < 5:
                i += 1
                time.sleep(2)
            else:
                break

def select_platform (ydl_opts, url):
    if "youtube.com" in url or "youtu.be" in url:
        ydl_opts.update({'outtmpl': os.path.join(os.path.expanduser("~"), "Videos", "SMdownloads-vid", "youtube", "%(title)s.%(ext)s")})
    elif "instagram.com" in url:
        ydl_opts.update({'outtmpl': os.path.join(os.path.expanduser("~"), "Videos", "SMdownloads-vid", "instagram", "%(title)s [%(id)s].%(ext)s")})
    elif "tiktok.com" in url:
        ydl_opts.update({'outtmpl': os.path.join(os.path.expanduser("~"), "Videos", "SMdownloads-vid", "tiktok", "%(title)s.%(ext)s")})
    elif "facebook.com" in url:
        ydl_opts.update({'outtmpl': os.path.join(os.path.expanduser("~"), "Videos", "SMdownloads-vid", "facebook", "%(title)s.%(ext)s")})
    else:
        ydl_opts.update({'outtmpl': os.path.join(os.path.expanduser("~"), "Videos", "SMdownloads-vid", "%(title)s.%(ext)s")})


# audio
aud_links_list = []
aud_ydl_opts = {
    'format': "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
}
def_aud_outtmpl = {'outtmpl': os.path.join(os.path.expanduser("~"), "Music", "SMdownloads-aud", "%(title)s.%(ext)s"),}
insta_aud_outtmpl = {'outtmpl': os.path.join(os.path.expanduser("~"), "Music", "SMdownloads-aud", "%(title)s [%(id)s].%(ext)s"),}


# Video
vid_links_list = []
vid_ydl_opts_list = []

# 
print("Welcome; Check readme file to know how to use this.")
while True:

    entry_links = input("Enter links: ")
    if entry_links:

        entry_links_splited = entry_links.split()

        if "-a" in entry_links_splited:
            entry_links_splited.remove("-a")
            aud_links_list.extend(entry_links_splited)
        else:
            if "-v" in entry_links_splited:
                entry_links_splited.remove("-v")
            vid_links_list.append(entry_links_splited)
            while True:
                quality = input("Enter a quality: ")

                if not quality or quality == "high":
                    vid_ydl_opts_list.append({'format': 'bestvideo*+bestaudio/best'})
                    break
                elif quality in ["360", "480", "720", "1080", "1440", "2160"]:
                    vid_ydl_opts_list.append({'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'})
                    break
                
    else:
        break

# audios downloading
for aud_url in aud_links_list:
    if "http" not in aud_url:
        aud_links_list.remove(aud_url)
    else:
        if "instagram.com" in aud_url:
            aud_ydl_opts.update(insta_aud_outtmpl)
        else:
            aud_ydl_opts.update(def_aud_outtmpl)

        ydl_download(aud_ydl_opts, aud_url)

# Videos downloading
for ydl_vid_opts, url_list in zip(vid_ydl_opts_list, vid_links_list):
    for url in url_list:
        select_platform(ydl_vid_opts, url)
        ydl_download(ydl_vid_opts, url)