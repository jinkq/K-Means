# K-Means
## 文件夹目录
* run_in_batch.sh：改变簇数k和迭代次数iternum，批量生成K-Means聚类的可视化结果
* input：输入文件（每行一个instance，各属性值用,分隔）
* output：Hadoop输出文件
* result：执行`run_in_batch.sh`批量生成的可视化图片
* src/main
    * java：Hadoop实现K-Means聚类的源代码
    * python：K-Means聚类结果的可视化
* target：Hadoop实现K-Means聚类可执行的jar包

## 算法原理
K-Means聚类是一种无监督学习，需要提前知道簇数k。初始选k个点作为中心点，计算每个样本点到中心点的距离，将样本点归到距离最近的中心点那一簇，再重新计算中心点。重复上述过程，直至k个中心点都不再变化（或指定迭代次数提前结束）。

## 结果可视化
为批量生成结果可视化的图片，编写了shell脚本`run_in_batch.sh`，循环簇数k（2-8）和迭代次数iternum（2-10），并调用画图函数`plot.py`，在result文件夹生成不同k值和不同iternum的聚类结果图片。`plot.py`主要使用seaborn画图，图片中用不同的颜色和形状区分属于不同簇的样本。

## 作业心得
