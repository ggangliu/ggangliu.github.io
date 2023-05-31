
# 基于阿里云免费资源学习langchain-ChatGLM

[阿里云试用教程](https://help.aliyun.com/document_detail/2261126.html?spm=5176.28008736.J_6443120770.d960469_1.5df73e4dQPwlhL&pipCode=learn&goodsId=960469&scm=20140722.M_960469._.V_1)

- [ChatGLM-6B模型轻量微调和推理](https://help.aliyun.com/document_detail/2329850.htm?spm=a2c4g.2261126.0.0.46ef1d2deTz4SE)
  ChatGLM-6B是一个开源的、支持中英双语的对话语言模型，基于General Language Model（GLM）架构，具有62亿参数。另外，通过模型量化技术，您可以再消费级的显卡上进行本地部署，且在INT4量化级别下最低只需6 GB显存。ChatGLM-6B使用和ChatGPT相似的技术，针对中文问答和对话进行了优化。经过约1 TB Token的中英双语训练，同时配合监督微调、反馈自助、人类反馈强化学习等技术进行优化，使得这个拥有62亿参数的模型能够生成符合人类偏好的回答。

## 免费的GPU资源

1. 阿里云->[免费试用](https://free.aliyun.com/?crowd=personal&spm=5176.28055625.J_5831864660.8.4917154a0QLwwN&scm=20140722.M_118367431.P_154.MO_1802-ID_9553144-MID_9553144-CID_20080-ST_7663-V_1)->搜“AI”->交互式建模 PAI-DSW
2. <https://modelscope.cn/>

## 创建过程记录

1. 创建实例(根据教程要求)
华东1(杭州)  
![config](/assets/snip-images/2023-05-25_175627.png)
资源信息
![resource](/assets/snip-images/2023-05-25_175920.png)
![mirror](/assets/snip-images/2023-05-25_175959.png)

2. 修改Python默认版本，解决库找不到的情况
   echo alias python=python3 >> ~/.bashrc
   source ~/.bashrc
3. 修改模型路径
   这里需用相对路径，完整路径有问题
   ![path](/assets/snip-images/2023-05-26_100210.png)
4. 登录测试
   ![website](/assets/snip-images/2023-05-26_102722.png)
   ![web](/assets/snip-images/2023-05-26_103046.png)
