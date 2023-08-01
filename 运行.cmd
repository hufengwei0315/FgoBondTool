@echo off
chcp 65001

pip3 install xlsxwriter
echo 开始执行基础数据更新脚本
python .\update_bond.py
echo 开始执行羁绊生成脚本
python .\bond.py

pause