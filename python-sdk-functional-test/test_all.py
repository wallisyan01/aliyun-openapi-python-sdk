import sys
import os
cur_path = os.path.abspath('..')
python_path = ''
for ret in os.walk(cur_path):
    root_path = ret[0]
    root_path_list = root_path.split('\\')
    if root_path_list[-1].startswith('aliyun-python-sdk'):
        sys.path.insert(1,root_path)
import subprocess
p = subprocess.Popen("coverage run --branch -m pytest python-sdk-functional-test/", stdout=subprocess.PIPE,shell=True)
out, err = p.communicate()
print(out)
print(err)
