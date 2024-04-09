import os
import subprocess
import datetime

# 输入文件夹和输出文件夹路径
input_folder = "input"
output_folder = "output"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 获取输入文件夹中的所有文件
input_files = [file for file in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file))]

# 循环处理每个视频文件
for input_file in input_files:
    # 构建输入和输出文件路径
    input_path = os.path.join(input_folder, input_file)
    output_file_name = "output_" + os.path.splitext(input_file)[0] + ".mp4"
    output_path = os.path.join(output_folder, output_file_name)
    
    # 构建 ffmpeg 命令行
    ffmpeg_command = [
        "ffmpeg", "-hide_banner", "-y", "-i", input_path,
        "-vf", "eq=contrast=1.06:brightness=0.03:saturation=1.06:brightness=0.01:contrast=1.01:gamma=1.01,crop=iw*0.99:ih*0.99:ow-iw:oh-ih,unsharp,trim=start_frame=6,hflip,hqdn3d,setpts=PTS/1.06,drawtext=text='@test':x=w-mod(t*30\,w+tw):y=h-th-168:fontsize=36:fontcolor=white",
        "-b:v", "20000k", "-bufsize", "20000k", "-maxrate", "20000k", "-vcodec", "libx264", "-acodec", "aac",
        "-shortest", "-force_key_frames", "expr:gte(t,n_forced*0.99)", "-r", "60", "-s", "1080x1920", "-preset", "slow",
        "-metadata", "title=My Title", output_path
    ]

    # 执行 ffmpeg 命令行
    subprocess.run(ffmpeg_command)

print("All videos processed successfully.")
