@echo off
git pull
git add .
git commit -m "updata"
git push
call hexo clean
call hexo d -g