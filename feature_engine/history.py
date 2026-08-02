import pandas as pd


class HistoryEngine:

    def __init__(self, dataframe):
        """
        Stores the UFC dataframe once.
        """

        self.df = dataframe.copy()

        self.df["date"] = pd.to_datetime(
            self.df["date"]
        )


    def get_history(
        self,
        fighter,
        before_date=None
    ):

        history = self.df[
            (self.df["R_fighter"] == fighter) |
            (self.df["B_fighter"] == fighter)
        ].copy()


        if before_date is not None:

            before_date = pd.to_datetime(before_date)

            history = history[
                history["date"] < before_date
            ]


        history = history.sort_values(
            "date",
            ascending=False
        )

        return history.reset_index(drop=True)