#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imageio
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from pathlib import Path


# In[2]:


class videoplayer(ttk.Frame):
    def __init__(self, parent, video):
        ttk.Frame.__init__(self, parent)
        
        #load video to array
        self.video = imageio.get_reader(video)
        self.framelist = []
        try:
        #N.B. imageino sometimes has issues reading the last frame of a file, hence this try function.
            for im in self.video:
            #N.B. this is a very slow way of handling videos, but its the only method I've
            #found that alows me to pause, play and restart. This is something to work
            #on in future
                self.framelist.append(ImageTk.PhotoImage(Image.fromarray(im)))

        except RuntimeError:
            self.video.close()
        
        #set key perameters
        self.isplaying = True
        self.frame_no = 0
        self.play_button_text = tk.StringVar()
        
        #screen - displays current frame
        self.im = self.framelist[0]
        self.screen = ttk.Label(self, image=self.im)
        self.screen.image = im
        self.screen.grid(row=0, columnspan=2)

        #progress bar
        self.bar = ttk.Progressbar(self, length = self.framelist[0].width(), maximum = len(self.framelist))
        self.bar.grid(row=1, columnspan=2)

        

        self.play = ttk.Button(self, command=self.playpausebutton, textvariable=self.play_button_text)
        self.play.grid(row=2, column=0, sticky="W")
        self.play_button_text.set("Pause")
        self.restart = ttk.Button(self, command=self.restartbutton, text="restart")
        self.restart.grid(row=2, column=1, sticky="W")
        
        self.columnconfigure(0, minsize = self.play.winfo_width())
        
        self.update_video()
        
    def update_video(self):
    #updates the frames of the video player and is called in __init__(). You should never directly access this method
    
        if self.isplaying == True and self.frame_no < len(self.framelist):
            self.new_vid_frame = self.framelist[self.frame_no]
            self.frame_no += 1
            self.screen.config(image = self.new_vid_frame)
            self.bar.config(value = self.frame_no)
        self.after(50, self.update_video)
            
    def playpausebutton(self):
        if self.isplaying == False:
            self.isplaying = True
            self.play_button_text.set("Pause")
                
        elif self.isplaying == True:
            self.isplaying = False
            self.play_button_text.set("Play")
                    
    def restartbutton(self):
        self.frame_no = 0
        self.bar.config(value = self.frame_no)

