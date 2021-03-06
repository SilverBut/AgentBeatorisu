# AgentBeatorisu

## Legal Statement

Copyright of this repo belongs to Silver.

Unless otherwise stated, you are requested to follow GPLv3 to use code in this repo.

The following related parts are NOT allowed to use this code, unless a statement is signed and published by the author:

* Humensec (http://www.humensec.com)
* Network Behaviour Research Center (NBRC) in Xidian University (http://nbrc.xidian.edu.cn)
* School of Cyber Engineering of Xidian University (http://ce.xidian.edu.cn)
* Leaders, researchers, students and any other people directly related to entities above

ANY POSSIBLE actions will be committed if this statement had been violated.

## Introduction 简介

A library which will provide you a wrapper of jwxt.xidian.edu.cn and some other sites.

本项目旨在提供西安电子科技大学部分信息化系统的第三方接口。

由于众所周知的原因，学校相关信息化系统的接口不对外开放，其界面也难以使用。因此，本项目旨在提供第三方接口，以方便 APP 的二次开发。

Beatorisu，得名于2016年日本四月新番《Re:从零开始的异世界生活》中管理禁书库的少女“ベアトリス”（碧翠丝）。

## Regulations 使用限制

您需要：

* 遵守本接口库使用的GPL协议；
* 确保您使用本接口库的访问频次与正常人类的访问频次没有明显差别，不会干扰正常业务运行，且自定义的提交数据不会对相关计算机系统产生严重的破坏性行为；
* 在测试过程中不使用非法的用户登陆凭据进行恶意测试，并在生产环境下，除明确取得许可外，不私自保存任何信息；
* 保证您的任何学科作业、竞赛作品和其他涉及到成绩评定、名次评定等相关内容的作品中，没有从本库中直接复制代码，或其他任何涉嫌“抄袭”本接口库的行为。否则，代码库拥有者和相关代码的作者有权利向相关的管理方（教务处、学术不端行为监察中心、竞赛组委会等）对有关行为申请处罚措施；
* 在前款所述作品中如果引用了本接口库，则应按照作业、竞赛的有关要求和惯例，在有必要的情况下，明确声明您的代码使用了本接口库。

因违反以上条款造成的一切后果，除法律法规另有规定的外，与本代码库的拥有者和代码开发者没有任何关系。代码库拥有者、代码开发者有权利对除第一条以外的其他规则进行解释。

## Support Status 支持情况

具体的支持情况请查看Issue #1。

## Usage 使用方法

TODO: 添加自动文档

本接口库目前仅有 Python 3 版本。

## Contribution 贡献代码

* Python代码请遵循PEP 8；
* 所有改动会在develop分支进行，确认代码可用后会合并到master分支；
* 多个改动积累到一定程度后会以tag的形式发布新版本，版本号格式为```\d?\.\d```，主版本号用于表示主要模块的更迭，子版本号表示对bug的修正，主版本号的更新不会清除子版本号，即```3.10->4.11->...->12.450```
