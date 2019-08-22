set Path="C:\Program Files\Git\bin\git.exe"
%Path% pull
%Path% add .
%Path% commit -m "updata"
%Path% push
call hexo clean
call hexo d -g