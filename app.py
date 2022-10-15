from pytube import YouTube

link = input("Enter The URL of The Video : ")
yt = YouTube(link)

print("Title: ",yt.title)   # shows title of video
print("Number of views: ",yt.views)  # shows number of views
print("Length of video: ",yt.length)    # shows length of video
print("Rating of video: ",yt.rating)    # shows rating of video

videos = yt.streams.all()

video = list (enumerate(videos))

for i in video:
    print(i)

print("Enter The Desired Option To Download The Format : ")
dn_option = int(input("Enter the Option : "))

dn_video = videos[dn_option]
dn_video.download()

print("Downloaded Successfully!")
