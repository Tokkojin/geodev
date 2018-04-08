import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


locations = pd.read_csv('locations.tsv', sep = '\t')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
geometry = [Point(xy) for xy in zip(locations.longitude, locations.latitude)]
crs = {'init': 'epsg:4326'}
points = gpd.GeoDataFrame(locations, crs=crs, geometry=geometry)
points.plot(color='blue')


points.plot(marker='*', color='green', markersize=5);
points = points.to_crs(world.crs)

base = world.plot(color = 'white', edgecolor = 'black')
points.plot(ax = base, marker = 'o', color = 'blue', markersize = 5)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_aspect('equal')

world.plot(ax=ax, color='blue', edgecolor='black', lw = 0.5)
points.plot(ax=ax, marker='o', color='red', markersize=5)
plt.show();

from bokeh.plotting import figure, save