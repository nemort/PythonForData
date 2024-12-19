from moviepy.editor import VideoFileClip
from sys import argv

params = argv
vid_name = params[1]
cut_start_time = params[2]
cut_end_time = params[3]


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


start_time_seconds = time_to_seconds(cut_start_time)
end_time_seconds = time_to_seconds(cut_end_time)

vid = VideoFileClip(vid_name)

if start_time_seconds >= end_time_seconds or end_time_seconds > vid.duration:
    raise ValueError(f"Некорректные временные промежутки, {vid.duration}")


clip_cutout = vid.subclip(start_time_seconds, end_time_seconds)
clip_cutout.write_videofile(f"cut_{vid_name}", codec="libx264")


vid.close()
clip_cutout.close()
