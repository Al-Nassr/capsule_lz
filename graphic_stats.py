import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class GraphicStatistics:
    def __init__(self, argum):
        self.defen = pd.read_csv(argum)

    def histogram(self):
        # усредняем данные по штатам и выбираем 8 случайных
        df = (
            self.defen.groupby("STATE", as_index=False)[
                ["FEDERAL_REVENUE", "STATE_REVENUE", "LOCAL_REVENUE"]
            ]
            .mean()
            .sample(8, random_state=1)
        )

        states = df["STATE"].reset_index(drop=True)
        values = df[["FEDERAL_REVENUE", "STATE_REVENUE", "LOCAL_REVENUE"]]

        # переводим в проценты
        percents = values.div(values.sum(axis=1), axis=0) * 100

        x = np.arange(len(states))
        fig, ax = plt.subplots(figsize=(18, 10))

        colors = ["royalblue", "seagreen", "darkorange"]
        labels = ["Федеральный бюджет", "Бюджет штата", "Местный бюджет"]

        bottom = np.zeros(len(states))
        for i, col in enumerate(percents.columns):
            bars = ax.bar(x, percents[col], bottom=bottom, color=colors[i], label=labels[i])
            ax.bar_label(bars, fmt="%.0f%%", label_type="center", color="white")
            bottom += percents[col]

        # таблица значений
        table = plt.table(
            cellText=np.round(values.values, 1),
            rowLabels=states,
            colLabels=["Федеральный", "Штат", "Местный"],
            cellLoc="center",
            loc="bottom",
            bbox=[0, -0.45, 1, 0.35]
        )
        table.set_fontsize(10)

        ax.set_xticks(x)
        ax.set_xticklabels(states, fontsize=12)
        ax.set_ylim(0, 100)
        ax.set_ylabel("%", fontsize=14)
        ax.set_title("Средние бюджеты школ по штатам (в %)", fontsize=18)

        ax.legend(loc="upper right", bbox_to_anchor=(1, 1), frameon=False, fontsize=12)
        plt.subplots_adjust(bottom=0.35)
        plt.show()
