@echo off
git pull
python updatePicture.py
git add .
git commit -m "updata"
git push
call hexo clean
call hexo d -g