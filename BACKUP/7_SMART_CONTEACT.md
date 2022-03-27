# [SMART_CONTEACT](https://github.com/linziyang1106/2022/issues/7)

智能合约开发

---

Ethereum介绍
https://hyperledger-fabric.readthedocs.io/zh_CN/release-2.2/whatis.html

---

> Adults always say, "don't do this, don't do that." However, children always like to try new things, and so do I. So I create this token so that more people can do what they like to. Anyone who wants more free time can come and claim my airdrop.
$RND tokens issued a total of 37.8 trillion, of which 12% was left to my mom and dad. It was their dedication and love over the past 12 years that gave me the opportunity to create this token. 38% of the total amount shall be subjected to liquidity mining. 50% of the total will be airdropped to 101010 people. Airdrop will be claimed within 1 year. After 1 year, the unclaimed tokens will be destroyed directly. In order to encourage more people to claim the airdrop, we will airdrop a larger share of tokens to the top 1010 people who come to claim for tokens.
When making this airdrop website, I encountered many difficulties, some because of the lack of information on the Internet, especially in the front-end connection to solidity.
Therefore, I will publish the source code of my website on GitHub for exchange and learning. I hope those who want to build Smart Contract can learn more conveniently from my code.
P.S.
My dad always say there is no such thing as a free lunch, well, let's wait and see. Maybe $RND is.

---zheng huang

---

# 基本概念

注意数字签名、公钥私钥加密的知识

## EVM

### 概述

EVM完全隔离于外界，在EVM中运行代码无法访问网络、文件系统和其他进程，智能合约之间的访问也是受限的。

### 账户

+ 外部账户：人用的，由公钥决定
+ 合约账户：在创建该合约时决定（这个地址通过合约创建者的地址和从该地址发出过的交易数量计算得到的，也就是所谓的“nonce”）

无论账户是否存储代码，这两类账户对EVM来说是一样的

每个账户都有一个键值对形式的持久化存储。其中 key 和 value 的长度都是256位，我们称之为 **存储** 。

此外，每个账户有一个以太币余额（ **balance** ）（单位是“Wei”, `1 ether` 是 `10**18 wei`），余额会因为发送包含以太币的交易而改变。

### 库

一个合约可以动态的调用别的合约的代码，使Solidity实现库的能力。

### 日志

有一种特殊的可索引的数据结构，其存储的数据可以一路映射直到区块层级。这个特性被称为 **日志(logs)** ，Solidity用它来实现 **事件(events)** 。合约创建之后就无法访问日志数据，但是这些数据可以从区块链外高效的访问。因为部分日志数据被存储在 [布隆过滤器（Bloom filter)](https://en.wikipedia.org/wiki/Bloom_filter) 中，我们可以高效并且加密安全地搜索日志，所以那些没有下载整个区块链的网络节点（轻客户端）也可以找到这些日志。

## 数据类型

1. 区分大小写
2. 风格类似Python，下划线分割单词
3. 占用空间越小，gas越低
4. 可见性
   + `private`：使函数和状态变量 , 仅在当前合约内可以访问 . 在继承的合约内不可访问。
   + `public`：使函数和状态变量 , 在当前合约内和被继承的合约内都可以访问 . 并且使函数和状态变量成为合约对外接口。
   + `external`：外部函数是合约接口的一部分 , 所以我们可以从其它合约或通过交易来发起调用 . 一个外部函数f , 不能通过内部的方式来发起调用 , (如f()不可以，但可以通过this.f()) . 外部函数在接收大的数组数据时更加有效。
   + `internal`：这样声明的函数和状态变量只能通过内部(internal)访问 . 如在当前合约中调用 , 或继承的合约里调用 . 需要注意的是不能加前缀this , 前缀this是表示通过外部(external)方式访问。
5. 数字单位
   + 默认wei，注意改为ether，1 ether = 10^18 wei，1 gwei = 10^9 wei
6. 时间单位
   + days
7. function修饰符
   + view：如果此函数不修改数据可用view修饰符，不消耗gas
   + pure：不修改也不读取可用pure

## ERC20代码

> OpenZeppelin的仓库

The file of ERC20.sol : https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol

The file of IERC20.sol : https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/IERC20.sol

The file of IERC20Metadata.sol : https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/extensions/IERC20Metadata.sol

The file of Context.sol : https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/Context.sol

