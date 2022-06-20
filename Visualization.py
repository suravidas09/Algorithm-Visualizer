#Importing required modules
from ctypes.wintypes import SIZEL
import imp
import sys
from tkinter import*
from tkinter import ttk
import random

sys.path.insert(1,'C:\\Users\\KIIT\\OneDrive\\Desktop\\Data Sc. Practice\\Sorting_Algorithms')

from Bubble_Sort import Bubble_Sort
from Selection_Sort import Selection_Sort
from Insertion_Sort import Insertion_Sort
from Merge_Sort import start_merge_sort
from Quick_Sort import start_sort

#To store the array/heights of rectangle
data = []
#To store the colour of respective rectangles
color_data = []

#Start visualization
def visualize(algorithm,step_time):
    step_time/=10
    if algorithm=="Bubble Sort":
        Bubble_Sort(data,draw_data,step_time)
    elif algorithm=="Merge Sort":
        start_merge_sort(data,draw_data,step_time)
    elif algorithm=="Selection Sort":
        Selection_Sort(data,draw_data,step_time)
    elif algorithm=="Insertion Sort":
        Insertion_Sort(data,draw_data,step_time)
    elif algorithm=="Quick Sort":
        start_sort(data,draw_data,step_time)

#Function to generate random data for visualization
def generate_data(data_size):
    global data,color_data
    data=color_data=[]
    #Set initial color of elements to grey
    color_data=['grey' for x in range(int(float(data_size)))]
    for _ in range(int(float(data_size))):
        data.append(random.randrange(1,100))
    #Draw the elemets on canvas
    draw_data(data,color_data)
    size_label.config(text=str(format(int(float(data_size)),"0>3d")))

#Function to draw rectangles, 'data' is a list of rectangle heights and 'color_data' is the respective colors
def draw_data(data,colorData):
    global height,width
    #Clears canvas before drawing new data
    canvas.delete("all")
    #Set the canvas height and width
    canvas_h=height-20
    canvas_w=width
    #Set the spacing between two rectangles
    spacing=2
    #Set the width of one rectangle
    rectangle_w=(canvas_w-spacing*(len(data)-1))/len(data)
    #Normalize the data
    for i in range(len(data)):
        data[i]=data[i]/max(data)
    #Draw the normalized data
    for i,rect_height in enumerate(data):
        x0=i*rectangle_w+(i+1)*spacing
        y0=canvas_h-rect_height*(canvas_h-20)
        x1=(i+1)*rectangle_w+(i+1)*spacing
        y1=canvas_h
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorData[i])
    root.update_idletasks()

#To change display delay on the label
def disp_delay(delay):
    delay.config(text=str(format(float(delay)/10,">03.1f")+" sec"))

#Main visualizer GUI
def main():

    #Set width and height of window
    global width,height
    width=1000
    height=610
    global root
    root=Tk()
    root.title("Algorithm Visualizer")
    style=ttk.Style()
    style.configure('TScale',background='black')
    root.resizable(0,0)
    root.config(bg='black')

    #To store the selected algorithm from combobox
    algorithm=StringVar()

    global title,delay,size_label
    title=Frame(root,width=width,height=height,bg='black')
    title.grid(row=0,column=0)
    size_label=Label(title,text="50",bg='black',fg='white',font=('Helvetica',25,'bold'))
    size_label.pack(side=LEFT,padx=(10,200))
    Label(title,text="Algorithms Visualizer",bg='black',fg='white',font=('Helvetica',25,'bold')).pack(pady=10,side=LEFT)
    delay=Label(title,text="0.0 sec",bg='black',fg='white',font=('Helvetica',25,'bold'))
    delay.pack(side=LEFT,padx=(190,10))

    #Top frame for user input
    top_frame=Frame(root,width=width, height=250 , bg='black')
    top_frame.grid(row=1,column=0,padx=10,pady=5)

    global size,speed
    size=IntVar()
    speed=IntVar()
    Label(top_frame,text="Step Delay (sec)",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=0,column=0,padx=5,pady=5,sticky=E)
    speed_scale=ttk.Scale(top_frame,variable=speed,from_=0,to=10,command=disp_delay)
    speed_scale.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    Label(top_frame,text="Select Algorithm",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=0,column=3,padx=(50,0),pady=5,sticky=E)
    algorithm_menu=ttk.Combobox(top_frame,textvariable=algorithm,state='readonly',values=['Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Quick Sort'])
    algorithm_menu.grid(row=0,column=4,padx=5,pady=5,sticky=W)
    algorithm_menu.current(0)

    #Second row top_frame 
    Label(top_frame,text="Size",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=1,column=0,padx=5,pady=5,sticky=E)
    size_scale=ttk.Scale(top_frame,variable=size,from_=3,to=100,command=generate_data)
    size_scale.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    size.set(50)
    Button(top_frame,text="Visualise",bg='white',command=lambda : visualize(algorithm.get(),speed.get())).grid(row=1,column=3,padx=(50,0),pady=5,ipadx=10,sticky=W)
    
    #Canvas for the live visualisation
    global canvas
    canvas = Canvas(root,width=width,height=height-20,bg='black')
    canvas.grid(row=2,column=0,padx=10,pady=5)

    #generate 50 elements on GUI startup
    generate_data(50)
        
    root.mainloop()

if __name__ == "__main__":
    main()    

    

