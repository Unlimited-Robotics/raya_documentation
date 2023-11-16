#!/bin/bash

# Install requirements
apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip

/usr/bin/python3 -m pip install \
    docutils==0.18.1 \
    sphinx==7.1.2 \
    sphinx-copybutton==0.5.2 \
    sphinx-rtd-theme==1.3.0 \
    myst-parser==2.0.0

# Install PyRaya
python3 -m pip install -e /pyraya

rm -R /raya_documentation/docs/html/* /raya_documentation/docs/doctrees/*
sphinx-build -M html . /raya_documentation/docs
chown 1000:1000 -R /raya_documentation/docs