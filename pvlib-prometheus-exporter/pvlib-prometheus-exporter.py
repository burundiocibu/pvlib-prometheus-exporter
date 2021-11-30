#!/usr/bin/env python3

import pandas as pd
import types

import asyncio
import time
import datetime
from prometheus_client import start_http_server, Gauge

prefix="pvlib_exporter"
port=9440
# array: index into array array
# obs: gih, dni, dhi, z, az, poa
irradiance = Gauge(f"{prefix}_clearsky", "Output from model", ['array','obs'])

from pvlib import pvsystem
invdb = pvsystem.retrieve_sam('CECInverter')
iq7=invdb.Enphase_Energy_Inc___IQ7_60_x_ACM_US__240V_
moddb = pvsystem.retrieve_sam(path="https://raw.githubusercontent.com/burundiocibu/SAM/develop/deploy/libraries/CEC%20Modules.csv") #'CECMod')
sil330 = moddb.Silfab_Solar_Inc__SIL_330BL

iq7 = pd.DataFrame({'Vac': '240',
 'Pso': 1.581551,
 'Paco': 240.0,
 'Pdco': 246.615662,
 'Vdco': 32.0,
 'C0': -5.6e-05,
 'C1': -0.000389,
 'C2': 0.031523,
 'C3': -0.048795,
 'Pnt': 0.072,
 'Vdcmax': 37.0,
 'Idcmax': 7.706739,
 'Mppt_low': 27.0,
 'Mppt_high': 37.0,
 'CEC_Date': '10/15/2018',
 'CEC_Type': 'Utility Interactive'})

sil330 = pd.DataFrame({
 'Technology': 'Mono-c-Si',
 'Bifacial': 0,
 'STC': 330.344,
 'PTC': 309.3,
 'A_c': 1.63,
 'Length': 1.64, # not in the database csv
 'Width': 0.94,  # not in the database csv
 'N_s': 63,
 'I_sc_ref': 9.84,
 'V_oc_ref': 42.2,
 'I_mp_ref': 9.52,
 'V_mp_ref': 34.7,
 'alpha_sc': 0.001771,
 'beta_oc': -0.112252,
 'T_NOCT': 42.7,
 'a_ref': 1.548435,
 'I_L_ref': 10.04273,
 'I_o_ref': 1.45e-11,
 'R_s': 0.286932,
 'R_sh_ref': 582.379162,
 'Adjust': 5.53333,
 'gamma_r': -0.369,
 'BIPV': 'N',
 'Version': 'SAM 2020.2.29 r3',
 'Date': '11/25/2020'})

start_http_server(port)



temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

mount = pvsystem.FixedMount(surface_tilt=23, surface_azimuth=180)

# This system uses micro-inverters so each array consists of 1 module and 1 inverter

location=[-90, 30, 200] # longitude, lattitude, altitude (m)

while True:

    time.sleep(5)
