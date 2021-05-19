# Imporatant places whitepaper

This document gives a more in deapth description of the processes used in the Importand Places desktop app. The document focusses on the data processing and visualisation
elements of the project, rather than creating the GUI. The document is devided in to sections according to the real world locations the application is intended to represent.

## Tab 1 - Introduction
This tab contains text introducing the application and its purpose. It does not feature an visualisations.

## Tab 2 - The Colne valley
This Tab features two abstract visualisations of the weather conditions in the Colne Valley in West Yorkshire. The data is represented as a colourscheme made up of 6 colour blocks.
The first visualisation uses live data (updated once every ... seconds)
The second visualisation is a video displaying the weather data (of the same type and in the same format) during 2019, recorded in 1-hour intervals. Data is presented at a rate of 1 hour per frame.

### windspeed and direction
wind direction and windspeed are represented by the hue and saturation of the colour in HSV colourspace. As such higher winds are represented by bolder colours. Varying the hue in HSV
colourspace results in a cyclic colour map, meaning slight changes in wind direction will always result in a smooth transition between colours.

Windspeed is normalised between 0

### solar elevation


### cloudcover

### temperature

### rainfall


### season
One of four colours representing the season is selected depending on the date.

season | date | colour | reason
-------|------|-------|---------------------------------------------------------
winter | bla | White | to represent the frost and snow
spring | bla | Green | to represent the new plant growth
summer | bla | Orange | to represent the warm summer sun
autumn | bla | Purple | to represent the colour of the heather on the moors in late summer and early autumn
