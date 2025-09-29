import pandas as pd

def dicts_to_dataframe(instances):
    """
    instances: list of dicts
    Return pandas DataFrame with columns sorted to keep consistent order.
    """
    if not instances:
        raise ValueError("No instances provided")
    df = pd.DataFrame(instances)
    # Ensure consistent column order (alphabetical) — important if pipeline expects fixed order.
    df = df.sort_index(axis=1)
    return df
