import tkinter as tk
from getnote import *
from DrawFretboard import *

HEIGHT = 420
UH=100
THEIGHT=HEIGHT+UH
WIDTH = 1200
fb_w =int(0.8*int(WIDTH))
fb_h =HEIGHT
BD=20


def new_tuning():
    print("new tuning")
    childframe=tk.Toplevel(mainframe) # Child window 
    childframe.geometry("200x200")  # Size of the window 
    #childframe.title("www.plus2net.com")

    my_str1 = tk.StringVar()
    l1 = tk.Label(childframe,  textvariable=my_str1 )
    l1.grid(row=1,column=2) 
    my_str1.set("Hi I am Child window")
    return



def update_scene(canvas):
    print("\nkey = ",key.get())
    print("chord = ",chord.get())
    On_Draw(canvas,fb_w,fb_h,BD,key.get(),chord.get())

def on_select(evt,canvas):
#def on_select(evt,canvas):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    #print('You selected item %d: "%s"' % (index, value))
    print("\nkey = ",key.get())
    chord.set(value)
    print("chord = ",chord.get())
    On_Draw(canvas,fb_w,fb_h,BD,key.get(),chord.get())



mainframe =  tk.Tk()

canvas = tk.Canvas(mainframe, height=HEIGHT+UH, width=WIDTH)
canvas.pack()

key_frame =  tk.Frame(mainframe, bg='#80c1ff', bd=5)
chord_frame =  tk.Frame(mainframe, bg='#80c1ff', bd=5)
fretboard_frame =  tk.Frame(mainframe, bg='#0f010f', bd=5)
utility_frame =  tk.Frame(mainframe, bg='#030402', bd=5)
#chord_scrollbar = tk.Scrollbar(chord_frame,orient=tk.VERTICAL)
tuning_button = tk.Button(utility_frame, text='Set Tuning', bg='#111111',fg='#000000',
                          activebackground='#004444',width='12',height='1',
                          activeforeground='#222222',relief=tk.RAISED,
                          highlightbackground='#3E4149',highlightcolor='#777777',
                          command=lambda:new_tuning())

key_frame.place(relwidth=0.07, relheight=1)
chord_frame.place(relx=0.07,relwidth=0.13, relheight=1)
fretboard_frame.place(relx=0.20,relwidth=.80, relheight=0.9)
utility_frame.place(relx=0.20,relwidth=.80,rely=0.90, relheight=0.1)
tuning_button.pack(side=tk.LEFT)
#tuning_button.place(relx=0.1,relwidth=0.2,rely=0.0,relheight=0.9)
fb_canvas = tk.Canvas(fretboard_frame, height=HEIGHT, width=fb_w)
fb_canvas_hold = fb_canvas
fb_canvas.pack()

key=tk.StringVar()
key.set("C")
chord=tk.StringVar()
chord.set("major")


lb=tk.Listbox(chord_frame,selectmode=tk.SINGLE,bg='#ffffff',fg='#000000',justify=tk.LEFT,width=40)
              #yscrollcommand=chord_scrollbar)
#chord_scrollbar.config(command=lb.yview)
lb.place(relwidth=0.90,relheight=0.9,rely = 0.04)
#chord_scrollbar.place(relx=0.9,relheight=0.3,rely = 0.04)
#chord_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
#lb.bind("<<ListboxSelect>>", on_select)
#lb.bind("<ListboxSelect>", lambda event, arg=fb_canvas: on_select(event,arg))
lb.bind("<<ListboxSelect>>", lambda event: on_select(event, canvas=fb_canvas))
l = 0

for c,v in chords.items():
    lb.insert(tk.END,c)


l = 0
for k,v in keys.items():
    #print(k,v)
    rb=tk.Radiobutton(key_frame,text=k,variable=key,value=k,bg='#80c1ff',justify=tk.LEFT,command=lambda : update_scene(canvas=fb_canvas))
    rb.place(relwidth=0.86,relheight=0.1,rely = float(l)*0.08)
    l = l+1
    #tk.Radiobutton(key_frame,text=key_set,variable=key,value=value,command=lamda: update_scene(key.get())).pack()
#DrawFretboard(fb_canvas,fb_w,fb_h,20)
On_Draw(fb_canvas,fb_w,fb_h,BD,key.get(),chord.get())

mainframe.mainloop()

