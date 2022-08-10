# -*- coding: utf-8 -*-

#### https://stackoverflow.com/questions/41656176/tkinter-canvas-zoom-move-pan

# Advanced zoom example. Like in Google Maps.
# It zooms only a tile, but not the whole image. So the zoomed tile occupies
# constant memory and not crams it with a huge resized image for the large zooms.
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import os

class AutoScrollbar(ttk.Scrollbar):
    ''' A scrollbar that hides itself if it's not needed.
        Works only if you use the grid geometry manager '''
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError('Cannot use pack with this widget')

    def place(self, **kw):
        raise tk.TclError('Cannot use place with this widget')

class Zoom_Advanced(ttk.Frame):
    ''' Advanced zoom of the image '''

    def __init__(self, mainframe, path,fidpath):
        ''' Initialize the main Frame '''
        ttk.Frame.__init__(self, master=mainframe)        
        self.master.title('Zoom with mouse wheel')
        self.CS=800
        self.master.minsize(self.CS+20,self.CS+20)
        
        # Vertical and horizontal scrollbars for canvas
        vbar = AutoScrollbar(self.master, orient='vertical')
        hbar = AutoScrollbar(self.master, orient='horizontal')
        vbar.grid(row=1, column=1, sticky='ns')
        hbar.grid(row=2, column=0, sticky='we')
        
        # Create canvas and put image on it
        self.canvas = tk.Canvas(self.master, highlightthickness=0,
                                xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=1, column=0, sticky='nswe')
        self.canvas.update()  # wait till canvas is created
        vbar.configure(command=self.scroll_y)  # bind scrollbars to the canvas
        hbar.configure(command=self.scroll_x)

        # Make the canvas expandable
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        
        # Give a minimum size to the canvas
        
        self.master.grid_columnconfigure(0,minsize=self.CS)
        self.master.grid_rowconfigure(1, minsize=self.CS)
        
        # Bind events to the Canvas
        self.canvas.bind('<Configure>', self.show_image)  # canvas is resized
        self.canvas.bind('<ButtonPress-1>', self.move_from)
        self.canvas.bind('<B1-Motion>',     self.move_to)
        self.canvas.bind('<MouseWheel>', self.wheel)  # with Windows and MacOS, but not Linux
        self.canvas.bind('<Button-5>',   self.wheel)  # only with Linux, wheel scroll down
        self.canvas.bind('<Button-4>',   self.wheel)  # only with Linux, wheel scroll up
        self.canvas.bind('<Double-Button-1>', self.clic_pixel)
        self.image = Image.open(path)  # open image
        self.fid = Image.open(path)  # open image
        self.width, self.height = self.image.size
        self.imscale = 1.0  # scale for the canvaas image
        self.delta = 1.3  # zoom magnitude
        
        # Put image into container rectangle and use it to set proper coordinates to the image
        self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)#,fill='red')
        
        
        # Plot some optional random rectangles for the test purposes
        # minsize, maxsize, number = 5, 20, 10
        # for n in range(number):
        #     x0 = random.randint(0, self.width - maxsize)
        #     y0 = random.randint(0, self.height - maxsize)
        #     x1 = x0 + random.randint(minsize, maxsize)
        #     y1 = y0 + random.randint(minsize, maxsize)
        #     color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
        #     self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, activefill='black')

        # Create cross 
        P1 =self.canvas.canvasx(0),  self.canvas.canvasy(0)# get visible area of the canvas²
        P2 =self.canvas.canvasx(self.canvas.winfo_width()),self.canvas.canvasy(self.canvas.winfo_height())
        
        self.circle = self.canvas.create_oval(P1, P2,outline=''),
        self.line1 = self.canvas.create_line(P1, P2, fill=''),
        self.line2 = self.canvas.create_line(P1[0], P2[1],P2[0],P1[1], fill='')

        self.show_image()
        # self.find_bbox()
        
        # create right frame
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=1, column=2)
        
        self.button = ttk.Button(self.frame, text="ok",command=self.master.destroy)
        self.button.grid(row=1)
        
                
        # display transparent fid mark
        # tkfid=ImageTk.PhotoImage(self.fid)
        tk.Label(self.master, text='hello').grid(column=4 ,row = 1, sticky= 'nsew')
        
        
        self.show_image()
        
        

    def scroll_y(self, *args, **kwargs):
        ''' Scroll canvas vertically and redraw the image '''
        self.canvas.yview(*args, **kwargs)  # scroll vertically
        self.show_image()  # redraw the image
        

    def scroll_x(self, *args, **kwargs):
        ''' Scroll canvas horizontally and redraw the image '''
        self.canvas.xview(*args, **kwargs)  # scroll horizontally
        self.show_image()  # redraw the image
        

    def move_from(self, event):
        ''' Remember previous coordinates for scrolling with the mouse '''
        self.canvas.scan_mark(event.x, event.y)
        

    def move_to(self, event):
        ''' Drag (move) canvas to the new position '''
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.show_image()  # redraw the image
        

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        print("\nzoom +/-")
        
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        bbox = self.canvas.bbox(self.container)  # get image area
        
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]: pass  # Ok! Inside the image
        else: return  # zoom only inside image area
        scale = 1.0
        
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down
            i = min(self.width, self.height)
            if int(i * self.imscale) < 30: return  # image is less than 30 pixels
            self.imscale /= self.delta
            scale        /= self.delta
            
        if event.num == 4 or event.delta == 120:  # scroll up
            i = min(self.canvas.winfo_width(), self.canvas.winfo_height())
            if i < self.imscale: return  # 1 pixel is bigger than the visible area
            self.imscale *= self.delta
            scale        *= self.delta
        self.canvas.scale('all', x, y, scale, scale)  # rescale all canvas objects
        print(self.imscale)
        self.show_image()
        

    def show_image(self, event=None):
        ''' Show image on the Canvas '''
        self.delete_cross()
        bbox1 = self.canvas.bbox(self.container)  # get image area
        # Remove 1 pixel shift at the sides of the bbox1
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  # whole image in the visible area
            bbox[0] = bbox1[0]
            bbox[2] = bbox1[2]
        if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  # whole image in the visible area
            bbox[1] = bbox1[1]
            bbox[3] = bbox1[3]
        self.canvas.configure(scrollregion=bbox)  # set scroll region
        x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        
        # print('x2 - x1 = ',int(x2 - x1))
        # print('y2 - y1 = ',int(y2 - y1))
        # print(self.canvas.winfo_width(),self.canvas.winfo_height())
        
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
            x = min(int(x2 / self.imscale), self.width)   # sometimes it is larger on 1 pixel...
            y = min(int(y2 / self.imscale), self.height)  # ...and sometimes not
            image = self.image.crop((int(x1 / self.imscale), int(y1 / self.imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
            imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(imageid)  # set image into background
            self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection
        
        self.draw_cross()
        
        print("show image")
            

        
    def clic_pixel(self, event):
        ''' left clic on image'''
        print("\ndouble clic")
        
        self.show_image()        
        self.find_bbox(event)
        
        print(self.imscale)

        print("\nchoosen point",event.x,event.y)
        
        
    def find_bbox(self,event):
        
        
        def pt(x,y,color='red'):
            self.canvas.create_oval(x-5,y-5,x+5,y+5, fill=color)
   
        ''' Show image on the Canvas '''
        bbox1 = self.canvas.bbox(self.container)  # get image area
        # Remove 1 pixel shift at the sides of the bbox1
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        print('\nbbox = ',bbox) # fenetre + image
        print('bbox1 = ',bbox1) # image
        print('bbox2 = ',bbox2) # fenetre
        
        self.canvas.create_rectangle(bbox, outline='red')
        self.canvas.create_rectangle(bbox1, outline='blue')
        self.canvas.create_rectangle(bbox2, outline='yellow')
        
        
        P1x = 0
        P1y = 0
        P2x =0
        P2y =  0
        
        imgx = np.linspace(P1x,P2x,self.width)
        imgy = np.linspace(P1y,P2y,self.height)
        
        
        # self.canvas.create_oval(P1x,P1y,
        #                         P2x,P2y, fill='red')
        pt(P1x,P1y,'blue')
        pt(event.x,event.y)
        
        
#%%% draw and delete cross   
    def draw_cross(self,event=None):
        # w=self.canvas.winfo_width()
        # h=self.canvas.winfo_height()
        P1 =self.canvas.canvasx(0),  self.canvas.canvasy(0)# get visible area of the canvas
                 
        P2 =self.canvas.canvasx(self.canvas.winfo_width()),self.canvas.canvasy(self.canvas.winfo_height())
        self.circle = self.canvas.create_oval(P1, P2,outline='red'),
        self.line1 = self.canvas.create_line(P1, P2, fill='red'),
        self.line2 = self.canvas.create_line(P1[0], P2[1],P2[0],P1[1], fill='red')
        # self.show_image()
        
        
    def delete_cross(self,event=None):
        self.canvas.delete(self.circle)
        self.canvas.delete(self.line1)
        self.canvas.delete(self.line2)
#%%%display fid ?
                
    # def display_fid(self,event=None):
        ''' Show image on the Canvas '''
        # bbox1 = self.canvas.bbox(self.container)  # get image area
        # # Remove 1 pixel shift at the sides of the bbox1
        # bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        # bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
        #          self.canvas.canvasy(0),
        #          self.canvas.canvasx(self.canvas.winfo_width()),
        #          self.canvas.canvasy(self.canvas.winfo_height()))
        # bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
        #         max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        # if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  # whole image in the visible area
        #     bbox[0] = bbox1[0]
        #     bbox[2] = bbox1[2]
        # if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  # whole image in the visible area
        #     bbox[1] = bbox1[1]
        #     bbox[3] = bbox1[3]
        # self.canvas.configure(scrollregion=bbox)  # set scroll region
        # x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        # y1 = max(bbox2[1] - bbox1[1], 0)
        # x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        # y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        
        imagetk = ImageTk.PhotoImage(self.fid)#.resize((int(x2 - x1), int(y2 - y1))))
        # imageid = self.canvas.create_image(anchor='nw', image=imagetk)
        # self.canvas.lower(imageid)  # set image into background
        self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection


#%%% Main
if __name__ =='__main__':
    
    lieu = 'maison'
    
    if lieu == 'maison':
        Path= r'C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\coins_to_check'
        PathFid =r'C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\Fid_mark_template'
        
    elif lieu == 'musee':
        Path =r'D:\ENSG_internship_2022\Burundi_1981-82\test7\01_CanvasSized\cornerToCheck'
        PathFid = r'D:\ENSG_internship_2022\Burundi_1981-82\Fid_mark_template'
    
  
    # OOOOOOOOOOOSSSSSSSSSSSKKKOOOOOOOUUUUUUUR https://www.tcl.tk/

    img = os.listdir(Path)[0]
    
    fid=os.listdir(PathFid)[1]
  
    
    path = r'{}\{}'.format(Path,img) # place path to your image here
    fidpath=r'{}\{}'.format(PathFid,fid) # place path to your fiducial mark here
    
    root=tk.Tk()
    app = Zoom_Advanced(root, path=path,fidpath=fidpath)
    root.mainloop()
    
    
    
    
    # Import the required libraries
    
    
    # from tkinter import *
    
    # # Create an instance of tkinter frame or window
    # win=Tk()
    
    # # Set the size of the tkinter window
    # win.geometry("700x350")
    
    # # Define a function to delete the shape
    # def on_click():
    #    canvas.delete(line)
    
    # # Create a canvas widget
    # canvas=Canvas(win, width=500, height=300)
    # canvas.pack()
    
    # # Add a line in canvas widget
    # line=canvas.create_line(100,200,200,35, fill="red", width=10)
    
    # # Create a button to delete the button
    # Button(win, text="Delete Shape", command=on_click).pack()
    
    # win.mainloop()