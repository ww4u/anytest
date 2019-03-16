cd .

set dir_name=anytest

::del /s /q %dir_name%
rmdir/s /q %dir_name%

mkdir %dir_name% 
copy t4.xlsm %dir_name%\

mkdir %dir_name%\script
copy script\*.py %dir_name%\script\
pause
