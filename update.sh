#!/bin/bash
git pull
python updatePicture.py
git add .
git commit -m "update"
git push
hexo cl 
cd source/leetcode
python source/leetcode/display.py 
cd ../../
hexo d