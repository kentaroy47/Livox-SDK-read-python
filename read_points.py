#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:15:57 2020

@author: ken
"""

import pptk
from utils import LivoxFileRead

# written out filename
data = LivoxFileRead("2020-06-11_17-38-30.lvx")
# Visualize with pptk
pptk.viewer(data[:,0:3], data[:, 3])
