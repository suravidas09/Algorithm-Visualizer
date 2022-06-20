from time import sleep

def start_merge_sort(data, draw_data,step_time):
    global color_data
    color_data=['grey' for x in range(len(data))]
    mergeSort(data,0,len(data)-1,draw_data,step_time)
    color_data=['green' for x in range(len(data))]
    draw_data(data,color_data)

def merge(data,start,end,draw_data,step_time):
    i=start
    j=(start+end)//2+1
    a=[]
    while i<=(start+end)//2 and j<=end:
        color_data[i]=color_data[j]='blue'
        draw_data(data,color_data)
        color_data[i]=color_data[j]='grey'
        sleep(step_time)
        if data[i]<data[j]:
            color_data[i]='green'
            draw_data(data,color_data)
            sleep(step_time)
            color_data[i]='grey'
            a.append(data[i])
            i+=1
        else:
            color_data[j]='green'
            draw_data(data,color_data)
            sleep(step_time)
            color_data[j]='grey'
            a.append(data[j])
            j+=1 
    while i<=(start+end)//2:
        color_data[i]='green'
        draw_data(data,color_data)
        sleep(step_time)
        color_data[i]='grey'
        a.append(data[i])
        i+=1
    while j<=end:
        color_data[j]='green'
        draw_data(data,color_data)
        sleep(step_time)
        color_data[j]='grey'
        a.append(data[j])
        j+=1
    for x in range(start,end+1):
        data[x]=a[x-start]

def mergeSort(data,start,end,draw_data,step_time):    
    if start>=end:
        return
    color_data[start:end+1]=['white' for x in range(start,end+1)]
    draw_data(data,color_data)
    sleep(step_time)
    color_data[start:end+1]=['grey' for x in range(start,end+1)]
    mergeSort(data,start,(start+end)//2,draw_data,step_time)
    mergeSort(data,(start+end)//2+1,end,draw_data,step_time)
    merge(data,start,end,draw_data,step_time)
    color_data[start:end+1]=['white' for x in range(start,end+1)]
    draw_data(data,color_data)
    sleep(step_time)
    color_data[start:end+1]=['grey' for x in range(start,end+1)]
    