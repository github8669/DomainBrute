# 简介

`DomainBrute`是一个超级简单的子域名扫描工具，融合了子域名挖掘机、及市面上很多非常强大的字典，使用也非常简单

# 安装

使用Python语言编写

第三方模块用了`requests`,所以`clone`以后只需要安装`requests`模块即可。

```
pip install requests
```

安装完成。

# 使用方法

```
Usage: domins.py [options]

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     target url for scan
  -f file, --file=file  file filename
  -t COUNT, --thread=COUNT
                        scan thread_count
```

使用案例：Python domins.py -f C:\Users\admin\Desktop\n.txt

![image](https://github.com/github8669/DomainBrute/assets/22950238/ea445e15-9115-43ab-925d-c8ec0a606632)


![7c8537f09f7439e6e5476319b515169](https://github.com/github8669/DomainBrute/assets/22950238/ff938be5-8ecf-4c22-8dd6-e46462861ccb)



