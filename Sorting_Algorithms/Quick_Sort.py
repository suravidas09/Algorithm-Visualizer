from time import sleep
color_data=[]

def start_sort(data, draw_data,step_time):
    global color_data
    color_data=['grey' for x in range(len(data))]
    Quick_Sort(data,0,len(data)-1,draw_data,step_time)
    color_data=['green' for x in range(len(data))]

def Quick_Sort(data,start,end,draw_data,step_time):
    if start>=end:
        return
    pivot=partition(data,start,end)
    Quick_Sort(data,start,pivot-1,draw_data,step_time)
    Quick_Sort(data,pivot+1,end,draw_data,step_time)

def partition(data,start,end):
    i=start-1
    pivot=data[end]
    for j in range(start,end):
        if data[j]<=pivot:
            i+=1
            data[i],data[j]=data[j],data[i]
    data[i+1],data[end]=data[end],data[i+1]
    return i+1

#data=[434243,34,23,2323,121]
#start_sort(data,0,0)
#print(data)