import pickle
import pandas as pd
from flask import Flask, request, Response
from src.ChurnTopBank import ChurnTopBank

model = pickle.load(open('/home/giovane/pythonProject/bank_churn/model/model_rf_tuned.pkl', 'rb'))

app = Flask(__name__)


@app.route('/topbank/classificator', methods=['POST'])
def topbank_classificator():
    test_json = request.get_json()

    if test_json:

        if isinstance(test_json, dict):
            df_raw = pd.DataFrame(test_json, index = [0])

        else:
            df_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        pipeline = ChurnTopBank()

        # data_cleaning
        df_cleaned = pipeline.data_cleaning(df_raw)

        # feature_engineering
        df_features = pipeline.feature_engineering(df_cleaned)

        # data_preparation
        df_precessed = pipeline.data_preparation(df_features)

        # classification
        df_labeled = pipeline.get_classification(model, df_raw, df_precessed)

        return df_labeled

    else:
        return Response('{}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run('127.0.0.1')

