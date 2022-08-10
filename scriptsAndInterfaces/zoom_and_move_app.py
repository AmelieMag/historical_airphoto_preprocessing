# -*- coding: utf-8 -*-
<<<<<<< HEAD
# https://stackoverflow.com/questions/41656176/tkinter-canvas-zoom-move-pan
# Advanced zoom example. Like in Google Maps.
# It zooms only a tile, but not the whole image. So the zoomed tile occupies
# constant memory and not crams it with a huge resized image for the large zooms.
# import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

=======


#### https://stackoverflow.com/questions/41656176/tkinter-canvas-zoom-move-pan

# Advanced zoom example. Like in Google Maps.
# It zooms only a tile, but not the whole image. So the zoomed tile occupies
# constant memory and not crams it with a huge resized image for the large zooms.
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep
import os


>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
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
<<<<<<< HEAD
    def __init__(self, mainframe, path):
        ''' Initialize the main Frame '''
        ttk.Frame.__init__(self, master=mainframe)
        # self.master.title('Zoom with mouse wheel')
=======
    def __init__(self, mainframe, path,fidpath):
        ''' Initialize the main Frame '''
        ttk.Frame.__init__(self, master=mainframe)        
        self.master.title('Zoom with mouse wheel')
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
        # Vertical and horizontal scrollbars for canvas
        vbar = AutoScrollbar(self.master, orient='vertical')
        hbar = AutoScrollbar(self.master, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')
<<<<<<< HEAD
=======
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
        # Create canvas and put image on it
        self.canvas = tk.Canvas(self.master, highlightthickness=0,
                                xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()  # wait till canvas is created
        vbar.configure(command=self.scroll_y)  # bind scrollbars to the canvas
        hbar.configure(command=self.scroll_x)
<<<<<<< HEAD
        # Make the canvas expandable
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
=======
        
        # # Make the canvas expandable
        # self.master.rowconfigure(0, weight=0)
        # self.master.columnconfigure(0, weight=0)
        
        # Give a minimum size to the canvas
        self.CS=800
        self.master.grid_columnconfigure(0,minsize=self.CS)
        self.master.grid_rowconfigure(0, minsize=self.CS)
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
        # Bind events to the Canvas
        self.canvas.bind('<Configure>', self.show_image)  # canvas is resized
        self.canvas.bind('<ButtonPress-1>', self.move_from)
        self.canvas.bind('<B1-Motion>',     self.move_to)
        self.canvas.bind('<MouseWheel>', self.wheel)  # with Windows and MacOS, but not Linux
        self.canvas.bind('<Button-5>',   self.wheel)  # only with Linux, wheel scroll down
        self.canvas.bind('<Button-4>',   self.wheel)  # only with Linux, wheel scroll up
<<<<<<< HEAD
        self.image = Image.open(path)  # open image
        self.width, self.height = self.image.size
        self.imscale = 1.0  # scale for the canvaas image
        self.delta = 1.3  # zoom magnitude
        # Put image into container rectangle and use it to set proper coordinates to the image
        self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)
        # # Plot some optional random rectangles for the test purposes
=======
        self.canvas.bind('<Double-Button-1>', self.clic_pixel)
        self.image = Image.open(path)  # open image
        print(self.image)
        self.fid = Image.open(path)  # open image
        print(self.fid)
        self.width, self.height = self.image.size
        self.imscale = 1.0  # scale for the canvaas image
        self.delta = 1.3  # zoom magnitude
        
        # Put image into container rectangle and use it to set proper coordinates to the image
        self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)
        
        
        # Plot some optional random rectangles for the test purposes
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
        # minsize, maxsize, number = 5, 20, 10
        # for n in range(number):
        #     x0 = random.randint(0, self.width - maxsize)
        #     y0 = random.randint(0, self.height - maxsize)
        #     x1 = x0 + random.randint(minsize, maxsize)
        #     y1 = y0 + random.randint(minsize, maxsize)
        #     color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
        #     self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, activefill='black')
<<<<<<< HEAD
        self.show_image()
=======
        
        # create right frame
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=0, column=2)
        
        self.button = ttk.Button(self.frame, text="ok",command=self.master.destroy)
        self.button.grid(row=0)
        
        # Create cross frame
        
                
        # display transparent fid mark
        # tkfid=ImageTk.PhotoImage(self.fid)
        # tk.Label(self.frame, image=tkfid).grid()
        
        
        self.show_image()
        # self.draw_cross()
        
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362

    def scroll_y(self, *args, **kwargs):
        ''' Scroll canvas vertically and redraw the image '''
        self.canvas.yview(*args, **kwargs)  # scroll vertically
        self.show_image()  # redraw the image
<<<<<<< HEAD
=======
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362

    def scroll_x(self, *args, **kwargs):
        ''' Scroll canvas horizontally and redraw the image '''
        self.canvas.xview(*args, **kwargs)  # scroll horizontally
        self.show_image()  # redraw the image
<<<<<<< HEAD
=======
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362

    def move_from(self, event):
        ''' Remember previous coordinates for scrolling with the mouse '''
        self.canvas.scan_mark(event.x, event.y)
<<<<<<< HEAD
=======
        print(event.x, event.y)
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362

    def move_to(self, event):
        ''' Drag (move) canvas to the new position '''
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.show_image()  # redraw the image
<<<<<<< HEAD

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
=======
        

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        print("\nzoom +/-")
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
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
<<<<<<< HEAD
        self.show_image()
