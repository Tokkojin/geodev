#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:29:45 2018

@author: ttle
"""

import pandas as pd
from shapely.geometry import Point

from bokeh.models import GeoJSONDataSource, LinearColorMapper, HoverTool

import geopandas as gpd
from bokeh.palettes import BuPu3 as palette
from bokeh.plotting import figure, save

# --- country borders
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
geo_source = GeoJSONDataSource(geojson=world.to_json())

# --- project locations
projects = pd.read_table('locations.tsv', sep = '\t')
geometry = [Point(xy) for xy in zip(projects.longitude, projects.latitude)]
crs = world.crs
projects_df = gpd.GeoDataFrame(projects, crs=crs, geometry=geometry)
project_source = GeoJSONDataSource(geojson=projects_df.to_json())

# --- create plot/figure
p = figure(title="Project Locations", plot_width=800, plot_height=500, 
           x_range=(0,100), y_range=(30,85),
           toolbar_location="below")

# --- map country borders / color by population
patches = p.patches('xs', 'ys', fill_alpha=0.7, 
          fill_color={'field': 'pop_est', 'transform': LinearColorMapper(palette=palette)}, 
          line_color='black', line_width=0.5, source=geo_source)

# --- plot project locations
circle = p.circle('x', 'y', source=project_source, color='black', size=2)

# --- create hovertool that displays info about project
project_info = HoverTool(renderers=[circle])
project_info.tooltips = [('Project ID', '@project_id'), ('Place', '@place_name'), 
                     ('Coordinates', '($x, $y)')]
p.add_tools(project_info)

# --- create hovertool that identifies country
country_info = HoverTool(renderers=[patches])
country_info.tooltips = [('Country Name', '@name'), ('Population Estimate', '@pop_est{0,0}')]
p.add_tools(country_info)

output = r"/Users/YOUR_NAME_HERE/Desktop/project_locations.html"
save(p, output)

