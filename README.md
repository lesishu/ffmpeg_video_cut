# single_video_cut.py 单视频剪辑
适用于抖音、Tiktok等，1080x1920（可自行修改参数适配不同规格的视频）。

# 使用方法
命令语句：\
```sh
python3 video_cut.py 视频文件名
```

命令行示例：
```sh
python3 video_cut.py 01.mp4
```

# 参数详解

-hide_banner  命令行执行时隐藏Banner，简化输出信息\
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
-r 60	输出帧率\
-y	直接覆盖输出同名文件\
-b:v 20000k	输出视频码率\
-bufsize 20000k	输出Buffer缓存，和-b:v搭配用，让码率更稳定\
-maxrate 20000k	最大码率\
-force_key_frames "expr:gte(t,n_forced\*0.99)"	每间隔0.99秒 强制关键帧\
-s 1080x1920	输出视频尺寸\
-preset slow	编码速度和质量\
-vcodec libx264	视频使用Libx264编码\
-acodec aac	音频使用AAC编码\
-an	输出不带音频【不需要声音时使用这个参数】\
-metadata title="My Title"	设置视频文件头信息：Title\
-shortest	音视频适配，根据短的截断\
-filter:v "setpts=1.03*PTS"	变速\
output_$(date +"%Y%m%d_%H%M%S").mp4	输出文件名：output_年月日_时分钟秒.mp4

# ffmpeg命令行
这段Python代码，也可以直接使用ffmpeg命令行实现同样的功能，命令行：
```sh
ffmpeg -hide_banner -y -i 08.mp4 -vf "eq=contrast=1.06:brightness=0.03:saturation=1.06:brightness=0.01:contrast=1.01:gamma=1.01,crop=iw\*0.99:ih\*0.99:ow-iw:oh-ih,unsharp,trim=start_frame=6,hflip,hqdn3d,setpts=PTS/1.06,drawtext=text='@test':x=w-mod(t\*30\\,w+tw):y=h-th-168:fontsize=36:fontcolor=white" -b:v 20000k -bufsize 20000k -maxrate 20000k -vcodec libx264 -acodec aac -shortest -force_key_frames "expr:gte(t,n_forced*0.99)" -r 60 -s 1080x1920 -preset slow -metadata title="My Title" output_$(date +"%Y%m%d_%H%M%S").mp4
```
# batch_video_cut.py 多视频剪辑
在batch_video_cut.py所在位置创建文件夹input，将需要剪辑的视频放到input文件夹中。\
运行batch_video_cut.py，会批量剪辑input文件夹中所有视频，保存在output文件夹。

# 声明
个人学习总结，可应用于任何用途。\
联系：lesishu@qq.com
