import urllib.request
import json 
import time
import pandas
import plotly.express as px
import os
import wikipedia
from simple_term_menu import TerminalMenu

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def TrackISS():
    Intervals = int(input("[Enter Second Intervals for Recording]>: "))
    print("Recording will take {0} minutes, are you sure?".format(round(Intervals/60)))
    Procedure_Logic = str(input("[Y/N]>: "))
    Data = [[],[],[]]
    i = 0
    for count in range(Intervals):
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        location = result["iss_position"]
        lat = location['latitude']
        lon = location['longitude']
        lat = float(lat)
        lon = float(lon)
        Data[0].append(lat)
        Data[1].append(lon)
        Data[2].append(i)
        i += 1
        time.sleep(1)

    grabber = pandas.DataFrame({"lat": Data[0], "lon": Data[1], "second":Data[2]})

    fig = px.scatter_mapbox(grabber, lat="lat", lon="lon", animation_frame="second")
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
          ])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def AstroGather():
    os.system('clear')
    options = list()
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    for key, value in enumerate(result['people']):
        options.append(value['name'] + ", "+ value['craft'])
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if(options[menu_entry_index]):
        print(wikipedia.summary(options[menu_entry_index]))
    exit_procedure = str(input("Exit? [Y/N]>: "))
    if(exit_procedure.upper() == "YES" or exit_procedure.upper() == "Y"):
        ScreenPrompt()

def Astronaut(color):
    file = open("Astronaut.txt", "r")
    print(color + file.read() + bcolors.ENDC)
    file.close()

def MainMenu():
    options = ["Tack ISS", "Learn about Astronauts", "Exit Progam"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if(options[menu_entry_index] == options[0]):
        TrackISS()
    elif(options[menu_entry_index] == options[1]):
        AstroGather()
    elif(options[menu_entry_index] == options[2]):
        os.system('clear')
        return()

def ScreenPrompt():
    os.system('clear')
    print(bcolors.BOLD + "Welcome To s5y's ISS Recorder" + bcolors.ENDC)
    Astronaut(bcolors.BOLD)
    MainMenu()


if __name__ == '__main__':
    ScreenPrompt()