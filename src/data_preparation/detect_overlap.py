import pandas as pd
import json
import codecs

la_govt_data_path = 'D:\\USC\\courses\\Fall_2018\\Data_mining\\project\\data\\LA_govt_2016-18_dataset.csv'
yelp_challenge_data_path = 'D:\\USC\\courses\\Fall_2018\\Data_mining\\project\\data\\yelp_dataset\\yelp_dataset~\\yelp_academic_dataset_business.json'

"""load the government data from csv file into dataframe"""
def load_la_govt_data(file):
    df = pd.read_csv(file)
    # here column 5 is city
    # column 0 is restaurant name
    print(len(df))
    df = df.loc[df['City'] == 'LOS ANGELES']
    df = df.rename(columns={'Zip': 'zip'})
    df = df.rename(columns={'Facility': 'name'})
    df = df['name'].str.lower().to_frame()
    print(len(df))
    return df

"""load the yelp challenge data from json file into dataframe"""
def load_yelp_challenge_data(file):
    with open(file,'rb') as f:
        data = pd.DataFrame(json.loads(line) for line in f)
    print(len(data))
    # # 9 - name
    # # 4 - city
    data = data['name'].str.lower().to_frame()
    data = data.rename(columns={'postal_code': 'zip'})
    # df = data.loc[data['City'] == 'Calgary']
    # print(len(df))
    return data

"""find overlap dataset"""
def find_overlap(la_govt_df, yelp_df):
    print("finding overlap...")
    # https: // stackoverflow.com / questions / 26921943 / pandas - intersection - of - two - data - frames - based - on - column - entries / 26921975
    s1 = pd.merge(la_govt_df, yelp_df, how='inner', on=['name'])
    print(len(s1))


if __name__ == '__main__':
    la_govt_df = load_la_govt_data(la_govt_data_path)
    yelp_df = load_yelp_challenge_data(yelp_challenge_data_path)
    find_overlap(la_govt_df, yelp_df)