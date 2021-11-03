# solar-model
A Prometheus exporter for available solar radiance at a given location.

* https://pypi.org/project/pvlib/
* https://pvlib-python.readthedocs.io/en/latest/

Inputs to model:
    time, location, array tilt, array orentation, array spacing,
    panel make/model, inverter make/model,
    free air temperature, back-of-panel temperature, wind speed
    rain accumulation over time (? for soiling model)
metrics to output:
    pvlib_dni: direct normal irradiance
    pvlib_

pipenv install --dev
 
 - or -

docker build -t solar-model .