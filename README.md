# pvlib-prometheus-exporter
A Prometheus exporter for various items computed by pvlib at a given location.
Note that this is both a promethus client and exporter

* https://pypi.org/project/pvlib/
* https://pvlib-python.readthedocs.io/en/latest/

* https://en.wikipedia.org/wiki/Solar_irradiance

Inputs to model:
    Not time variant:
        location, array tilt, array orentation, array spacing,
        panel make/model, inverter make/model,
    Time Variant:
        time, free air temperature, back-of-panel temperature, wind speed
        rain accumulation over time (? for soiling model)
metrics to output:
    dni: direct normal irradiance (i.e. something tracking sun's position)
    dhi: diffuse horizontal irradiance
    ghi: global horizontal irradiance dhi + dni*cos(z)
    z: solar zenith angle, angle between local normal and sun (cos of this scales dni to ghi)
    poa: plane of array irradiance (https://pvlib-python.readthedocs.io/en/latest/auto_examples/plot_ghi_transposition.html)
Power reported in W/m^2


# development environment
using the system python3
``` bash
cd ~/git/pvlib-prometheus-exporter
virtualenv -p python3 .venv
source .venv
pip install pvlib prometheus-client
pip install matplotlib PyQT5
```
