import numpy as np
from numpy.linalg import norm
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from typing import TypeVar, Callable
dframe = TypeVar('pd.core.frame.DataFrame')
narray = TypeVar('numpy.ndarray')
import math
import json

def hello():
  return "Welcome to s21_puddles library"

###Week 4

def knn(table, target_list):

  distance_record = []
  n = len(table)

  for i in range(n):
    crowd_row = table.loc[i].to_list()
    crowd_numbers = crowd_row[:-1]
    choice = crowd_row[-1]
    d = euclidean_distance(target_list, crowd_numbers)
    distance_record += [[d,choice]]

  sorted_record = sorted(distance_record)
  return sorted_record
