from pytube import YouTube
from os import makedirs


url = input('Enter The URL of the video: ')
yt = YouTube(url)
print()

videos = yt.streams
video = list(enumerate(videos))
for i in video:
    print(i)

m, s = divmod(yt.length, 60)
h, m = divmod(m, 60)
print(f'\nTitle: {yt.title}')  # Shows title of video
print(f'Views: {yt.views:,}'.replace(',', '.'))  # Shows number of views
print(f'Duration: {h:d}h, {m}m and {s}s\n')  # Shows length of video

print('Enter The Desired Option To Download The Format: ')
dn_option = int(input('Enter the Option: '))

makedirs('Videos', exist_ok=True)  # Create a folder to store the videos
dn_video = videos[dn_option]
dn_video.download(output_path='Videos')

print('\nThe video was downloaded successfully!')
