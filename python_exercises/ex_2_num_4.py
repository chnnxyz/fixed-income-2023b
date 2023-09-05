import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from nelson_siegel_svensson import NelsonSiegelSvenssonCurve
from nelson_siegel_svensson.calibrate import calibrate_nss_ols

if __name__ == "__main__":
    data = pd.read_csv('data/usyield.csv')
    print(data.dtypes)
    t = data['date']
    calibrate_nss_ols()