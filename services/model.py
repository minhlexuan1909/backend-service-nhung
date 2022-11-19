import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

LIGHT_THRESHOLD = 30

def init_knn_model() -> None:
    df = pd.read_csv("services/data.csv")
    df.drop(labels=["crop"], axis=1, inplace=True)
    X = df.drop(labels="pump", axis=1)
    y = df["pump"]
    global __KNN
    __KNN = KNeighborsClassifier(weights='distance', leaf_size=8, p=1, algorithm='auto', n_neighbors=7)
    __KNN.fit(X.values, y)


def can_turn_on_pump(moisture: float, temp: float):
    labels = __KNN.predict([[moisture, temp]])
    return bool(labels[0])


def can_turn_on_light(light: float):
    return light <= LIGHT_THRESHOLD
