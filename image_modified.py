# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 10:36:35 2020

@author: Dong Li
"""

from skimage import io
import os
import numpy as np
import matplotlib.pyplot as plt
import powerlaw
from scipy import asarray as ar,exp
from scipy.optimize import curve_fit
import scipy.stats as stats
import random as rd


print(18%3)