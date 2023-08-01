@echo off
chcp 65001

echo 开始执行基础数据下载脚本
python .\base.py
echo 开始执行基础数据更新脚本
python .\update_bond.py
pause