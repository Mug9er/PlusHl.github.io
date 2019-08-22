set Path="C:\Program Files\Git\bin\git.exe"
%Path% pull
hexo clean
hexo d -g
%Path% add .
%Path% commit -m "updata"
%Path% push