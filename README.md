# K-Means聚类
## 文件夹目录
* run_in_batch.sh：改变簇数k和迭代次数iternum，批量生成K-Means聚类的可视化结果
* input：输入文件（每行一个instance，各属性值用,分隔）
* output：Hadoop输出文件（输入为示例输入NewInstance.txt，簇数k=4，迭代次数iternum=5的结果）。文件夹cluster-i是第i次迭代产生的中心点数据，最终结果存储在文件夹clusteredInstances中，<key, value>=<样本点, 簇>
* result：执行`run_in_batch.sh`批量生成的可视化图片
* src/main：
    * java：Hadoop实现K-Means聚类的源代码
    * python：K-Means聚类结果可视化的源代码
* target：Hadoop实现K-Means聚类可执行的jar包

## 算法原理
K-Means聚类是一种无监督学习，需要提前知道簇数k。初始选k个点作为中心点，计算每个样本点到中心点的距离，将样本点归到距离最近的中心点那一簇，再重新计算中心点。重复上述过程，直至k个中心点都不再变化，即聚类结果不再变化（或指定迭代次数提前结束）。

## 结果可视化
为批量生成结果可视化的图片，编写了shell脚本`run_in_batch.sh`，循环簇数k（2-8）和迭代次数iternum（2-10），并调用画图函数`plot.py`，在result文件夹生成不同k值和不同iternum的聚类结果图片。`plot.py`主要使用seaborn画图，图片中用不同的颜色和形状区分属于不同簇的样本。

### 例：k=5, iternum=6的聚类结果图片

（其余结果图片在result文件夹中）

![](https://finclaw.oss-cn-shenzhen.aliyuncs.com/img/k=5_iternum=6.png)



## 作业心得
1. 刚开始是打算用matplotlib.pyplot画聚类结果图，希望以不同颜色区分不同簇的样本点，但上网搜发现这需要提前从Hadoop输出结果文件中读取总簇数，并为每一个不同的簇指定颜色。后来改用Seaborn，可以直接通过scatterplot的`hue`和`style`参数指定按照某一变量自动生成不同的颜色和形状，Seaborn库的功能更加强大，与R语言相似
2. 由于要求尝试不同的簇数k和迭代次数iternum，而示例代码是通过命令行传参指定k和iternum，因此首次尝试写shell脚本来批量生成不同k和iternum的结果并作图

## 作业可改进的地方
* 修改选取初始k个中心点的方式
* 增加参数，让用户可以选择一直迭代到聚类结果不发生变化，还是指定迭代次数提前结束聚类