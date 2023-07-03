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
* The code in this project is protected under the MIT Licensing Agreement      *
* and by using this software you agree not to break any laws regarding         *
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
Documentation: https://urllib3.readthedocs.io/en/stable/user-guide.html

json: Used to parse the Data from urllib
Documentation: https://docs.python.org/3/library/json.html

time: Used for intervals in the ISS recording
Documentation: https://docs.python.org/3/library/time.html

pandas: Used to parse data for use in plotly (Could have used standard dictionaries but, better practices yk?)
Documentation: https://pandas.pydata.org/docs/

plotly.express: Graphing Utility. Needed for mapbox as far as I know.
Documentation: https://plotly.com/python-api-reference/

os: Will change to subprocess in future iterations but in the meantime lets boogie
Documentation: https://docs.python.org/3/library/os.html

wikipedia: Used for processing data according to the astronauts currently in space.
Documentation: https://wikipedia.readthedocs.io/en/latest/

simple_term_menu: Used for the terminal menu.
Documentation: https://pydigger.com/pypi/simple-term-menu
'''

#Used as a simple way to access colors in string concatenation "bcolors.attribute"
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

#Current class for main program, will change to library in future versions
class ISSPlus:

    #Way to access credits. License, GitHub, Docs, and return
    def credits(self):

        #Opens the credits so I don't flood the program with ASCII
        file = open("credits.txt", "r")

        #Prints the contents
        print(file.read())

        #Closes the file
        file.close()

        #Options for the Terminal Menu
        options = ["GitHub", "License", "Documentation", "Return"]

        #Variable for the terminal menu
        terminal_menu = TerminalMenu(options)

        #Used to check for different options by the user
        menu_entry_index = terminal_menu.show()

        #Logic check function for seeing if a menu object is selected or not
        Logic_Check = lambda x: options[menu_entry_index] == options[x] 

        #Control flow for different options according to array index for, "options" variable
        if(Logic_Check(0)):

            #Clears CLI
            os.system('clear')

            #Prints my GitHub
            print("https://github.com/s5y-ux")

            #Used to return to, "credits" selection
            print("Press enter to return...")
            return_val = input()

            #Once again clears CLI for Credits. Might go back and fix but soy perezoso
            os.system('clear')
            self.credits()

        #Option for "License" (Assuming you didn't change the options variable 🤭)
        elif(Logic_Check(1)):

            #Used to open the Licensing
            file = open("LICENSE.txt", "r")

            #Prints the license
            print(file.read())

            #Closes the File
            file.close()

            #Used to return to, "credits" selection
            print("Press enter to return...")
            return_prompt = input()

            #Once again clears CLI for Credits. Might go back and fix but soy perezoso
            os.system('clear')
            self.credits()

        #Option for "Documentation" (Assuming you didn't change the options variable 🤭)
        elif(Logic_Check(2)):

            #This will eventually print the Documentation page on GitHub
            print("Coming Soon")

            #Used to return to, "credits" selection
            print("Press enter to return...")
            return_prompt = input()

            #Once again clears CLI for Credits. Might go back and fix but soy perezoso
            os.system('clear')
            self.credits()

        #Used to return to Main Screen
        elif(Logic_Check(3)):
            self.ScreenPrompt()


    #Shorthand for gathering API data through URL. Parameter is specific Jason Data
    def GatherData(self, url_parameter):

        #Pushes url_parameter to request
        response = urllib.request.urlopen(url_parameter)

        #Parses and stores JSON data in result variable
        result = json.loads(response.read())

        #Returns the result as Dictionary
        return(result)

    #Method for Actually tracking ISS (Will come back to this)
    def TrackISS(self):

        #Used to set Intervals (Logging ISS)
        Intervals = int(input("[Enter Second Intervals for Recording]>: "))

        #Time estimate for the recording
        print("Recording will take {0} minutes, are you sure?".format(round(Intervals/60)))

        #Variable to verify if you want to continue with recording
        Procedure_Logic = str(input("[Y/N]>: "))

        #If Procedure Logic variable is not "yes" we return to Main Screen
        if(Procedure_Logic.lower() != y or Procedure_Logic.lower() != yes):
            self.ScreenPrompt()

        #Multi Dimensional list to store our latitude, longitude, and period on plotly
        Data = [[],[],[]]

        #Holder for our intervals
        i = 0

        #For loop that will call the API every second 
        for count in range(Intervals):

            #Calls API to result
            result = self.GatherData("http://api.open-notify.org/iss-now.json")

            #Stores location from API
            location = result["iss_position"]

            #Stores latitude to multidimensional array 
            Data[0].append(float(location['latitude']))

            #Stores Longitude to multidimensional array 
            Data[1].append(float(location['longitude']))

            #Stores interval for playback
            Data[2].append(i)

            #Increments Interval
            i += 1

            #Timer for interval (1 Second)
            time.sleep(1)

        #Variable to store data-frame with the respective key value pairs referencing multi dimensional array
        grabber = pandas.DataFrame({"lat": Data[0], "lon": Data[1], "second":Data[2]})

        #Uses data for plotly/mapbox scatter chart
        fig = px.scatter_mapbox(grabber, lat="lat", lon="lon", animation_frame="second")

        #Changes the figure layout (Will add map customization in the near future)
        fig.update_layout(
            mapbox_style="white-bg",

            #Used to store map overlay. Will be adding JSON file for maps and selection through term menu
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

        #Sets the margins of the map
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        #Displays the plotly map via local web-server
        fig.show()

    #Method used to gather astronaut data
    def AstroGather(self):

        #Clears the command prompt
        os.system('clear')

        #Used as a holder for enumeration over the data
        options = list()

        #Gathers the JSON data from the API
        result = self.GatherData("http://api.open-notify.org/astros.json")

        #Enumerates over the people in the result
        for key, value in enumerate(result['people']):

            #Stores attributes name and value in the options array
            options.append(value['name'] + ", "+ value['craft'])

        #Used as a variable for menu selection in CLI
        terminal_menu = TerminalMenu(options)

        #Used as selection reference in terminal menu library
        menu_entry_index = terminal_menu.show()

        #Logic Cheeeeeck 🤗
        #If the Wikipedia Article Exists...
        if(options[menu_entry_index]):
            try:

                #Print the Article
                print(wikipedia.summary(options[menu_entry_index]))

            #However, if there is an exception...    
            except:

                #Tell the CLI the Data is Unavailable
                print("Data Unavailable")

        #Ask if you wanna exit
        exit_procedure = str(input("Exit? [Y/N]>: "))

        #I used upper this time for some reason, Just roll with it
        #If yes in any form is returned...
        if(exit_procedure.upper() == "YES" or exit_procedure.upper() == "Y"):

            #Go to main menu
            self.ScreenPrompt()

        #Otherwise
        else:

            #Return to the Astronauts
            self.AstroGather()

    #Used to print the Astronaut ASCII art to the CLI
    def Astronaut(self, color):

        #Opens the file under read perms
        file = open("Astronaut.txt", "r")

        #Prints the data in the selected color parameter
        print(color + file.read() + bcolors.ENDC)

        #Closes the file
        file.close()


    #Used as the main menu terminal menu
    def MainMenu(self):

        #Again we have the options
        options = ["Tack ISS", "Learn about Astronauts", "Exit Program", "Library Info"]

        #Variable used to store the menu options
        terminal_menu = TerminalMenu(options)

        #Is used to store the selected menu item
        menu_entry_index = terminal_menu.show()

        #I will probably replace this with a lambda function next time I open the code

        #Logic for option 0 "Track ISS" (Assuming you didn't change the options variable 🤭)
        if(options[menu_entry_index] == options[0]):

            #If press Track ISS, you track the ISS 🥴
            self.TrackISS()
        elif(options[menu_entry_index] == options[1]):

            #I think you get how this works so ill omit the rest of the comments
            self.AstroGather()
        elif(options[menu_entry_index] == options[2]):
            os.system('clear')
            return()
        elif(options[menu_entry_index] == options[3]):
            os.system('clear')
            self.credits()

    #Used as main menu screen
    def ScreenPrompt(self):

        #Clears the CLI
        os.system('clear')

        #Displays the Header
        print(bcolors.BOLD + "Welcome To s5y's ISS Recorder" + bcolors.ENDC)

        #Prints the ASCII art to the screen
        self.Astronaut(bcolors.BOLD)

        #Shows the main terminal menu
        self.MainMenu()


if __name__ == '__main__':
    a = ISSPlus()

    #Initial main menu method call
    a.ScreenPrompt()