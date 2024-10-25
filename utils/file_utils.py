import pandas as pd

def load_data(filepath):
    df = pd.read_excel(filepath)
    names = df['Names'].tolist()
    return names