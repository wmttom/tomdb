tomdb
=====

A simple wrapper around MySQLdb.  
tomdb是MySQLdb的简单封装,方便获得各种类型的数据结构结果集.  
是不使用ORM场合中，非常轻量、方便的数据库访问方式.  
fork自tornado的db模块,在原有基础上加入了事务autocommit选项和commit(),加入了one,onelist,oneset等方法方便使用.

Installation
=====

requires: **MySQLdb**  
依赖模块MySQLdb  
``$ pip install tomdb``

Getting Started
=====
创建一个数据库连接,最后的布尔类型参数为事务是否自动提交,不显示指定False默认为True.  
create connection,the last boole argument means autocommit.
```python
import tomdb
db = tomdb.Connection("localhost", "database", "user", "passwd", True)
```
提交事务,在自动提交为False时使用.  
commit transaction , if autocommit = False
```python
db.commit()
```
关闭数据库连接.  
close the connection
```python
db.close()
```
获得表内一个单元格的信息,如果SQL语句的结果集超过一个单元格,会提示错误.  
get a table-cell from database.if the result more than one,raise error.
```python
>>>cell = db.one("SELECT id FROM table WHERE id=1")
>>>print cell
$ 1
```
以列表的形式获取某一列的数据,如果结果集有多列,只会获得第一列.  
get a list from one column.if the result-set has multiple columns,the list only contains first column.
```python
>>>clist = db.onelist("SELECT id FROM table")
>>>print clist
$ [1,2,3,4,5,6,7]
```
以集合的形式获取某一列的数据,如果结果集有多列,只会获得第一列.  
get a set from one column.if the result-set has multiple columns,the set only contains first column.
```python
>>>cset = db.oneset("SELECT id FROM table")
>>>print cset
$ set([1,2,3,4,5,6,7])
```
以字典的形式获取某一行数据,key为列名,value为对应数据,如果结果超过一行,会提示错误.  
get a dict from one row.if the result more than one row,raise error.
```python
>>>cell = db.get("SELECT id FROM table WHERE id=1")
>>>print cell
$ {'id':1}
```
以列表的形式获取SQL查询结果集所有数据,每一行数据为一个字典,key为列名,value为对应数据.  
get a list from query-set,and in the list every unit is a dict .The key is column-name,and the value is value of the row.
```python
>>>result = db.query("SELECT id,name FROM table WHERE id<3")
>>>print result
$ [{'id':1, 'name':'Tom'}, {'id':2, 'name':'Jerry'}]
```
以迭代器的形式获取SQL查询结果集所有数据,可使用for遍历,每次遍历获取一个字典,key为列名,value为对应数据.  
get a Iterators from query-set,and in the Iterators every unit is a dict same as above method get().
```python
>>>result = db.iter("SELECT id,name FROM table WHERE id<3")
>>>for item in result:
>>>    print item
$ {'id':1, 'name':'Tom'}
$ {'id':2, 'name':'Jerry'}
```
执行一条SQL,比如INSERT和UPDATE,返回这次查询的lastrowid(插入操作会取得最后插入行id).  
execute a query,like INSERT or UPDATE,returning the lastrowid from the query.
```python
>>>db.execute("INSERT INTO table (name,passwd) VALUES ('tom','passwd')")
$ 3
>>>db.execute("UPDATE table SET name='Jerry' WHERE id=3")
$ 0
```
获得查询结果集的行数量.  
get the rowcount of quert-set.
```python
>>>rowcount = db.execute_rowcount("SELECT id,name FROM table WHERE id<3")
>>>print rowcount
$ 2
```
根据给出的参数多次执行SQL语句，返回这次查询的lastrowid.  
executes the given query against all the given param sequences,return the lastrowid from the query.
```python
>>>db.executemany("INSERT INTO table (name,passwd) VALUES (%s,%s)", (('Tom','passwd'), ('Jerry','passwd')))
$ 5
```
