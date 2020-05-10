import pandas as pd
import datetime
import os

class TimestampMatcher(object):
    def __init__(self, shimmer_dir="./analysis/shimmer_data/", log_dir="./data/logs/trev/"):
        self.shimmer_dir = shimmer_dir
        self.log_dir = dir

        print(os.getcwd())

        print(os.listdir(self.shimmer_dir))


tm = TimestampMatcher()