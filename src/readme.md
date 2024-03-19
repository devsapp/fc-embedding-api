
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# fc3-embedding-api 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc3-embedding-api&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc3-embedding-api" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc3-embedding-api&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc3-embedding-api" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc3-embedding-api&type=packageDownload">
  </a>
</p>

<description>

使用serverless devs将  开源Bert模型部署到函数计算上，内置bge-large-zh、text2vec-large,支持模型自定义

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/fc-embedding-api)

</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>
</service>

<remark>

您还需要注意：   
您还需要注意：  
1.项目依赖阿里云函数计算和阿里云文件存储 Nas，这两款产品都会产生资费，请关注您的资源包使用情况和费用情况 2.项目部署成功之后确保模型加载完毕（左上角选择框有模型显示）再开始推理 3.项目初始启动有大约 1 分钟的白屏时间，这是服务完全冷启动的状态，请耐心等待

</remark>

<disclaimers>

免责声明：   
免责声明：

1. 该项目的构建镜像及应用模板完全开源，由社区开发者贡献，阿里云仅提供了算力支持；

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc3-embedding-api) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc3-embedding-api) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init fc3-embedding-api -d fc3-embedding-api`
  - 进入项目，并进行项目部署：`cd fc3-embedding-api && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

### 简介
基于本案例，您可以将bge-large-zh 模型部署到 阿里云，并且以api的方式进行访问
### 背景
在以LLM为核心的应用场景中，向量嵌入（embedding）已被广泛应用于知识库，Agent 长记忆等场景，然而该基础服务随着业务量的增加，会带来较大的成本，因此我们期望有一种极致成本优化的方案来解决这个问题，基于开源模型的自托管是一种方案，更重要的是，我们采用CPU的方式实现了跟GPU差不多的效果，而成本却低很多。
### 价值
部署专属的向量算法模型（bge-large-zh），并且充分利用阿里云产品函数计算的弹性能力，低成本优势（基于cpu方案），能够满足您的自用或者商用需求，不管是大规模还是中小规模的服务调用都适用，并且是最佳的方案

</appdetail>

## 使用流程

<usedetail id="flushContent">

1. 访问应用中心，选择fc3-embedding-api应用模板进行部署
2. 根据指引进行选择部署
![部署fc3-embedding-api](https://img.alicdn.com/imgextra/i4/O1CN01HCp6Dj1HU7wnozj8e_!!6000000000760-0-tps-3376-1794.jpg)
![部署fc3-embedding-api](https://img.alicdn.com/imgextra/i1/O1CN0114TIuB2A2vI3KPgUj_!!6000000008146-0-tps-3488-1702.jpg)
3.访问 api测试界面进行测试
![访问embedding api](https://img.alicdn.com/imgextra/i4/O1CN01TkDGPr1aynAI9OEe9_!!6000000003399-0-tps-3048-1782.jpg)

</usedetail>

## 注意事项

<matters id="flushContent">

您需要开通[阿里云Nas服务](https://www.aliyun.com/product/nas?spm=5176.21213303.J_XmGx2FZCDAeIy2ZCWL7sW.54.23ef2f3dYF14Mj&scm=20140722.S_product@@%E4%BA%91%E4%BA%A7%E5%93%81@@105381._.ID_product@@%E4%BA%91%E4%BA%A7%E5%93%81@@105381-RL_nas-LOC_topbar~UND~product-OR_ser-V_3-P0_0)
我们使用该服务存储beg-large-zh 模型，它越会占用你1.2G的空间

</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
