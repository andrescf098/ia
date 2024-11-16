import pandas as pd
import yaml

with open("./Models/handwriting_recognition/202301111911/configs.yaml", 'r') as f:
    df = yaml.safe_load(f)

df = pd.DataFrame([df])
print(df.values.tolist())