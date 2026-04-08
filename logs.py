import os
import pandas as pd
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        file_path = "logs.csv"
        now = datetime.now()

        if os.path.exists(file_path):
            try:
                current_logs = pd.read_csv(file_path)
                new_id = current_logs.shape[0]
            except Exception:
                new_id = 0
        else:
            new_id = 0

        row = pd.DataFrame([{
            "id": new_id,
            "pc_username": os.getlogin(),
            "function_name": func.__name__,
            "Date in date.month.year": now.strftime("%d-%m-%Y"),
            "Time": now.strftime("%H:%M:%S")
        }])

        row.to_csv(
            file_path,
            mode="a",
            header=not os.path.exists(file_path),
            index=False
        )

        print(f"Данные записаны в {file_path}")
        return result

    return wrapper
