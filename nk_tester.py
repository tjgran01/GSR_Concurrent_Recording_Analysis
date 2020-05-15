import neurokit2 as nk
import pickle
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def load_data(data_fpath="./exports/par2.1_finger.csv"):

    data = pd.read_csv(data_fpath)
    return data

def main():

    data = load_data()
    print(data.columns)

    eda = nk.eda_phasic(nk.standardize(data["GSR_Skin_Conductance(uS)"]),  sampling_rate=128)

    eda["events"] = data["Timestamp_Marks"] - 5

    eda.plot()
    plt.show()

    eda.to_csv("./exports/par2.1_finger_decomposed.csv")

if __name__ == "__main__":
    main()
