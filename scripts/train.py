import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def load_and_map_data(data_path: str):
    df = pd.read_csv(data_path, sep=';')
    df.columns = df.columns.str.lower()
    
    medu_map = {
        0: 'none',
        1: 'primary education (4th grade)',
        2: '5th to 9th grade',
        3: 'secondary education',
        4: 'higher education'
    }

    fedu_map = {
        0: 'none',
        1: 'primary education (4th grade)',
        2: '5th to 9th grade',
        3: 'secondary education',
        4: 'higher education'
    }

    travel_time_map = {
        1: '<15 min',
        2: '15 to 30 min',
        3: "30 min to 1 hour",
        4: '>1 hour'
    }

    study_time_map = {
        1: '<2 hours',
        2: '2 to 5 hours',
        3: '5 to 10 hours',
        4: '>10 hours'
    }

    famrel_map = {
        1: 'very bad',
        2: 'bad',
        3: 'average',
        4: 'good',
        5: 'excellent'
    }

    freetime_map = {
        1: 'very low',
        2: 'low',
        3: 'average',
        4: 'high',
        5: 'very high'
    }

    gooout_map = {
        1: 'very low',
        2: 'low',
        3: 'average',
        4: 'high',
        5: 'very high'
    }

    dalc_map = {
        1: 'very low',
        2: 'low',
        3: 'average',
        4: 'high',
        5: 'very high'
    }

    walc_map = {
        1: 'very low',
        2: 'low',
        3: 'average',
        4: 'high',
        5: 'very high'
    }

    health_map = {
        1: 'very bad',
        2: 'bad',
        3: 'average',
        4: 'good',
        5: 'very good'
    }

    df['medu'] = df['medu'].map(medu_map)
    df['fedu'] = df['fedu'].map(fedu_map)
    df['traveltime'] = df['traveltime'].map(travel_time_map)
    df['studytime'] = df['studytime'].map(study_time_map)
    df['famrel'] = df['famrel'].map(famrel_map)
    df['freetime'] = df['freetime'].map(freetime_map)
    df['goout'] = df['goout'].map(gooout_map)
    df['dalc'] = df['dalc'].map(dalc_map)
    df['walc'] = df['walc'].map(walc_map)
    df['health'] = df['health'].map(health_map)

    return df

def split_datasets(df: pd.DataFrame):
    X = df.drop(columns=["g3"])
    y = df["g3"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

    # DictVectorizer for encoding
    dv = DictVectorizer(sparse=False)
    X_train_encoded = dv.fit_transform(X_train.to_dict(orient="records"))
    X_val_encoded = dv.transform(X_val.to_dict(orient="records"))

    return X_train_encoded, X_val_encoded, y_train, y_val, dv

def train_and_eval(X_train, X_val, y_train, y_val):
    model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=10, min_samples_split=2, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_val)
    metrics = {
        "Accuracy": accuracy_score(y_val, y_pred),
        "Precision": precision_score(y_val, y_pred, average='macro'),
        "Recall": recall_score(y_val, y_pred, average='macro'),
        "F1 Score": f1_score(y_val, y_pred, average='macro')
    }

    print("Final Model Performance")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    return model, metrics

def save_model(model, dv, filename='dtree_model.pkl'):
    with open(filename, 'wb') as f_out:
        pickle.dump((model, dv), f_out)
    print(f"Model and DV saved to {filename}")

def main():
    path = '../data/student-mat.csv'
    df = load_and_map_data(path)
    X_train, X_val, y_train, y_val, dv = split_datasets(df)
    model, metrics = train_and_eval(X_train, X_val, y_train, y_val)
    save_model(model, dv)


if __name__ == "__main__":
    main()