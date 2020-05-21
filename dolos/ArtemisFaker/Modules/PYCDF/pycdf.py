"""
Copyright © Her Majesty the Queen in Right of Canada, 
as represented by the Minister of Statistics Canada, 2020
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
import math

def normalize(max, min, point):
    norm = (point - min) / (max - min)
    return norm

def binary(y_data: list, point: int, xdata: list):
    
    first = 0
    last = len(y_data) - 1
    
    while (first <= last):
        mid = (first + last) // 2
        if (point == y_data[mid]):
            return {xdata[mid] : y_data[mid]}
        else:
            if point < y_data[mid]:
                last = mid - 1
            else:
                first = mid + 1
                
    last = len(y_data) - 1
    found = False
    step = 0
    while not found:
        if (step + 1) < len(y_data):
            mid = (first + last) // 2
            if ((y_data[mid] < point) and (y_data[mid + 1] > point)):
                found = True
                return {xdata[mid] : y_data[mid], xdata[mid + 1] : y_data[mid + 1]}
            else:
                if point < y_data[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        else:
            raise IndexError("Iterations exceed total list size. \
                              Either the point does not exist, \
                              or the array is not normalized")
        step += 1

def interp(point: float, ui: float, uj: float, xi: float, xj: float) -> float:
    
    a = ((uj - point) / (uj - ui)) * xi
    b = ((point - ui) / (uj - ui)) * xj
    
    return a + b
