import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[0:3]
    # OR
    return employees.head(3)
    # OR
    return employees.iloc[0:3]
