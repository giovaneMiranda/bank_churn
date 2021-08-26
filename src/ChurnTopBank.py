import json
import pickle
import inflection


class ChurnTopBank(object):
    def __init__(self):
        self.home_path = '/home/giovane/pythonProject/bank_churn'
        self.standard_scaler_credit = pickle.load(open(self.home_path + '/parameter/standard_scaler_credit.pkl', 'rb'))
        self.min_max_scaler_tenure = pickle.load(open(self.home_path + '/parameter/min_max_scaler_tenure.pkl', 'rb'))
        self.min_max_scaler_age = pickle.load(open(self.home_path + '/parameter/min_max_scaler_age.pkl', 'rb'))
        self.min_max_scaler_salary = pickle.load(open(self.home_path + '/parameter/min_max_scaler_salary.pkl', 'rb'))
        self.min_max_scaler_geo_salary = pickle.load(
            open(self.home_path + '/parameter/min_max_scaler_geo_salary.pkl', 'rb'))
        self.min_max_scaler_geo_credit = pickle.load(
            open(self.home_path + '/parameter/min_max_scaler_geo_credit.pkl', 'rb'))
        self.min_max_scaler_geo_balance = pickle.load(
            open(self.home_path + '/parameter/min_max_scaler_geo_balance.pkl', 'rb'))
        self.min_max_scaler_balance = pickle.load(open(self.home_path + '/parameter/min_max_scaler_balance.pkl', 'rb'))
        self.encoding_label_geo = pickle.load(open(self.home_path + '/parameter/encoding_label_geo.pkl', 'rb'))
        self.encoding_label_gender = pickle.load(open(self.home_path + '/parameter/encoding_label_gender.pkl', 'rb'))

    def data_cleaning(self, df_churn):
        cols_old = df_churn.columns
        snake_case = lambda x: inflection.underscore(x)
        cols_new = list(map(snake_case, cols_old))

        # renomeando colunas
        df_churn.columns = cols_new

        return df_churn

    def feature_engineering(self, df_churn):
        # creating geography median salary
        df_churn['geo_median_salary'] = df_churn.groupby('geography')['estimated_salary'].transform('median')

        # creating geography median Credit Score
        df_churn['geo_median_cred'] = df_churn.groupby('geography')['credit_score'].transform('median')

        # creating geography median balance
        df_churn['geo_median_balc'] = df_churn.groupby('geography')['balance'].transform('median')

        # variable filtering
        cols_drop = ['surname', 'customer_id']
        df_churn = df_churn.drop(cols_drop, axis=1)

        return df_churn

    def data_preparation(self, df_churn):
        # Standard
        df_churn['credit_score'] = self.standard_scaler_credit.fit_transform(df_churn[['credit_score']].values)

        # Rescaling

        # tenure
        df_churn['tenure'] = self.min_max_scaler_tenure.fit_transform(df_churn[['tenure']].values)

        # age
        df_churn['age'] = self.min_max_scaler_age.fit_transform(df_churn[['age']].values)

        # estimated salary
        df_churn['estimated_salary'] = self.min_max_scaler_salary.fit_transform(df_churn[['estimated_salary']].values)

        # geo_median_salary
        df_churn['geo_median_salary'] = self.min_max_scaler_geo_salary.fit_transform(
            df_churn[['geo_median_salary']].values)

        # geo_median_cred
        df_churn['geo_median_cred'] = self.min_max_scaler_geo_credit.fit_transform(df_churn[['geo_median_cred']].values)

        # geo_median_balc
        df_churn['geo_median_balc'] = self.min_max_scaler_geo_balance.fit_transform(
            df_churn[['geo_median_balc']].values)

        # balance
        df_churn['balance'] = self.min_max_scaler_balance.fit_transform(df_churn[['balance']].values)

        # Enconding

        # Label Enconding geography
        df_churn['geography'] = self.encoding_label_geo.fit_transform(df_churn['geography'])

        # Label Enconding gender
        df_churn['gender'] = self.encoding_label_gender.fit_transform(df_churn['gender'])

        # variables select
        df_churn.drop(['row_number', 'geo_median_salary'], axis=1, inplace=True)

        cols_select = ['credit_score', 'age', 'tenure', 'balance', 'num_of_products', 'estimated_salary',
                       'geography', 'is_active_member']

        return df_churn[cols_select]

    def get_classification(self, model, df_original, df_precessed):
        # classification
        label = model.predict_proba(df_precessed)

        # merger with df_original
        df_original['churn_proba'] = label[:, 1]

        return json.dumps(df_original.to_dict(orient='records'))