
from moviepy.editor import VideoFileClip
import xlrd

laps = 59
xl = xlrd.open_workbook(r'times.xlsx')
video = VideoFileClip("alpine skiing.mp4")
for i in range(4):
    table = xl.sheets()[0]
    start = i*laps+1
    end = start+laps
    col_start = table.col_values(2, start, end)
    col_end = table.col_values(3, start, end)
    for j in range(laps):
        clip = video.subclip(col_start[j],col_end[j])
        clip.write_videofile("static/movies/rank"+str(i+1)+"_"+str(j+1)+".mp4")