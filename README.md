# ISS+
## Description
The "ISS+ Project" project is an exciting endeavor that aims to track the International Space Station (ISS) in real-time and visualize its location using Mapbox on Plotly. Additionally, the project utilizes Pandas data frames to efficiently store and manipulate JSON data retrieved through NASA's ISS API.

The project consists of several key components. Firstly, it employs the ISS API provided by NASA to fetch relevant information about the ISS, including its latitude, longitude, altitude, and other parameters. The API returns the data in JSON format, which is then processed and stored using Pandas data frames.

Using the obtained ISS data, the project dynamically updates and maps the current location of the ISS on a map using Mapbox and Plotly. Mapbox provides a comprehensive mapping platform that allows for interactive and visually appealing visualizations. Plotly, on the other hand, is a powerful graphing library that integrates seamlessly with Mapbox, enabling the creation of rich, interactive maps.

To implement the project, you would begin by setting up the necessary Python environment. Install the required libraries, including Pandas, Plotly, and Mapbox, using the appropriate package managers. Then, you would use the requests module to make HTTP requests to the NASA ISS API and retrieve the JSON data.

Once the JSON data is obtained, you would employ Pandas to create a data frame and store the relevant information in columns, such as latitude, longitude, and altitude. This data frame can be easily manipulated and analyzed, allowing for efficient processing of the ISS data.

Next, you would utilize Plotly and Mapbox to create an interactive map visualization. By providing the latitude and longitude data from the Pandas data frame, you can plot markers on the map representing the ISS's current location. The map can be customized with various features, such as zoom levels, map styles, and tooltips displaying additional information about the ISS.

To ensure the tracking is real-time, you can implement a loop that periodically requests updated ISS data from the NASA API and refreshes the map visualization accordingly. This way, users can observe the ISS's movement in near real-time on the map.

In summary, the "ISS+ Project" project combines the power of Pandas, Mapbox, and Plotly to track the ISS's location and visualize it on an interactive map. By utilizing the NASA ISS API, you can fetch real-time data, store it efficiently using Pandas data frames, and create dynamic visualizations that allow users to explore the ISS's trajectory and position.
## Screenshot
![Screenshot 2023-06-28 at 5 17 08 PM](https://github.com/s5y-ux/ISSPlus/assets/59636597/b5b8154e-1267-4ef5-abb7-a2dd7f2a0cd0)
