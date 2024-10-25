import pandas as pd

def load_data(input_file_path):
    df = pd.read_excel(input_file_path)
    names = df['Names'].tolist()
    return names