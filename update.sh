#!/bin/bash
git pull
python updatePicture.py
git add .
git commit -m "update"
git push
hexo clean
hexo d -g
