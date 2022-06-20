from time import sleep
color_data=[]

def Insertion_Sort(data, draw_data, step_time):
    color_data=['grey' for x in range(len(data))]
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        color_data[i]='blue'
        draw_data(data,color_data)
        sleep(step_time)
        while j>=0 and data[j]>key:
            color_data[j]='white'
            draw_data(data,color_data)
            sleep(step_time)
            color_data[j]='grey'
            data[j+1]=data[j]
            j-=1
        data[j+1]=key
        color_data[j+1]='red'
        draw_data(data,color_data)
        sleep(step_time)
        color_data[j+1]='grey'
        color_data[i]='grey'
    color_data=['green' for x in range(len(data))]
    draw_data(data,color_data)