import pandas as pd

def do():
    data = pd.read_json("result.json")
    for index, row in data.iterrows():
        row['defi'] = filter(lambda s : s.lower().islower(), row['defi'])
        row['defi'] = "; ".join(row['defi'])
    with open("output.txt", 'w') as f:
        for index, row in data.iterrows():
            f.write(row['word'])
            f.write(": ")
            f.write(row['defi'])
            f.write("\n")
