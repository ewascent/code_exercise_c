#!/bin/bash
# install dev only libraries for linbting, building, and testing
python -m pip install --user --upgrade setuptools wheel
pip install nose pylint
