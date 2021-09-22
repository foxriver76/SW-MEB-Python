#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:54:01 2021

@author: moritz
"""

from lib.kernel_swmeb_plus import KernelSWMEB_Plus
from skmultiflow.data.hyper_plane_generator import HyperplaneGenerator

# Initialize kernelized swmeb
k_swmeb = KernelSWMEB_Plus(batch_size=1)

# Initialize a new data stream
stream = HyperplaneGenerator()

for i in range(10000):
    stream.next_sample()
    k_swmeb.append(stream.current_sample_x)