import pandas as pd


def main(csv_file_path: str) -> None:
    df = pd.read_csv(csv_file_path)
    
    # print(df)

    df_grouped = df.groupby(['item_1', 'item_2']).sum()

    # print(df_grouped)

    df_grouped['win_rate'] = df_grouped['win'] / (df_grouped['win'] + df_grouped['lose'])
    
    print(df_grouped)


if __name__ == '__main__':
    csv_file_path = './item_purchase_history.csv'

    main(csv_file_path)