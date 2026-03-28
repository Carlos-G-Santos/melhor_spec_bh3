# start = primeira linha (ex: surface  520) end = penultima linha
def load_dados(arquivo, start, end):

    import pandas as pd
    import numpy as np
    
    with open(arquivo, 'r') as f:
        lines = f.readlines()

    dados = [line.strip().split() for line in lines[start:end]]
    df = pd.DataFrame(dados)
    df.columns = ['energy','flux', 'error']
    df = df.iloc[1:-1]
    df = df.astype(float)
    
    return df