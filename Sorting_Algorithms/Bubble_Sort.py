from time import sleep

from pyparsing import col
color_data=[]

def Bubble_Sort(data, draw_data, step_time):
    color_data=['grey' for x in range(len(data))]
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            color_data[j]=color_data[j+1]='white'
            draw_data(data,color_data)
            color_data[j]=color_data[j+1]='grey'
            sleep(step_time)
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                color_data[j]=color_data[j+1]='red'
                draw_data(data, color_data)
                color_data[j]=color_data[j+1]='grey'
                sleep(step_time)
        color_data[len(data)-1-i]='green'
        draw_data(data,color_data)
    color_data[0]='green'
    draw_data(data,color_data)