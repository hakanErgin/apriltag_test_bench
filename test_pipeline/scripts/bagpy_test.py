#!/home/uware/projects/apriltags_ws/src/test_pipeline/env/bin/python3
import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np

b = bagreader("/home/uware/rosbags/2022-02-17-15-33-21.bag")

print(b.topic_table)