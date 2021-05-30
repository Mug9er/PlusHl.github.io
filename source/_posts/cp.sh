#!/bin/bash
read -p "同步文档: " source

read -p "目标文档: " dest

cp "$source" "../../../$dest"
