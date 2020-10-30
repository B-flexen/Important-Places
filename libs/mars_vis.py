import requests
import seaborn as sns
from matplotlib.figure import Figure
import io
import PIL

sns.set_style("darkgrid") #sets seaborn plot style

#Define API get requests
def get_mars_weather(API_key):
    params = {'api_key':API_key, 'feedtype':'json', 'ver':'1.0'}
    URL = "https://api.nasa.gov/insight_weather/?"
    response = requests.get(URL, params)
    data = response.json()
    
    
    if response.status_code != 200:
        raise Exception(("Error: " + str(response.status_code)))
    
    else:
        return(data)
    
def get_mars_photo(API_key):
    URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
    params = {'api_key':API_key}
    response = requests.get(URL, params=params)
    
    if response.status_code != 200:
        raise Exception(("Error: " + str(response.status_code)))

    image_URL = response.json()["latest_photos"][1]["img_src"]
    image_data = requests.get(image_URL, stream=True)
        
    if image_data.status_code != 200:
        raise Exception(("Error: " + str(response.status_code)))
    
    image = io.BytesIO(image_data.content)
    
    return PIL.Image.open(image)


def get_mars_figure(api_key):
    data = get_mars_weather(api_key)
    max_temp = []
    min_temp = []
    av_temp = []
    sol = []
    for i in data:
        if not (i.isdigit()):
            break
        mn = data[i]["AT"]["mn"]
        mx = data[i]["AT"]["mx"]
        av = data[i]["AT"]["av"]
        sol.append(int(i))
        min_temp.append(mn)
        max_temp.append(mx)
        av_temp.append(av)

    fig = Figure(figsize=[4,3], dpi=70)
    sub = fig.add_subplot(111)
    sub.plot(sol, max_temp, marker='o', label = "maximum")
    sub.plot(sol, min_temp, marker='o', label = "minimum")
    sub.plot(sol, av_temp, marker='o', label = "average")
    sub.legend()
    sub.set_xlabel("Sol")
    sub.set_ylabel("Temperature ( $^{\circ}$C)")

    return fig

