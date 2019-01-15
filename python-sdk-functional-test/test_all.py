import os
print('enter test')
cur_path = os.path.abspath('..')
python_path = ''
for ret in os.walk(cur_path):
    root_path = ret[0]
    root_path_list = root_path.split('\\')
    if root_path_list[-1].startswith('aliyun-python-sdk-'):
        python_path += root_path + ';'
os.environ.update({"PYTHONPATH":python_path})
# path = os.environ.get('PYTHONPATH')
# print(path)
import subprocess
cmd = 'coverage run -a --source="./aliyun-python-sdk-core/aliyunsdkcore" --branch -m pytest python-sdk-functional-test'
ret = subprocess.check_call(cmd, shell=True)
print(ret)