=======
        
        self.show_image()
        
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362

    def show_image(self, event=None):
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
<<<<<<< HEAD
=======
        
        print('x2 - x1 = ',int(x2 - x1))
        print('y2 - y1 = ',int(y2 - y1))
        
        print(self.canvas.winfo_width(),self.canvas.winfo_height())
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
            x = min(int(x2 / self.imscale), self.width)   # sometimes it is larger on 1 pixel...
            y = min(int(y2 / self.imscale), self.height)  # ...and sometimes not
            image = self.image.crop((int(x1 / self.imscale), int(y1 / self.imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
<<<<<<< HEAD
            imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(imageid)  # set image into background
            self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection


if __name__ =='__main__':
    
    lieu = 'maison'
    disque=''
    
    if lieu == 'maison':
        disque = 'J'
    elif lieu == 'musee':
        disque ='F'
    

    Path = r'{}:\2_SfM_READY_photo_collection\Burundi_1981-82\GAPP\test6\01_CanvasSized\cornerToCheck'.format(disque)
    img = os.listdir(Path)[0]
    print(img)
    # path = 'doge.jpg'  # place path to your image here
    root = tk.Tk()
    app = Zoom_Advanced(root, path=Path+'/'+img)
    root.mainloop()
=======
            imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), 
                                               max(bbox2[1], bbox1[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(imageid)  # set image into background
            self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection
            print(self.canvas.bbox(image))
            
            # self.canvas.create_rectangle(x1,y1,x,y,fill='orange')
            print(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]))
            
        # print('\nbbox = ',bbox)
        # print('bbox1 = ',bbox1)
        # print('bbox2 = ',bbox2)
        # # self.draw_cross(True)
        # print("m=",min(self.canvas.winfo_width(),self.canvas.winfo_height()))

        
    def clic_pixel(self, event):
        ''' left clic on image'''
        print("\ndouble clic")
        
        
        bbox1 = self.canvas.bbox(self.container)  # get image area
        # Remove 1 pixel shift at the sides of the bbox1
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        
        x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
            x = min(int(x2 / self.imscale), self.width)   # sometimes it is larger on 1 pixel...
            y = min(int(y2 / self.imscale), self.height)  # ...and sometimes not
            
        
        x0,y0=int(max(bbox2[0], bbox1[0])), int(max(bbox2[1], bbox1[1]))
        
        scale = self.imscale # echelle de l'image fr
        print("size=",self.image)
        
        # x1,y1=(self.canvas.winfo_width(),self.canvas.winfo_width()) # taille de la fenetre fr
        
        # x,y = event.x,event.y # clic position
        # print(x,y)
        
        
        color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
        # self.canvas.create_rectangle(x0,y0 ,x0+2500*scale,y0+2500*scale,fill=color) 
        
        # lorsque le coins en haut a gauche est visible ou collé au bord gauche de la fenetre fr
        
        # ax=x0-x1
        # ay=y0-y1
        # bx=ax+2500*scale
        # by=ay+2500*scale
        # print("position image ?",ax,ay ,bx,by)
        # print(x,y)
        # print("x1,y1=",x1,y1)
        # print(x2,y2)
        # print('echelle = ',scale)
        # # self.canvas.create_rectangle(ax,ay,bx,by,fill=color)
        # if x1 > 0 and y1 >0:
        #     self.canvas.create_oval(x0+event.x-2,y0+event.y-2,x0+event.x+2,y0+event.y+2,fill='red')
        #     print("poin coord 1= ", x0+event.x,y0+event.y)
        # else:
        #     cx,cy=ax,ay
        #     self.canvas.create_oval(cx+event.x-2,cy+event.y-2,cx+event.x+2,cy+event.y+2,fill='red')
        #     print("poin coord 2= ", x+event.x,y+event.y)
            
            
        #TODO
        a=1
    
    # def draw_cross(self,event=None):
    #     w=self.canvas.winfo_width()
    #     h=self.canvas.winfo_height()
    #     self.cross = [self.canvas.create_oval(0, 0, w,h,outline='red'),
    #                   self.canvas.create_line(0, 0, w,h, fill='red'),
    #                   self.canvas.create_line(0, w,h,0, fill='red')]
        
        
        def display_fid(self,event=None):
            imagetk = ImageTk.PhotoImage(self.fid.resize((int(x2 - x1), int(y2 - y1))))
            imageid = self.canvas.create_image(anchor='nw', image=imagetk)
            
        
        
if __name__ == '__main__':
    # OOOOOOOOOOOSSSSSSSSSSSKKKOOOOOOOUUUUUUUR https://www.tcl.tk/
    Path = r'D:\ENSG_internship_2022\Burundi_1981-82\test7\01_CanvasSized\cornerToCheck'
    img = os.listdir(Path)[0]
    PathFid = r'D:\ENSG_internship_2022\Burundi_1981-82\Fid_mark_template'
    fid=os.listdir(PathFid)[1]
  
    
    path = r'{}\{}'.format(Path,img) # place path to your image here
    fidpath=r'{}\{}'.format(PathFid,fid) # place path to your fiducial mark here
    
    root=tk.Tk()
    app = Zoom_Advanced(root, path=path,fidpath=fidpath)
    root.mainloop()
>>>>>>> 241fc1badaef28a582e68fb4d8ee9cf2acac6362
