@echo off
SET PYTHONPATH = %PYTHONPATH%
for /r %i in ('aliyun-python-sdk*') do (
	SET PYTHONPATH=%PYTHONPATH%;%i
)
pause
