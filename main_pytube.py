from pytube import YouTube

url = 'https://www.youtube.com/watch?v=w2cvZ3Z5YkQ'
my_video = YouTube(url)

print("*********video title**********")

print(my_video.title)

print("********video download********")

my_video = my_video.streams.get_highest_resolution()
#my_video = my_video.streams.first()

my_video.download()