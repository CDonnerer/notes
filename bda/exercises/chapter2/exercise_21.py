"""Exercise 12: Simple hierarchical model

The file pew research center june elect wknd data.dta3 has data from Pew
Research Center polls taken during the 2008 election campaign. You can read
these data into R using the read.dta() function (after first loading the
foreign package into R).

Your task is to estimate the percentage of the (adult) population in each state
(excluding Alaska, Hawaii, and the District of Columbia) who label themselves
as ‘very liberal,’ following the general procedure that was used in Section 2.7
to estimate cancer rates, but using the binomial and beta rather than Poisson
and gamma distributions.

But you do not need to make maps; it will be enough to make scatterplots,
plotting the estimate vs. Barack Obama’s vote share in 2008 (data available at
2008ElectionResult.csv, readable in R using read.csv()).

Make the following four graphs on a single page:
• Graph proportion very liberal among the survey respondents in each state vs.
  Obama vote share—that is, a scatterplot using the two-letter state
  abbreviations (see state.abb() in R).
• Graph the Bayes posterior mean in each state vs. Obama vote share.
• Repeat graphs (a) and (b) using the number of respondents in the state on the
  x-axis.

This exercise has four challenges: first, manipulating the data in order to get
the totals by state; second, estimating the parameters of the prior
distribution; third, doing the Bayesian analysis by state; and fourth, making
the graphs.
"""
import os

import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt


#  Alaska, Hawaii, and the District of Columbia

DATA_DIR = "../../data"
STATES_TO_EXCLUDE = ["alaska", "hawaii", "district of columbia", "washington dc"]


def _exclude_states(df, state_col="state"):
    df[state_col] = df[state_col].str.lower()
    df = df.loc[~df[state_col].isin(STATES_TO_EXCLUDE), :]
    return df


def load_poll_data():
    df = pd.read_stata(
        os.path.join(DATA_DIR, "pew_research_center_june_elect_wknd_data.dta")
    )
    df = _exclude_states(df)
    return df


def load_election_data():
    df = pd.read_csv(os.path.join(DATA_DIR, "2008ElectionResult.csv"))
    df = _exclude_states(df)
    return df


def posterior_mean_binom_beta(alpha, beta, y, n):
    """Posterior mean of binomial model with beta distribution prior"""
    return (alpha + y) / (alpha + beta + n)


def ideo_by_state(df):
    ideo_count = df.groupby(["state", "ideo"]).size()
    state_count = ideo_count.groupby("state").transform("sum")
    ideo_prop = ideo_count / state_count

    return pd.concat(
        [
            ideo_count.rename("count"),
            ideo_prop.rename("prop"),
            state_count.rename("total"),
        ],
        axis=1,
    )


def main():
    df_poll = load_poll_data()
    df_elec = load_election_data()

    ideo_prop = ideo_by_state(df_poll)

    very_liberal_prop = ideo_prop.loc[
        ideo_prop.index.get_level_values("ideo") == "very liberal"
    ]

    # estimate the prior
    df_elec["vote_Obama_frac"] = df_elec["vote_Obama_pct"] / 100.0

    # plt.hist(very_liberal_prop["prop"])

    lnspc = np.linspace(0, 0.25, 100)

    alpha, beta, loc, scale = stats.beta.fit(
        very_liberal_prop["prop"], floc=0, fscale=1
    )
    pdf_beta = stats.beta.pdf(lnspc, alpha, beta, loc=0, scale=1)
    # plt.plot(lnspc, pdf_beta, label="Beta")
    #
    # plt.show()

    def row_apply(row, alpha=alpha, beta=beta):
        return posterior_mean_binom_beta(
            alpha=alpha, beta=beta, y=row["count"], n=row["total"],
        )

    posterior_mean = very_liberal_prop.apply(row_apply, axis=1,)

    df = pd.merge(
        df_elec, posterior_mean.reset_index(), left_on="state", right_on="state"
    )

    from IPython import embed

    embed()


if __name__ == "__main__":
    main()
