# To create .data , .names file to custom training with Yolo

import os
import math
file_path =  './data/'
list_path =  './data/list/'

with(
    open(file_path + 'humanClass' + '.names', 'w') as class_file, # all classes to use
    open(file_path + 'personDetection' + '.data', 'w') as data_file # informations for custom training
    ):
        class_file.write('person')

        data_file.write('classes = 1\n')
        data_file.write('train = ' + list_path + 'train.txt\n')
        data_file.write('valid = ' + list_path + 'valid.txt\n')
        data_file.write('test = ' + list_path + 'test.txt\n')
        data_file.write('names = ' + file_path + 'humanClass.names\n')
        data_file.write('backup = ./darknet/backup\n')

    
