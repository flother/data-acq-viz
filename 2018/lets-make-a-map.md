---
title: Let's make a map with QGIS
date: 2018-02-23
layout: 2018
---

We're going to make a [choropleth map] showing people killed by police and other law enforcement agencies across the United States in 2015 and 2016. The result will look like this:

![](/img/per-1m.png)

Data sources
------------

We'll use three data sources. Download all three and unzip the ZIP file.

- [1:10m _Admin 1 – States, Provinces_][sp] from [Natural Earth] (a free source of geographical data useful for base layers)
- [The Counted data][tc] with extra latitude/longitude columns. The extra columns were added using [Geocodio]
- [US state populations][pp]. The population data was [scraped from Wikipedia] and then tidied up a little

Software
--------

To make the map we're going to use [QGIS], a high-quality geographic information system (GIS) that's free, open-source, and cross-platform. [Download and install QGIS]. (On Windows, use the _standalone installer_, not the network installer, and when you run the application make sure to use the version that includes GRASS.)

You might find QGIS has a steep learning curve so try the [official training manual] and [unofficial tutorials]. You can also find [tutorials on YouTube].

Creating the map
----------------

1. The 1:10m states and provinces data you downloaded from Natural Earth is named `ne_10m_admin_1_states_provinces.zip`. Unzip that to get a folder that contains [shapefile data], including a file named `ne_10m_admin_1_states_provinces.shp`.

1. Add that shapefile as a _vector_ layer (use the menu _Layer → Add Layer → Add Vector Layer..._).

1. This gives us a map of the world showing the borders of sub-national states and provinces. We want to filter this to show only the [48 contiguous states].

   Select the layer from the Layers Panel on the left-hand side of the main QGIS window. Open the Filter window (use the menu _Layer → Filter..._) and add the filter expression:

   ```sql
   "iso_a2" = 'US'
   AND
   name NOT IN ('Alaska', 'Hawaii')
   ```

   ![](/img/48-filter.png)

1. Now we have a map of the 48 contiguous states we want to use a projection that suits that geography. Open the project properties (use the menu _Project → Properties..._) and select the _CRS_ panel. Tick _Enable 'on the fly' CRS transformation (OTF)_ and then use the filter to select _US National Atlas Equal Area_.

   ![](/img/crs-filter.png)

   Now you have a map that looks like this (the colour may be different):

   ![](/img/projected-plain-map.png)

1. To set the scale to 1:12,000,000, type `1:12000000` into the _Scale_ text box in the toolbar at the bottom edge of the main QGIS window.

1. Next we want to add The Counted data as a layer. Use the _Layer → Add Layer → Add Delimited Text Layer..._) menu to add the `the-counted-geocoded.csv` data file as a layer.

   **Note**: If QGIS pops up a window asking you for a CRS, click _Cancel_ to use the default CRS, WGS 84 (aka EPSG:4326).

1. Now we can count the number of deaths that occurred in each state. Choose the _Vector → Analysis Tools → Count points in polygons_ menu item to do a vector join like this:

   ![](/img/count-points.png)

   Make sure to name the count field `NUM_DEATHS` and then click _Run_.

1. There's a new layer on the map named _Count_. Open the layer properties (_Layer → Properties..._) and select the _Style_ panel. Choose a graduated style using a sequential colour ramp ([ColorBrewer] will help you here), `NUM_DEATHS` as the data column and _Natural Breaks (Jenks)_ as the mode. Try five data classes. Click _Classify_ and then _OK_.

   ![](/img/layer-style.png)

1. This gives is an unnormalised map (absolute number of deaths per state) but we want a normalised map (number of deaths per 1,000,000 population). Add the final data source, `us-state-pop.csv`, containing US state population data (_Layer → Add Layer → Add Vector Layer..._)

