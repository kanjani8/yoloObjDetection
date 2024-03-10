#to set cfg file 

# Path to cfg file
cfg_file_path = 'cfg/yolov4-tiny-custom.cfg' 

# Elements you find and the new value
elements_to_update = {
    'subdivisions': '16',
    'max_batches': '2000', # = classes * 2000
    'steps': '1600, 1800', # 80%, 90% of max batches
    'classes': '1',
#    'filters': '256' # filters = (classes+coords+1)*<number of mask> == 18 212th, 263th line only 
}

# Read the file
with open(cfg_file_path, 'r') as file:
    lines = file.readlines()

# Modify the specific elements
with open(cfg_file_path, 'w') as file:
    for line in lines:
        for element, new_value in elements_to_update.items():
            if line.startswith(element):
                line = element + ' = ' + new_value + '\n'
                break  # Stop checking once a match is found and updated
        file.write(line)