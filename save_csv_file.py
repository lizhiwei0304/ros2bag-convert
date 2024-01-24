import csv
import json
import time
import numpy as np

# 将嵌套字典和列表展平为一级字典
def flatten_data(data, parent_key='', sep='_'):
    items = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(flatten_data(v, new_key, sep=sep).items())
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}{sep}{i}" if parent_key else f"{i}"
            items.extend(flatten_data(v, new_key, sep=sep).items())
    else:
        items.append((parent_key, data))
    return dict(items)

def save_csv_file(data, csv_file_name, version=0, print_out=False):
    with open(csv_file_name, mode='w') as csv_file:
        field_names = ['row_time', 'topic_name', 'topic_type', 'time_stamp', 'message']
        writer = None
        nt, line_datas = data[0], data[1]
        for index in range(len(line_datas)):
            row_time, row_data = nt[index], line_datas[index]
            flattened_data = flatten_data(row_data)
            
            # 将 row_time 添加到字典的第一列
            flattened_data = {'row_time': row_time, **flattened_data}
            
            if writer is None:
                field_names = flattened_data.keys()
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
            writer.writerow(flattened_data)
    print('Saving', csv_file_name)

