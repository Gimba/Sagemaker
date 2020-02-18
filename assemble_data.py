import numpy as np
import pandas as pd


with open('frame_energies.csv','r') as f:
    energies = []
    flag = False
    for line in f.readlines():
        if 'DELTA' in line:
            flag = True
            continue
        if flag:
            line = line.split(',')
            line = [ll.replace('\n','') for ll in line]
            if len(line) > 1:
                energies.append(line[-1])

    energies = np.asarray(energies)

    metrics = pd.read_csv('bindingsite_metrics.dat', nrows=len(energies), header=0, delim_whitespace=True)
    metrics['#Frame'] = energies
    metrics.rename(columns={'#Frame':'energies'}, inplace=True)
    metrics.to_csv('training_data.csv',sep=',',header=None,index=None)
