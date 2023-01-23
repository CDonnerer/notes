"""Simple bivariate stats
"""

import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


def generate_data(n_samples=1_000):
    return pd.DataFrame({
        "f1": np.random.normal(0, 2.1, n_samples),
        "f2": np.random.normal(10, 0.07, n_samples)
    })


def bivariate_stats(
    df_left, 
    df_right,
    *,
    left_prefix="left_",
    right_prefix="right_"
):

    stats1 = df_left.describe().transpose().add_prefix(left_prefix)
    stats2 = df_right.describe().transpose().add_prefix(right_prefix)

    df_bivar = pd.concat([stats1, stats2], axis=1)

    ttest_stats = ttest_ind(df_left, df_right)
    df_bivar["ttest_statistic"] = ttest_stats.statistic
    df_bivar["ttest_pvalue"] = ttest_stats.pvalue

    cols = [
        f"{prefix}{stat}"
        for stat in ("count", "mean", "std")
        for prefix in (left_prefix, right_prefix)
    ] + ["ttest_statistic", "ttest_pvalue"]

    return df_bivar.loc[:, cols]

def main():
    df1 = generate_data()
    df2 = generate_data()
    df3 = bivariate_stats(df1, df2)

    print(df3)

if __name__ == "__main__":
    main()