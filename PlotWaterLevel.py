#! /usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------
from   sys                 import argv
from   os                  import path
from   json                import load as jload
from   pandas              import DataFrame
from   matplotlib.pyplot   import subplots
from   matplotlib.ticker   import ScalarFormatter
#----------------------------------------------------

# Load arguments
name_json_file_in = argv[1]


#----------------------------------------------------
# Load content of GEOjson file with json module
with open(name_json_file_in) as h_json:
    z_table = jload(h_json)


# Convert into pandas dataframe
data = DataFrame(z_table['data'])


#----------------------------------------------------
# Plot with matplotlib
fig, ax = subplots(figsize=(16,9))

ax.errorbar(data['time'], 
            data['water_surface_height_above_reference_datum'], 
            yerr = data['water_surface_height_uncertainty'],
            color = 'darkblue',
            ecolor = 'darkred',
            ls = '-',
            marker = '.',
            alpha = .8,
            label = 'Mean dispersion = %4.2f cm)'%(data['water_surface_height_uncertainty'].mean()*100))


ax.set_xlabel('Time')
ax.xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.set_ylabel('Water Surface Height (m)')
ax.legend(loc = 'best')
ax.grid()
fig.autofmt_xdate()

#----------------------------------------------------
# Save plot
name_png_file_out = path.splitext(name_json_file_in)[0]+'.png'
fig.savefig(name_png_file_out)