from pytube import YouTube

def download(link):
    youtubeobject = YouTube(link)
    youtubeobject = youtubeobject.streams.get_highest_resolution()

    try:
        youtubeobject.download()
    except:
        print("An error has occered ")
    else:
        print("The video download succesfully")

link = input("Enter your youtube link: ")
download(link)