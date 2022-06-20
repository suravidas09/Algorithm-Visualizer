from time import sleep
color_data=[]

def Selection_Sort(data, draw_data,step_time):
    color_data=['grey' for x in range(len(data))]
    for i in range(len(data)):
        min=data[i]
        min_index=i
        color_data[i]='blue'
        for j in range(i+1,len(data)):
            color_data[j]='white'
            draw_data(data,color_data)
            color_data[j]='grey'
            sleep(step_time)
            if data[j]<min:
                color_data[min_index]='grey'
                min=data[j]
                min_index=j
                color_data[j]='blue'
                if j!=len(data)-1:
                    color_data[j+1]='white'
                draw_data(data,color_data)
                sleep(step_time)
        data[min_index],data[i]=data[i],data[min_index]
        color_data[i+1:]=['grey' for x in range(i+1,len(data))]
        color_data[i]='green'
        draw_data(data,color_data)
        sleep(step_time)