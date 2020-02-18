#! /usr/bin/env python

# Copyright (c) 2020 Martin Rosellen

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
