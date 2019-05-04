# chinese_words_lib
整和了网上多个中文词库文件，合并成了一个比较齐全的词库，可供大家下载使用
1. chi_words_lib_sql.rar中是我已经整合好的中文词库，从数据库（MySQL）中导出来的sql文件，大家可以直接导入DB然后使用；如果您有其他更多词库文件，也可以使用我提供的代码，加入filepaths中，重新运行程序整和词库，整和的结果是存入MySQL的，表结构可参考sql文件最前面的表结构定义。

2. 代码入口是src/chi_word_libs/generate_wordset.py，src/db/mysql_db/dbapi.py封装了操作数据库的一些简单接口，src/zh_data_files/文件夹下是我从网上下载的一些中文词库，他们主要来自于这两个网址：https://download.csdn.net/download/zhaohuakai/10594462 和 https://download.csdn.net/download/weixin_39128119/10641353 

3. 如果是运行代码，请将src/zh_data_files/下的文件解压再执行。
