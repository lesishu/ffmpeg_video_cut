# video_cut 视频自动剪辑工具
适用于抖音、Tiktok等，1080x1920（可自行修改参数适配不同规格的视频）。

# 使用方法
命令语句：\
python3 video_cut.py 视频文件名

命令行示例：\
python3 video_cut.py 01.mp4

# 参数详解

-hide_banner	命令行执行时隐藏Banner，简化输出信息\
-vf	颜色滤镜\
hqdn3d	画质增强\
eq=contrast=1.06	对比度增加到 1.06 倍\
brightness=0.03	亮度提升0.03\
saturation=1.06	饱和度101%\
contrast=1.01	白色（Whites）\
brightness=0.1	黑色（Blacks）\
gamma=1.5	阴影（Shadows）\
hflip	水印翻转\
crop=iw*0.99:ih*0.99:ow-iw:oh-ih	右下角 99% 的内容，裁剪掉了左上角的部分\
unsharp	锐化，使用默认参数\
trim=start_frame=6	掐头，从第6帧开始\
drawtext=text='@test':x=168:y=1680:fontsize=32:fontcolor=white"	插入字幕\
|-r 60	输出帧率\
|-y	直接覆盖输出同名文件\
|-b:v 20000k	输出视频码率\
|-bufsize 20000k	输出Buffer缓存，和-b:v搭配用，让码率更稳定\
|-maxrate 20000k	最大码率\
|-force_key_frames "expr:gte(t,n_forced*0.99)"	每间隔0.99秒 强制关键帧\
|-s 1080x1920	输出视频尺寸\
|-preset slow	编码速度和质量\
-vcodec libx264	视频使用Libx264编码\
-acodec aac	音频使用AAC编码\
|-an	输出不带音频\
-metadata title="Puppy Love"	设置视频文件头信息：Title\
-shortest	音视频适配，根据短的截断\
|-filter:v "setpts=1.03*PTS"	变速\
|output_$(date +"%Y%m%d_%H%M%S").mp4	输出文件名：output_年月日_时分钟秒.mp4