import time
from pytube import YouTube

# URL of the YouTube playlist
playlist_url = "https://www.youtube.com/watch?v=JX0agKW4noM&ab_channel=TheTechBlackBoard"

# Split the playlist URL to extract the video ID
video_id = playlist_url.split('v=')[1].split('&')[0]

# Create the direct video URL
video_url = f"https://www.youtube.com/watch?v={video_id}"

# Start measuring time
start_time = time.time()

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Get the default filename
video_filename = video_stream.default_filename

# Define the path to the Downloads directory
downloads_path = "C:/Users/aboal/Downloads/Downloads_Python"

# Download the video to the specified path
video_stream.download(output_path=downloads_path)

# Calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

# Print video name and download time
print(f"Video name:'{video_filename}' downloaded successfully !")
print(f"Download time: {elapsed_time:.2f}  seconds")
