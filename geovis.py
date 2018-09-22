#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:33:03 2018

@author: ttle
"""
from bokeh.io import show, output_notebook, output_file
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper
)
from bokeh.plotting import figure
from bokeh.palettes import BuPu3 as palette

with open(r'concessions.geojson', 'r') as f:
    geo_source = GeoJSONDataSource(geojson=f.read())
    
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world_source = GeoJSONDataSource(geojson=world.to_json())

p = figure(title="Liberia Concessions", plot_width=800, plot_height=500, 
           x_range=(-12,-7), y_range=(4,10),
           toolbar_location="below")

patches = p.patches('xs', 'ys', fill_alpha=0.9, 
                    fill_color={'field': 'aiddataID', 'transform': LinearColorMapper(palette=palette)}, 
                    line_color='white', line_width=0.5, source=geo_source)

info = HoverTool(renderers=[patches])
info.tooltips = [('Title', '@title'), ('Company', '@country')]
p.add_tools(info)

patches = p.patches('xs', 'ys', fill_alpha=0.2, 
          fill_color={'field': 'pop_est', 'transform': LinearColorMapper(palette=palette)}, 
          line_color='black', line_width=0.5, source=world_source)


show(p)