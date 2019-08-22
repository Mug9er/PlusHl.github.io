@echo off
set Path="C:\Program Files\Git\bin\git.exe"
%Path% pull
%Path% add .
%Path% commit -m "updata"
%Path% push
echo clean
echo d -g