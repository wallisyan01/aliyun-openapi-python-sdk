import os
import sys
print(sys.path)
cur_path = os.path.abspath('..')
python_path = ''
for ret in os.walk(cur_path):
    root_path = ret[0]
    root_path_list = root_path.split('\\')
    if root_path_list[-1].startswith('aliyun-python-sdk-'):
        sys.path.insert(1,root_path)
        python_path += root_path + ';'
os.environ.update({"PYTHONPATH":python_path})
print(sys.path)
