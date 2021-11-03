#!/usr/bin/env python3

import asyncio
import time
import datetime
from prometheus_client import start_http_server, Gauge


prefix="solar_model"
port=9400
power = Gauge(f"{prefix}_power", "Output from model")

start_http_server(port)

location=[-90, 30, 200] # longitude, lattitude, altitude (m)

while True:
    for target in targets:
        rc = ping(target)
        if rc is None:
            lost.labels(target).inc()
        elif rc is False:
            unresolved.labels(target).inc()
        else:
            pings.labels(target).observe(rc)

    time.sleep(5)