1. We need to join the state population data to the _Count_ layer. Select the _Count_ layer, open its properties (_Layer → Properties..._), and choose the _Joins_ panel.

   Click the _+_ button to add a join, use _us-state-pop_ as the join layer, _state_ as the join field, and _name_ as the target field. Chose only the _population_ field to be joined, and use a blank custom field name prefix.

   ![](/img/layer-join.png)

1. Make sure the _Count_ layer is still selected and open its attribute table (_Layer → Open Attribute Table_). From the toolbar, click the _Open field calculator_ button --- it's probably second from the right, it looks like an abacus.

   From the field calculator, create a new decimal field named `deaths_p1m` using the expression `(NUM_DEATHS / population) * 1e6`

   ![](/img/field-calc.png)

1. By adding a new column 'editing mode' has been turned on. We won't need this again so turn it off by selecting the _Count_ layer in the _Layers Panel_ and clicking the _Toggle Editing_ button on the _Digitizing Toolbar_ near the top of the main QGIS window (it looks like a single yellow pencil). If QGIS prompts you to save the file, click _Save_.

1. To normalise the map we now need to go into the properties for the _Count_ layer (Layer → Properties). Make sure the _Style_ panel is selected. The column is set to `NUM_DEATHS`; change that to `deaths_p1m`, click _Classify_ and then _OK_.

  ![](/img/normalised-map.png)

1. We have a map, but it's missing a title and sub-title, legend, and source. This can all be done using a print composer. From the _Project_ menu choose _New Print Composer..._. From the _Layout_ menu in the new window you can add maps, labels (for titles and sources), and legends.

   Make sure to edit the legend so it's useful — use better text for the legend labels, remove unneeded legend entries, and so on. This can all be done using the _Legend Items_ section of the _Item Properties_ panel in the right-hand sidebar.

   The tutorial [Automating map creation with print composer atlas] will help guide you through this process.

  ![](/img/print-composer.png)

Alternatives to QGIS
--------------------

[ArcGIS] is used very widely in industry and government but it's expensive.

[Mapbox Studio] lets you create customised maps but it doesn't support data wrangling.

[Carto] provides let's you create thematic maps using data from cloud-based PostgreSQL databases.

R has [excellent support for geospatial data] but it can be difficult to get everything installed.

[D3.js] also has excellent support for geospatial data, but it's very low-level (that's both a positive and a negative).

  [sp]: http://www.naturalearthdata.com/downloads/10m-cultural-vectors/
  [tc]: http://dataviz.flother.is/2018/data/the-counted-geocoded.csv
  [pp]: http://dataviz.flother.is/2018/data/us-state-pop.csv

  [choropleth map]: https://en.wikipedia.org/wiki/Choropleth_map
  [Natural Earth]: http://www.naturalearthdata.com/
  [Geocodio]: https://geocod.io/
  [scraped from Wikipedia]: https://en.wikipedia.org/w/index.php?title=List_of_U.S._states_and_territories_by_population&oldid=825371767
  [QGIS]: https://www.qgis.org/
  [Download and install QGIS]: https://www.qgis.org/en/site/forusers/download.html
  [official training manual]: https://docs.qgis.org/2.18/en/docs/training_manual/index.html
  [unofficial tutorials]: http://www.qgistutorials.com/
  [tutorials on YouTube]: https://www.youtube.com/results?search_query=qgis+tutorials
  [shapefile data]: https://en.wikipedia.org/wiki/Shapefile
  [48 contiguous states]: https://en.wikipedia.org/wiki/Contiguous_United_States
  [ColorBrewer]: http://colorbrewer2.org/
  [Automating map creation with print composer atlas]: http://www.qgistutorials.com/en/docs/automating_map_creation.html
  [ArcGIS]: https://www.esri.com/arcgis/about-arcgis
  [Mapbox Studio]: https://www.mapbox.com/mapbox-studio/
  [Carto]: https://carto.com/
  [excellent support for geospatial data]: https://github.com/Robinlovelace/Creating-maps-in-R
  [D3.js]: https://medium.com/@mbostock/command-line-cartography-part-1-897aa8f8ca2c
