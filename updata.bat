@echo off
git pull
python updatePicture.py
git add .
git commit -m "updata"
git push
call hexo clean
cd source/leetcode
python display.py
cd ../../
call hexo d