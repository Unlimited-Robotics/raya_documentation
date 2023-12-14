#!/bin/bash

# Install sphinx-wagtail-theme
if [ -d "sphinx-wagtail-theme/node_modules" ]; then
    cd sphinx-wagtail-theme
    npm run build
else
    # The 'node_modules' directory exists, so execute the commands
    cd sphinx-wagtail-theme || exit 1

    # Upgrade Python packages
    /usr/bin/python3 -m pip install --upgrade -r requirements.txt

    # Clean up
    make clean
    make clean-frontend

    # Install and build frontend if 'node_modules' exists
    npm ci
    npm run build
    /usr/bin/python3 -m pip install -e sphinx-wagtail-theme/.
fi