
import utils.params as params
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from utils.file import get_absolute_path
import pandas
import os
if __name__ == "__main__":
    if not os.path.exists(get_absolute_path("/home/hosseinamiri/Research/geopol-dev/results/params.top.json")):
        # df2 = params.get_dataframe_from_json("/home/hosseinamiri/Research/geopol-dev/params.init.json")
        # df3 = params.get_dataframe_from_json("/home/hosseinamiri/Research/geopol-dev/params.pool.aws.json")
        df = params.get_dataframe_from_json("/home/hosseinamiri/Research/geopol-dev/params.pool.json")
        # df5 = params.get_dataframe_from_json("/home/hosseinamiri/Research/geopol-dev/params.pool.terminated.json")
        # df6 = params.get_dataframe_from_json("/home/hosseinamiri/Research/geopol-dev/params.pool1.json")
        # df = pandas.concat([df2, df3, df4, df5, df6])
        df.to_csv(get_absolute_path("data/all_params.csv"))
    else:
        print("Top params file exists!")
        df = params.get_dataframe_from_json(get_absolute_path("results/params.top.json"))
    df = df.drop(df.columns[0], axis=1)
    # normalize the data and scale it
    # remove the column if all the values are the same
    df = df.loc[:, (df != df.iloc[0]).any()]
    df = (df - df.min()) / (df.max() - df.min())
    # round the values to 2 decimal points
    df = df.round(2)

    df.to_csv(get_absolute_path("data/normalized.csv"))
    df.dropna(inplace=True)
    print(df.describe())
    print(df.corr())
    X = df.drop('score', axis=1) 
    y = df['score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    p_value = pearsonr(y_test, y_pred)
    print(mse)
    print(model.coef_)
    print(p_value)

    
    coefficients = pandas.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
    # absolute value of the coefficients
    coefficients['Coefficient'] = coefficients['Coefficient'].abs()
    # Sort the coefficients for better visualization
    coefficients.sort_values(by='Coefficient', ascending=False, inplace=True)
    # print(coefficients.head(10))
    print(coefficients.to_string().replace("properties.", ""))
    # print(coefficients[10:-10].to_string().replace("properties.", ""))
    # print(coefficients.tail(10))

