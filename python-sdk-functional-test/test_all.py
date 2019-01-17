import sys
import os
cur_path = os.path.abspath('..')
python_path = ''
for ret in os.walk(cur_path):
    root_path = ret[0]
    root_path_list = root_path.split('\\')
    if root_path_list[-1].startswith('aliyunsdk'):
        sys.path.insert(1,root_path)
print(sys.path)
import subprocess
ret = subprocess.call("coverage run --branch -m pytest python-sdk-functional-test/")
print(ret)
