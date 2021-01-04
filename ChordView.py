import pdb
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
#numstrings=6
#banjo=0

current_tuning = 0

def on_select_tlb(evt,canvas):
    w = evt.widget
    #pdb.set_trace()
    #print("w tuning = ",w)
    if len(w.curselection()) == 0:
        return
    index = int(w.curselection()[0])
    value = w.get(index)
    #print('You selected item %d: "%s"' % (index, value))
    #print("new tuning ",value)
    nt = tunings.get(value,"999")
    #print("new tuning value = ",value)
    #print("new tuning nt = ",nt)
    l = len(nt)
    if l > 0 < 7:
        numstrings.set(l)
        for n in range(l):
            tuning_note[n]=nt[n]
            tuning[n] = tuning_dict.get(nt[n],"999")
    banjo.set(0)
    if l == 5:
        banjo.set(1)
    On_Draw(canvas,fb_w,fb_h,BD,key.get(),chord.get(),banjo.get(),numstrings.get())
    #print("new tuning numstrings = ",numstrings.get())
    #print("new tuning banjo = ",banjo.get())
    return

def new_tuning(canvas):
    childframe=tk.Toplevel(mainframe) # Child window 
    childframe.geometry("400x400")  # Size of the window 
    #childframe.title("www.plus2net.com")

    tlb=tk.Listbox(childframe,selectmode=tk.SINGLE,bg='#333355',fg='#888888',justify=tk.LEFT,width=15)
    tlb.pack(side=tk.LEFT,fill=tk.Y)
    tlb.bind("<<ListboxSelect>>", lambda evnt: on_select_tlb(evnt, canvas=canvas))
    l = 0
    for c,v in tunings.items():
        tlb.insert(tk.END,c)
    tlb.activate(0)

    #my_str1 = tk.StringVar()
    #l1 = tk.Label(childframe,  textvariable=my_str1 )
    #l1.grid(row=1,column=2) 
    #my_str1.set("Hi I am Child window")
    return



def update_scene(canvas):
    ##print("\nkey = ",key.get())
    #print("chord = ",chord.get())
    On_Draw(canvas,fb_w,fb_h,BD,key.get(),chord.get(),banjo.get(),numstrings.get())

def on_select(evt,canvas):
#def on_select(evt,canvas):
    w = evt.widget
    #pdb.set_trace()
    if len(w.curselection()) == 0:
        return
    index = int(w.curselection()[0])
    value = w.get(index)
    chord.set(value)
    #print('You selected item %d: "%s"' % (index, value))
    #print("\nkey = ",key.get())
    #print("chord = ",chord.get())
    On_Draw(canvas,fb_w,fb_h,BD,key.get(),chord.get(),banjo.get(),numstrings.get())
    return



mainframe =  tk.Tk()

canvas = tk.Canvas(mainframe, height=HEIGHT+UH, width=WIDTH)
canvas.pack()

key_frame =  tk.Frame(mainframe, bg='#80c1ff', bd=5)
chord_frame =  tk.Frame(mainframe, bg='#80c1ff', bd=5)
fretboard_frame =  tk.Frame(mainframe, bg='#0f010f', bd=5)
fb_canvas = tk.Canvas(fretboard_frame, height=HEIGHT, width=fb_w)
fb_canvas.pack()
utility_frame =  tk.Frame(mainframe, bg='#030402', bd=5)
#chord_scrollbar = tk.Scrollbar(chord_frame,orient=tk.VERTICAL)
tuning_button = tk.Button(utility_frame, text='Set Tuning', bg='#111111',fg='#000000',
                          activebackground='#004444',width='12',height='1',
                          activeforeground='#222222',relief=tk.RAISED,
                          highlightbackground='#3E4149',highlightcolor='#777777',
                          command=lambda:new_tuning(canvas=fb_canvas))

key_frame.place(relwidth=0.07, relheight=1)
chord_frame.place(relx=0.07,relwidth=0.13, relheight=1)
fretboard_frame.place(relx=0.20,relwidth=.80, relheight=0.9)
utility_frame.place(relx=0.20,relwidth=.80,rely=0.90, relheight=0.1)
tuning_button.pack(side=tk.LEFT)
#tuning_button.place(relx=0.1,relwidth=0.2,rely=0.0,relheight=0.9)
#fb_canvas_hold = fb_canvas

key=tk.StringVar()
key.set("C")
chord=tk.StringVar()
chord.set("major")
banjo=tk.IntVar()
banjo.set(0)
numstrings=tk.IntVar()
numstrings.set(6)


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
lb.activate(0)


l = 0
for k,v in keys.items():
    #print(k,v)
    rb=tk.Radiobutton(key_frame,text=k,variable=key,value=k,bg='#80c1ff',justify=tk.LEFT,command=lambda : update_scene(canvas=fb_canvas))
    rb.place(relwidth=0.86,relheight=0.1,rely = float(l)*0.08)
    l = l+1
    #tk.Radiobutton(key_frame,text=key_set,variable=key,value=value,command=lamda: update_scene(key.get())).pack()
#DrawFretboard(fb_canvas,fb_w,fb_h,20)
On_Draw(fb_canvas,fb_w,fb_h,BD,key.get(),chord.get(),banjo.get(),numstrings.get())

mainframe.mainloop()

