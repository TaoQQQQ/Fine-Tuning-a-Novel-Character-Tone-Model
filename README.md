重生之我是萧炎

第一步：打开split.py，输入想要提取角色的名字（可以加入角色的别名啥的），按一定长度切割成不同的段落。

第二步：打开create.py，使用大模型去提取角色对话，按预先的设定格式，保存为txt文件。

第三步：打开convert_data_format.py，转换成Alpaca的格式，具体是个json文件。

第四步：如果考虑再用KTO进一步对齐，打开KTO.py，按kto.txt的格式，输入对话及评价，运行KTO.py转化为ShareGPT格式的偏好数据集。

第五步：转到LLaMA，按官方教程部署，将指令数据集和偏好数据集（就是那两个json格式的文件）放到data数据集，记着改一下dataset_info.json里面的内容。

第六步：先指令微调后合并再用kto进一步对齐。
