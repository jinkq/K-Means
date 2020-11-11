# K-Means
## 文件夹目录
* input：输入文件（每行一个instance，各属性值用,分隔）
* output：Hadoop输出文件
* result：执行`run.sh`批量生成的可视化图片
* src/main
    * java：Hadoop实现K-Means聚类的源代码
    * python：K-Means聚类结果的可视化
* target：Hadoop实现K-Means聚类可执行的jar包
* run_in_batch.sh：改变簇数k和迭代次数iternum，批量生成K-Means聚类的可视化结果

## 算法原理
K-Means聚类是一种无监督学习

## 结果可视化
为批量生成结果可视化的图片，编写了shell脚本`run_in_batch.sh`，循环簇数k（2-8）和迭代次数iternum（2-10），并调用画图函数`plot.py`，在result文件夹生成不同k值和不同iternum的聚类结果图片。`plot.py`主要使用seaborn画图，图片中用不同的颜色和形状区分属于不同簇的样本。
