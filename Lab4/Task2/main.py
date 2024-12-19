import os
from moviepy.editor import VideoFileClip
from sys import argv
from PIL import Image


def time_to_seconds(time_str: str) -> int:
    time_parts = time_str.split(":")
    if len(time_parts) != 3:
        raise ValueError("Некорректный формат времени. Ожидался формат чч:мм:сс")
    hours, minutes, seconds = map(int, time_parts)
    if minutes < 0 or minutes > 59:
        raise ValueError(f"Некорректное значение минут: {minutes}. Допустимый диапазон: 0-59.")
    if seconds < 0 or seconds > 59:
        raise ValueError(f"Некорректное значение секунд: {seconds}. Допустимый диапазон: 0-59.")
    return hours * 3600 + minutes * 60 + seconds


params = argv
vid_name = params[1]
cut_start_time = params[2]
cut_end_time = params[3]
output_dir = params[4]
step = int(params[5]) if len(params) > 5 else 10

start_time_seconds = time_to_seconds(cut_start_time)
end_time_seconds = time_to_seconds(cut_end_time)

vid = VideoFileClip(vid_name)

if start_time_seconds >= end_time_seconds or end_time_seconds > vid.duration:
    raise ValueError(f"Некорректные временные промежутки. Длительность видео: {vid.duration} секунд")

clip_cutout = vid.subclip(start_time_seconds, end_time_seconds)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_count = 0
for t in range(0, int(clip_cutout.duration), step):
    frame = clip_cutout.get_frame(t)
    img = Image.fromarray(frame)
    img = img.resize((250, int(250 * img.height / img.width)))
    output_frame_path = os.path.join(output_dir, f"{frame_count}.jpg")
    img.save(output_frame_path)
    frame_count += 1

vid.close()
clip_cutout.close()

print(f"Кадры успешно сохранены в папку: {output_dir}")
