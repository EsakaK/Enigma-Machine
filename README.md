### 恩格玛(Enigma)加密解密一体机
恩尼格玛密码机（德语：Enigma，又译恩尼格密码机、哑谜机、奇谜机或谜式密码机）是一种用于加密与解密文件的密码机。确切地说，恩尼格玛是对二战时期纳粹德国使用的一系列相似的转子机械加解密机器的统称，它包括了许多不同的型号，为密码学对称加密算法的流加密。

恩格玛机的破解是一个艰辛且漫长的过程，涌现了无数仁人志士，许多为破解恩格玛机贡献巨大的科学家却因为战争、世俗而流离失所，抑郁终身，其中就包括计算机祖师爷——阿兰·图灵。

本仓库力图实现最基本的加密解密过程（不包括插线板）

### Usage
```commandline
python --key [ABC] --textfile [file_path]
```
- [ABC] 是三转子恩格玛机的加密/解密秘钥，由交流者制定和共享
- [file_path] 应该是一个纯文本文件的绝对路径
由于恩格玛机的“自反性”，不需要对明文和暗文进行区分，恩格玛机只会完成它该做的。

### Link
[【计算机博物志】战争密码（上集）如何复刻一台恩格玛机](www.bilibili.com/video/BV1DS4y1R7hM)