import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
df = pd.DataFrame(pd.read_excel("sample1.xlsx"))
read_file = pd.read_excel("sample1.xlsx")
read_file.to_csv("sample1.csv", header=True, index=False)
df = pd.DataFrame(pd.read_csv("sample1.csv"))
print(df.head())

def algo(datas,r):
    print(datas)

    data = pd.read_csv('sample1.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = DecisionTreeClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]