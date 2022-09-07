from wholeslidedata.iterators import create_batch_iterator
import numpy as np
from matplotlib import pyplot as plt
# from plot_utils import init_plot, plot_batch, show_plot
from wholeslidedata.samplers.utils import plot_batch_detection
import time
from pprint import pprint

# basic user config 
user_config = './user_config_detection.yml'

# mode of batch iterator
mode = 'training'

# number of cpus used to extract patches on multiple cores
cpus = 1

# create batch iterator via context manager
number_of_batches = 2
repeats=2
with create_batch_iterator(user_config=user_config, 
                           number_of_batches=number_of_batches,
                            mode=mode, 
                            cpus=cpus) as training_batch_iterator:
    print('hello')
    for r in range(repeats):
        print(f'repeat {r}')
        for idx, (x_batch, y_batch, info) in enumerate(training_batch_iterator):
            plot_batch_detection(x_batch, y_batch)