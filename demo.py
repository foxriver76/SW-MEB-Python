#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:54:01 2021

@author: moritz
"""

from lib.swmeb_plus import SWMEB_Plus
from skmultiflow.data.hyper_plane_generator import HyperplaneGenerator

# Initialize kernelized swmeb
swmeb = SWMEB_Plus(batch_size=1)

# Initialize a new data stream
stream = HyperplaneGenerator()

for i in range(10000):
    stream.next_sample()
    swmeb.append(stream.current_sample_x)