#!/bin/bash
git pull
python updatePicture.py
git add .
git commit -m "update"
git push
hexo cl && hexo g && hexo d