# FgoBondTool
计算Fgo 自有从者点数
# 前情提要
1. 所有base文件夹中的json文件 都是从 https://github.com/chaldea-center/chaldea-data/tree/main/dist 拷贝或者下载来得
2. 请自行安装Python运行环境
3. 请使用 https://docs.chaldea.center/zh/guide/import_https/ 的方法 进行游戏内容抓包
4. 抓包后的json文件 保存为result.json和 cmd文件同目录
5. 如果日服有更新从者 可以使用 基础数据更新.cmd 更新文件
6. base.py中 已经写好了代理功能 如果自有机场可以吧链接指向到自己的代理 加速下载文件
# 生成羁绊文件
1. 完成上述准备工作后 请点击运行.cmd  会自动下载excel的依赖包
2. 生成的文件 是按照 cost分sheet页
3. 每个sheet页中的从者 都按照距离升级最少的点数 正向排序
