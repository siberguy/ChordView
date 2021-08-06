import tkinter as tk
from getnote import *

fret_spacing = 70
string_spacing = 60
diam=16

def On_Draw(canvas,RW,RH,RM,key,chord,bnjo,ns):
    DrawFretboard(canvas,RW,RH,RM,key,chord,bnjo,ns)

def DrawFretboard(canvas,RW,RH,RM,key,chord,bnjo,ns):
        #dc = wx.PaintDC(self)
#       brush = wx.BrushFromBitmap(wx.Bitmap('granite.png'))
#        dc.SetBrush(brush)
        #dc.SetBrush(wx.Brush('#333333'))
        #dc.DrawRectangle(0, 0, RW+2*RM,(100+RH))
        canvas.create_rectangle(0,0, RW+2*RM,(100+RH),fill='#333333')
        #dc.SetFont(self.font)

        title = key+" "+chord
        fout=int(float(RW)/2.) - 8
        sout=30
        canvas.create_text(fout,sout,fill="black",font="Times 35 bold",text=title)
        #dc.SetPen(wx.Pen('#F8FF25'))
        #dc.SetTextForeground('#F8FF25')

        x0 = RM + fret_spacing
        y0 = 70
        y1 = RH-y0
        dy = int(float(RH-2*y0)/5.0)
        #import pudb;pu.db
        y1 = y1 +(ns-6)*dy
        
        for i in range(14):
            f =x0 + int(fret_spacing*i)
#            if not (i % 100):
            #dc.DrawLine(f,20, f,RH-20)
            if bnjo == 0 :
                ys=y1
            else:
             if i >4:
                ys = y1
             else:
                ys = y1 - dy
            canvas.create_line(f,y0,f,ys,fill='#F8FF25')
            #w, h = dc.GetTextExtent(str(i))
            #if(i > 0):
            #   dc.DrawText(str(i), f-w/2,RH-10)
#            elif not (i % 20):
#                dc.DrawLine(i+RM, 0, i+RM, 8)
#            elif not (i % 2): dc.DrawLine(i+RM, 0, i+RM, 4)

        #print("\n\n")
        for i in range(ns):
            f = y0 + i*dy
            #dc.DrawLine(70,f, RW+2*RM - 70,f)
            #print("S  bnjo = ",i,bnjo)
            if bnjo == 0:
                  canvas.create_line(x0,f,RW-RM,f,fill='#F8FF25')
            if bnjo == 1 and i == 4:
                  canvas.create_line(x0+6*dy,f,RW-RM,f,fill='#F8FF25')
            else:
                  canvas.create_line(x0,f,RW-RM,f,fill='#F8FF25')
            fout = RM
            sout = y0 + i*string_spacing
            sout = f
            canvas.create_rectangle(fout+diam, sout+diam, fout-diam, sout-diam, fill='#888888')
            canvas.create_text(fout,sout,fill="black",font="Times 20 bold",text=tuning_note[i])

        #dc.SetFont(self.font2)
        #print("keys,chords ",self.keys,self.chords)
        draw_notes(canvas,key,chord,fret_spacing,fret_spacing,string_spacing,string_spacing,bnjo,ns)

        return



def draw_notes(canvas,key,chord,f1,df,s1,ds,bnjo,ns):
        note = 0
        s1 = s1+13
        ds = ds - 5
        #dc.SetBrush(wx.Brush('white'))
        #dc.SetTextForeground('#000000')
        for f in range(0, numfrets):
              for s in range(0, (ns)):
                       note = get_note(s,f,key,chord,ns,bnjo) 
#                      #print "f,s ",f,s,' note = ',note
                       fout = f1 + f*df
                       sout = s1 + s*ds
#                      print ' note = ',note
                       if bnjo == 0:
                         if(note != ""):
                          #dc.DrawCircle(fout+11,sout+11,12) 
                            canvas.create_oval(fout+diam, sout+diam, fout-diam, sout-diam, fill='#000000')
                            #canvas.create_oval(50+diam, 50+diam, 50-diam, sout-diam, fill='#000000')
                         canvas.create_text(fout,sout,fill="white",font="Times 20 bold",text=note)
                       if bnjo == 1 and s < 4:
                         if(note != ""):
                            canvas.create_oval(fout+diam, sout+diam, fout-diam, sout-diam, fill='#000000')
                         canvas.create_text(fout,sout,fill="white",font="Times 20 bold",text=note)
                       if bnjo == 1 and s == 4 and f > 4:
                         if(note != ""):
                            canvas.create_oval(fout+diam, sout+diam, fout-diam, sout-diam, fill='#000000')
                         canvas.create_text(fout,sout,fill="white",font="Times 20 bold",text=note)
                       #dc.DrawText(note,fout+2,sout+2)
#                      print "f,s ",fout,sout,' note = ',note
                       
        return








