#!/usr/bin/env python

import tkinter as tk
import argparse
from tkinter import ttk
from libs.videoplayer_widget import videoplayer
from libs.moors_vis import *
from libs.mars_vis import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


#commandline argument parser
parser = argparse.ArgumentParser()

parser.add_argument("-api_1", "--open_weather_api", help = "Enter a valid OpenWeather API key")
parser.add_argument("-api_2", "--nasa_api", help = "Enter a valid NASA open data API key")
#parser.add_argument("")

args = parser.parse_args()

ow_api = args.open_weather_api
nasa_api = args.nasa_api

#set up app

root = tk.Tk() 
root.title("Tab Widget") 
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text ='Intro') 
tab_control.add(tab2, text ='Colne Valley')
tab_control.add(tab3, text ='Mars')
tab_control.add(tab4, text ='Hull')
tab_control.pack(expand = 1, fill ="both")


#Tab 1 - introduction page

intro_text = """I want to tell you about myself through the places that are important to me. They will tell you about my background, and my thougths of the future. I have chosen three locations that are significant to me for different reasons. For each of these locations I have taken live or recent data and produced a visulisation. Some are more traditional scientific graphs and charts, others are more artistic. I hope to show how important place is to us as individuals, and the power of data to understand and represent those places. Please select one of the tabs above to continue."""

intro_label = ttk.Label(tab1, text = intro_text, wraplength=700, justify="center")
intro_label.grid(column = 0, row = 0, padx = 20, pady = 20, columnspan=2) 

#Tab 2 - Colne Valley page

marsden_text = """I grew up in the Colne Valley in West Yorkshire on the edge of the Pennines. It a beutiful landscape made only more wonderful by its dynamic nature. I love the changing of the seasons; The colour of the heather on the moors, seeing the hills on a clear day, or only being able to see the bottom in low cloud. I even quite like the rain. But I also notice the changes in the weather year on year. Climate change is becoming more tangible. The dangers it will bring ever more worrying.
The image to the top right shows the colour scheme based on the current weather conditions in the colne valley and is updated every 20 seconds. As the weather fluctuates only slightly over such short timescales the colour changes are likely to be difficult to perceive. Bellow is an explanation of each of the different colours.
Top left: Wind. The hue is dictated by the wind direction and the saturation being dictated by the speed.
Top centre: Solar elevation. depends on the elevation of the sun with the colourmap roughly corresponding the usual colour of the sky.
Top right: Cloud cover. A grey scale with white corresponding to 0% cloud cover and dark grey to 100% cloud cover.
Bottom left: Temperature. A diverging colour scale with the coolest temperatures being represented by blue and the warmest being represented by red.
Bottom centre: Rainfall. A scale from white to dark blue, with white meaning no rainfall and the darkest blue representing heavy rain, i.e. more than 4mm in the previous hour.
Bottom right: The seasons. This is one of four colours; White for winter, representing the frost and snow, green for spring representing the new growth of plants, a warm orange to represent the summer and purple representing the colour of the heather on the moors in early autumn.

The video shows the colour scheme based on the weather for the same place over all of 2019. Each frame is a 1 hour timestep and the video plays at 24fps; you see 1 day per second."""

moors_text_lab = ttk.Label(tab2, text = marsden_text, wraplength=500, justify="left")
moors_text_lab.grid(column = 0, row = 0, padx = 20, pady = 20)

try:
    im = ImageTk.PhotoImage(get_image(get_weather_data("Marsden", ow_api)))
    
except:
    im = ImageTk.PhotoImage(file='media/error.png')

colour_chart = ttk.Label(tab2, image=im)
 #keep a reference to the image (otherwise it is garbage collected)
colour_chart.grid(column = 1, row = 0, padx = 20, pady = 20)   

def update_colour_chart():
    try:
        new_im = ImageTk.PhotoImage(get_image(get_weather_data("Marsden", ow_api)))
        colour_chart.config(image=new_im)
        colour_chart.image = new_im
    except:
        print("running exception")
        new_im = ImageTk.PhotoImage(file='media/error.png')
        colour_chart.configure(image=new_im)
        colour_chart.image = new_im
        
    
    root.after(20000, update_colour_chart)
    
video_2019 = videoplayer(tab2, "media/2019_weather_colour.mp4")
video_2019.grid(column = 1, row = 1)

#Tab 3 - Mars page

mars_text = """I have always been fascinated by space; the wonder of the immense unknown and the sheer beauty of the small amount we can actually witness. This fascination led me to study astrophysics at university and continues to fuel my desire to work in the space sector. As space is a very big place, I have decided to focus just on mars for this application.
The graph to the right shows the maximum, minimum and average atmospheric temperatures on the surface of mars for each of the past 7 sols (martian days) as measured by the InSight lander. The dataset may occasionally miss data points for some sols, in which case the graph will only include the available data points.
The image in the bottom right is the most resent photograph taken by Curiosity rover that is available via NASA open data API.
"""

mars_text_lab = ttk.Label(tab3, text = mars_text, wraplength=500, justify="center")
mars_text_lab.grid(column = 0, row = 0, padx = 20, pady = 20)


#mars temperature plot
try:
    mars_temp_plot = FigureCanvasTkAgg(get_mars_figure(nasa_api), tab3)
    mars_temp_plot.get_tk_widget().grid(column=1, row=0)
except:
    im = ImageTk.PhotoImage(file='media/error.png')
    mars_temp_plot = ttk.Label(tab3, image=im)
    mars_temp_plot.image = im
    mars_temp_plot.grid(column=1, row=0)

#mars photo
try:
    mars_photo_im = get_mars_photo(nasa_api)
    mars_photo_im = mars_photo_im.resize((350, 250), Image.ANTIALIAS)
    mars_photo_im = ImageTk.PhotoImage(mars_photo_im)
except:
    mars_photo_im = ImageTk.PhotoImage(file='media/error.png')
    
mars_photo_lab = ttk.Label(tab3, image = mars_photo_im)
mars_photo_lab.image = mars_photo_im
mars_photo_lab.grid(column = 1, row = 1)

#Tab 4

hull_text = """For the last four years, I have lived and studied in the city of Hull. The city is situated on the Humber estuary and has been shaped by its connection to the sea. It has historically been central to the UK fishing industry and continues to be a significant freight and ferry port. The city centre is shaped by its maritime history; it has multiple quays in the city centre, even one of the main shopping centres is built on stilts above an old marina. One of my personal favourite places in the whole city is on the estuary bank, with the boats in the marina on one side and the wide estuary on the other.
This tab is still a work in progress. Eventually it will display real time tidal data, reflecting the maritime history of Hull and the importance that the Humber Estuary and Hull river still has for the city today.
"""

hull_lab = ttk.Label(tab4, text = hull_text, wraplength=700, justify="center")
hull_lab.grid(column = 0, row = 0, padx = 20, pady = 20, columnspan=2) 

#Launch app

update_colour_chart()
root.mainloop()





