from pytube import YouTube

url = input("Enter the URL of the video: ")
video = YouTube(url)
print(video.title)

video = video.streams.get_highest_resolution()
video.download()