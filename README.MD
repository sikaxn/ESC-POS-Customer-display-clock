## Turn 8 seg (LED8) customer display into a clock
## 将POS 8位数字LED顾客显示屏作为时钟
You need a ESC/POS compliant customer display unit.
你需要一个支持ESC/POS的顾客显示屏

Example compatable display unit
支持ESC/POS的顾客显示屏的例子

https://www.ocominc.com/cn/products/Double-Line-Pos-LED-Customer-Display-LED8A.html
https://detail.tmall.com/item.htm?spm=a21wu.10013406.0.0.6bec6647XC0ywV&id=584671093507
https://item.taobao.com/item.htm?spm=a21wu.10013406.0.0.6bec6647XC0ywV&id=15241673778
https://www.yoycart.com/Product/35302543438/
https://guide.alibaba.com/t-shop/aibo-led8-customer-display-pole-display-pos-customer-display-led-customer-display-pole-display_76523365.html
https://www.alibaba.com/product-detail/LED8-Customer-Display-POS-Pole-Display_1852639944.html
https://www.chinaglobalmall.com/products/565701019398
These links are not affiliated with me and may change overtime.
这些链接与我没有推广关系，并可能随着时间而改变。

## Setup environment
## 配置环境
You need to install python and pyserial library in order to get this work.
python和pyserial是本程序的依赖，需要被安装。

After install, you needs to edit serial port assignment on ```timeupdate.py``` to the matching one on the stack display connected to. 
 ```timeupdate.py```中的串口需要修改为顾客显示屏连接的串口。
 
 ## Setup startup (windows)
 ## 配置开机启动(windows)
 Copy  ```timeupdate.py``` into C drive, than throw ```stkclock.bat``` into startup folder (by running shell:startup on cmd or run you can open startup folder). Stack clock will come on when startup. 
 将```timeupdate.py```拷贝到C盘根目录，然后将```stkclock.bat```放入startup文件夹（通过在CMD里运行shell:startup可以打开这个文件夹），时钟将开机启动，
