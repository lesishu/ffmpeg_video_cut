# -*- coding: utf-8 -*-
import subprocess
import datetime
import sys

# 检查参数是否正确
if len(sys.argv) != 2:
    print("Usage: python script.py input_video_path")
    sys.exit(1)

# 获取输入视频文件路径
input_video_path = sys.argv[1]

# 构建输出视频文件路径
output_video_name = "output_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"
output_video_path = output_video_name

# 构建 ffmpeg 命令行
ffmpeg_command = [
    "ffmpeg", "-hide_banner", "-y", "-i", input_video_path,
    "-vf", "eq=contrast=1.06:brightness=0.03:saturation=1.06:brightness=0.01:contrast=1.01:gamma=1.01,crop=iw*0.99:ih*0.99:ow-iw:oh-ih,unsharp,trim=start_frame=6,hflip,hqdn3d,setpts=PTS/1.06,drawtext=text='@puppylove.top':x=w-mod(t*30\,w+tw):y=h-th-168:fontsize=36:fontcolor=white",
    "-b:v", "20000k", "-bufsize", "20000k", "-maxrate", "20000k", "-vcodec", "libx264", "-acodec", "aac",
    "-shortest", "-force_key_frames", "expr:gte(t,n_forced*0.99)", "-r", "60", "-s", "1080x1920", "-preset", "slow",
    "-metadata", "title=My Title", output_video_path
]

# 执行 ffmpeg 命令行
subprocess.run(ffmpeg_command)
