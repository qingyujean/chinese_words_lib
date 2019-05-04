#coding=utf-8
'''
Created on 2019-3-20

@author: Yoga
'''
import threading
import time
import pkg_resources
from db.mysql_db import dbapi

files = ['360万中文词库/词典360万单词量.txt',
         
         '中文分词词库汇总/主流分词工具的词库/IK分词.txt',
         '中文分词词库汇总/主流分词工具的词库/jieba分词.txt',
         '中文分词词库汇总/主流分词工具的词库/mmseg分词.txt',
         '中文分词词库汇总/主流分词工具的词库/word分词.txt',
         
         '中文分词词库汇总/中文分词词库汇总/40.txt',
         '中文分词词库汇总/中文分词词库汇总/57.txt',
         '中文分词词库汇总/中文分词词库汇总/91.txt',
         '中文分词词库汇总/中文分词词库汇总/133.txt',
         '中文分词词库汇总/中文分词词库汇总/155.txt',
         '中文分词词库汇总/中文分词词库汇总/196-1.txt',
         '中文分词词库汇总/中文分词词库汇总/213-1.txt',
         '中文分词词库汇总/中文分词词库汇总/217.txt',
         '中文分词词库汇总/中文分词词库汇总/218.txt',
         '中文分词词库汇总/中文分词词库汇总/300.txt'
         ]
wordSet = set()
threads = []


        
def readWordsFile(filePath):
    start = time.clock()   
    with open(filePath, 'r', encoding='UTF-8') as f:#文件特征：公司\tcomb\t968911\n
        for line in f:
            #print(line.split()[0])
            wordSet.add(line.split()[0])            
    end = time.clock()
    f.close()
    print('处理文件：',filePath, '，耗时：',end-start)
    print('当前wordSet有词：',len(wordSet),'个')

def createThreads(threads, filePaths): 
    for i in range(len(filePaths)):
        
        filepath_i = pkg_resources.resource_filename(__name__, "../zh_data_files/"+filePaths[i])
        t = threading.Thread(target=readWordsFile, args=(filepath_i,))
        threads.append(t)
 
 
        
if __name__ == '__main__':
    start = time.clock()  
    createThreads(threads, files)
    for t in threads:
        #t.setDaemon(True)#将该线程标记为守护线程(True)或用户线程
        t.start()
    for t in threads:
        t.join()    
    end = time.clock()
    print('All over!')
    print('共耗时：',end-start)
    print(len(wordSet))
    
    
    dbapi.connect2db("root", "123456", "wa")
    tmpWords = []
    idx = 0
    print('开始入库...')
    for w in wordSet:
        #print(w)
        tmpWords.append((w,))#插入的一行值应为元祖
        idx += 1
        if idx==10000:#一次插入一万条
            #print(tmpWords)
            dbapi.insert2chi_words_lib(tmpWords)
            tmpWords = []
            idx = 0
    #处理最后不足1万的词
    if(len(tmpWords)>0):
        dbapi.insert2chi_words_lib(tmpWords)
    dbapi.close2db()
    print('入库完成...')
    