'''
Created on 2019-3-20

@author: Yoga
'''
import pymysql

global db_coon
db_coon = None

global cursor
cursor = None

def connect2db(userName, password, dbName, ip="localhost", ):
    global db_coon
    global cursor
    db_coon = pymysql.connect(ip, userName, password, dbName, charset="utf8")
    cursor = db_coon.cursor()
    
def close2db():
    global db_coon
    global cursor
    if cursor is not None:
        cursor.close()
    if db_coon is not None:
        print('关闭数据库连接！')
        db_coon.close()
        
        
#INSERT INTO chi_words_lib (word) VALUES ('xijian') 
def insert2chi_words_lib(word):
    sql = 'INSERT INTO chi_words_lib (word) VALUES (%s)'
    #print(sql)
    data = word
    update2table(sql, data)



def select2table(variant_word_set):
    global db_coon
    global cursor
    sql = 'SELECT word FROM chi_words_lib WHERE word IN ('
    first = True
    for w in variant_word_set:
        if first:
            sql += '"'+w+'"'
            first = False
        else:
            sql += ', "'+w+'"'
    sql += ')'
    #print(sql)
    cursor.execute(sql)#执行sql语句
    return cursor.fetchall()#获取查询的所有记录
    
def select(sql):
    global db_coon
    global cursor
    cursor.execute(sql)#执行sql语句
    return cursor.fetchall()
      
def update2table(sql, data):
    global db_coon
    global cursor   
    
    #cursor = db_coon.cursor()
    if(len(data)>1):
        effective_row = cursor.executemany(sql, data)
        if(effective_row>0):
            print("成功插入%s条数据"%(effective_row))
    else:
        effective_row = cursor.execute(sql, data[0])
    
    db_coon.commit()#1万条一提交
    #cursor.close()
    
    