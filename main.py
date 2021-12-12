from tkinter import *
import math
FONT = ('Arial',24,'normal')
WHITE_C = "#fff"
BG = '#444'
WORK_TIME_MINS = 25
SHORT_REST_TIME = 5
LONG_REST_TIME = 10
repts = 0
root = Tk()
root.config(padx=80,pady=80,bg=BG)
root.title('Learn Time')
def start_count():
    global repts
    repts += 1
    if repts % 2 == 0:    
        count_down(SHORT_REST_TIME*60)
        timer_label.config(text='short Rest time')
        canvas.config(bg='green')
        
    elif repts % 8 ==0 :
        count_down(SHORT_REST_TIME*60)
        timer_label.config(text='Long Rest time')
        canvas.config(bg='green')
    else:
        count_down(WORK_TIME_MINS*60)
        timer_label.config(text='Time to work')
        canvas.config(bg='red')

def count_down(counter):
    mins = math.floor(counter / 60)
    secs = counter % 60
    if mins < 10:
        mins = f'0{mins}'
    if secs < 10:
        secs = f'0{secs}'
    if counter > 0:
        root.after(1000, count_down, counter-1)
        canvas.itemconfigure(clock,text=f"{mins} : {secs}")
    else:
        start_count()
        

    



timer_label = Label(root, text='Timer',fg=WHITE_C,font=FONT,bg= BG)
timer_label.grid(row=0,column=1,columnspan=2,pady=20)
canvas = Canvas(width=200,height=80,bg=BG)
canvas.grid(row=1,column=1,columnspan=2)
clock = canvas.create_text(100,40,text='00 : 00',font=FONT,fill=WHITE_C)
start_btn = Button(text="Start",pady=15,padx=30,command=start_count)
start_btn.grid(row=2,column=1,pady=20)

clear_btn = Button(text="clear",pady=15,padx=30)
clear_btn.grid(row=2,column=2,pady=20)




root.mainloop()