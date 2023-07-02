'''
********************************************************************************
*                                                                              *
* Project Start Date: 06/20/2023                                               *
* Project End Date: 07/1/2023                                                  *
*                                                                              *
* License: https://opensource.org/license/mit/                                 *
*                                                                              *
* Programmed By: Joseph R. Shumaker                                            *
*                                                                              *
* Purpose: This project was made as a reference library for some of my         *
* Co-Workers at the LRC (Learning Resource Center) where we hope to use        *
* the data in this API wrapper to create a robot that points at the ISS.       *
* The code in this project is protected under the MIT Licencing Agreement      *
* and by using this software you agree not to break any laws reguarding        *
* communications with the application server or the abuse of such services.    *
*                                                                              *
* All code seen below is my original work and all information regarding the    *
* use of library-specific methods and attributes were learned directly from    *
* the libraries' documentation.                                                *
*                                                                              *
* If you have any questions or would like to get in contact with me, my email  *
* and phone number is listed below...                                          *
*                                                                              *
* Phone: (805) 701 - 3171                                                      *
*                                                                              *
* Email: josephshumaker11@gmail.com                                            *
*                                                                              *
********************************************************************************
'''

import urllib.request
import json 
import time
import pandas
import plotly.express as px
import os
import wikipedia
from simple_term_menu import TerminalMenu

'''
urllib.request: Used to probe HTTPS for JASON Data
Documentation: 

json: Used to parse the Data from urllib
Documentation:

time: Used for intervals in the ISS recording
Documentation:

pandas: Used to parse 
Documentation:

plotly.express: 
Documentation:

os: 
Documentation:

wikipedia: 
Documentation:

simple_term_menu: 
Documentation:
'''

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

class ISSPlus:

    def credits(self):
        file = open("credits.txt", "r")
        print(file.read())
        file.close()
        options = ["GitHub", "Licence", "Documentation", "Return"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        Logic_Check = lambda x: options[menu_entry_index] == options[x] 
        if(Logic_Check(0)):
            os.system('clear')
            print("https://github.com/s5y-ux")
            return_val = input()
            os.system('clear')
            self.credits()
        elif(Logic_Check(1)):
            file = open("LICENSE.txt", "r")
            print(file.read())
            file.close()
            return_prompt = input()
            os.system('clear')
            self.credits()
        elif(Logic_Check(2)):
            print("Coming Soon")
            return_prompt = input()
            os.system('clear')
            self.credits()
        elif(Logic_Check(3)):
            self.ScreenPrompt()


    def GatherData(self, url_parameter):
        response = urllib.request.urlopen(url_parameter)
        result = json.loads(response.read())
        return(result)

    def TrackISS(self):
        Intervals = int(input("[Enter Second Intervals for Recording]>: "))
        print("Recording will take {0} minutes, are you sure?".format(round(Intervals/60)))
        Procedure_Logic = str(input("[Y/N]>: "))
        Data = [[],[],[]]
        i = 0
        for count in range(Intervals):
            result = self.GatherData("http://api.open-notify.org/iss-now.json")
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

    def AstroGather(self):
        os.system('clear')
        options = list()
        result = self.GatherData("http://api.open-notify.org/astros.json")
        for key, value in enumerate(result['people']):
            options.append(value['name'] + ", "+ value['craft'])
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if(options[menu_entry_index]):
            try:
                print(wikipedia.summary(options[menu_entry_index]))
            except:
                print("Data Unavailable")
        exit_procedure = str(input("Exit? [Y/N]>: "))
        if(exit_procedure.upper() == "YES" or exit_procedure.upper() == "Y"):
            self.ScreenPrompt()
        else:
            self.AstroGather()

    def Astronaut(self, color):
        file = open("Astronaut.txt", "r")
        print(color + file.read() + bcolors.ENDC)
        file.close()

    def MainMenu(self):
        options = ["Tack ISS", "Learn about Astronauts", "Exit Progam", "Library Info"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if(options[menu_entry_index] == options[0]):
            self.TrackISS()
        elif(options[menu_entry_index] == options[1]):
            self.AstroGather()
        elif(options[menu_entry_index] == options[2]):
            os.system('clear')
            return()
        elif(options[menu_entry_index] == options[3]):
            os.system('clear')
            self.credits()

    def ScreenPrompt(self):
        os.system('clear')
        print(bcolors.BOLD + "Welcome To s5y's ISS Recorder" + bcolors.ENDC)
        self.Astronaut(bcolors.BOLD)
        self.MainMenu()


if __name__ == '__main__':
    a = ISSPlus()
    a.ScreenPrompt()