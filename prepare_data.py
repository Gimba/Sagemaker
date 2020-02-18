
from pathlib import Path
import pandas as pd


def main():

    data = pd.DataFrame()
    print(data.shape)
    for path in Path('.').rglob('training_data.csv'):
        data = data.append(pd.read_csv(path, header=None, index_col=None))
        print(data.shape)

    data -= data.min()
    data /= data.max()
    # shuffle data
    data = data.sample(frac=1)

    data.to_csv('training_bside_metrics_energy.csv', index=None, header=None)


if __name__ == '__main__':
    main()