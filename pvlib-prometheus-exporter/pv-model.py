#!/usr/bin/env python

from pvlib import location
from pvlib import irradiance
import pandas as pd
from matplotlib import pyplot as plt
import types

site = location.Location(latitude=30, longitude=-98, tz='CST6CDT')
array = types.SimpleNamespace(**{
    'azimuth':180,
    'tilt':23.5
})

times = pd.date_range('11-6-2021', freq='30min', periods=24*2, tz=site.tz)
clearsky = site.get_clearsky(times) # clearsky ghi, dni, dhi
solar_position=site.get_solarposition(times=times)

# Use the get_total_irradiance function to transpose the GHI to POA
poa_irradiance = irradiance.get_total_irradiance(
    surface_tilt=array.tilt,
    surface_azimuth=array.azimuth,
    dni=clearsky['dni'],
    ghi=clearsky['ghi'],
    dhi=clearsky['dhi'],
    solar_zenith=solar_position['apparent_zenith'],
    solar_azimuth=solar_position['azimuth'])

ghi = clearsky['ghi']
poa = poa_irradiance['poa_global']
ghi2poa= poa/ghi
