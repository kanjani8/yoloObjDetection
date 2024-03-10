# To create txt list for training datas

import os
import math

# Dataset ratios #Total should be 100
train_set_ratio = 70
valid_set_ratio = 10
test_set_ratio = 20

file_path = './data/humanData/'
txt_path = './data/list/'
# Listing file names
file_names = [file for file in os.listdir(file_path) if file.endswith(('.jpg', '.png'))]
file_len = len(file_names)

# Calculating indices for dataset division
train_index_end = math.ceil(file_len * (train_set_ratio / 100))
valid_index_end = train_index_end + math.ceil(file_len * (valid_set_ratio / 100))

# Opening text files to write paths
with(
    open(txt_path + 'train.txt', 'w') as train_file,
    open(txt_path + 'valid.txt', 'w') as val_file,
    open(txt_path + 'test.txt', 'w') as test_file
    ):
    # Writing train file paths
    for i in range(0, train_index_end):
        train_file.write(file_path + file_names[i] + '\n')
    
    # Writing validation file paths
    for i in range(train_index_end, valid_index_end):
        val_file.write(file_path + file_names[i] + '\n')
    
    # Writing test file paths
    for i in range(valid_index_end, file_len):
        test_file.write(file_path + file_names[i] + '\n')
    
    print(train_file)