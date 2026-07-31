from moviepy.editor import VideoFileClip

# Input video
video = VideoFileClip("cmp_stu.mp4")

# Resize (optional)
video = video.resize(width=900)

# Keep only first 10 seconds (optional)
video = video.subclip(0, 10)

# Save as GIF
video.write_gif(
    "portfolio_demo.gif",
    fps=15,
    program="ffmpeg"
)

print("GIF created successfully!")
