#!/usr/bin/env python
""" Computes the clearsky ghi and poa for a single day for given system/location/time
"""
import pandas as pd
import matplotlib.pyplot as plt

from pvlib import irradiance
from pvlib import pvsystem
from pvlib.pvsystem import PVSystem, FixedMount
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

# Hardcoding the inverter and module data for now
iq7 = pd.Series({'Vac': 240, 'Pso': 1.581551, 'Paco': 240.0, 'Pdco': 246.615662, 'Vdco': 32.0, 'C0': -5.6e-05, 'C1': -0.000389,
 'C2': 0.031523, 'C3': -0.048795, 'Pnt': 0.072, 'Vdcmax': 37.0, 'Idcmax': 7.706739, 'Mppt_low': 27.0, 'Mppt_high': 37.0,
 'CEC_Date': '10/15/2018', 'CEC_Type': 'Utility Interactive'}, name="IQ7")
sil330 = pd.Series({'Technology': 'Mono-c-Si', 'Bifacial': 0, 'STC': 330.344, 'PTC': 309.3, 'A_c': 1.63, 'Length': 1.64,
 'Width': 0.94, 'N_s': 63, 'I_sc_ref': 9.84, 'V_oc_ref': 42.2, 'I_mp_ref': 9.52, 'V_mp_ref': 34.7, 'alpha_sc': 0.001771,
 'beta_oc': -0.112252, 'T_NOCT': 42.7, 'a_ref': 1.548435, 'I_L_ref': 10.04273, 'I_o_ref': 1.45e-11, 'R_s': 0.286932,
 'R_sh_ref': 582.379162, 'Adjust': 5.53333, 'gamma_r': -0.369, 'BIPV': 'N', 'Version': 'SAM 2020.2.29 r3', 'Date': '11/25/2020'}, 
 name="sil 330")
sil330["b"] = 0.05 # needed to get the model class to be happy

# This represents one inverter/module pair 
system = pvsystem.PVSystem(surface_tilt=23, surface_azimuth=180, 
    module_parameters=sil330, 
    inverter_parameters=iq7,
    temperature_model_parameters=TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass'])

location = Location(name="hill country", latitude=30, longitude=-98, tz='CST6CDT', altitude=300)

# The model chain has all the time/weather invariant things
mc = ModelChain(system, location)


# the weather input includes all time varrying things -- including irradiance
times = pd.date_range('11-11-2021 0600', freq='10min', periods=12*6, tz=location.tz)
# Assume clearsky to get max output
weather = location.get_clearsky(times) # clearsky ghi, dni, dhi

# Now add on air temps, wind speed, and preciptable water
# Put in 1cm for precipitable water since getting that data might be hard
# but ... https://landweb.modaps.eosdis.nasa.gov/cgi-bin/ATM/ATMbrowse.cgi
weather['temp_air'] = 25 # C
weather['wind_speed'] = 5 # kph
weather['precipitable_water'] = 1 # cm

mc.run_model(weather)
mc.results.ac.plot()
