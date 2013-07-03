tomdb
=====

A simple wrapper around MySQLdb.

Installation
=====

requires: **MySQLdb**

``$ pip install tomdb``

Getting Started
=====
create connection,the last boole argument means autocommit.
```python
import tomdb
db = tomdb.Connection("localhost", "database", "user", "passwd", True)
```
commit transaction , if autocommit = False
```python
db.commit()
```
close the connection
```python
db.close()
```
get a table-cell from database.if the result more than one,raise error.
```python
>>>cell = db.one("SELECT id FROM table WHERE id=1")
>>>print cell
$ 1
```
get a list from one column.if the result-set has multiple columns,the list only contains first column.
```python
>>>clist = db.onelist("SELECT id FROM table")
>>>print clist
$ [1,2,3,4,5,6,7]
```
get a set from one column.if the result-set has multiple columns,the set only contains first column.
```python
>>>cset = db.oneset("SELECT id FROM table")
>>>print cset
$ set([1,2,3,4,5,6,7])
```
get a dict from one table-cell.if the result more than one,raise error.
```python
>>>cell = db.get("SELECT id FROM table WHERE id=1")
>>>print cell
$ {'id':1}
```
get a list from query-set,and in the list every unit is a dict .The key is column-name,and the value is value of the row.
```python
>>>result = db.query("SELECT id,name FROM table WHERE id<3")
>>>print result
$ [{'id':1, 'name':'Tom'}, {'id':2, 'name':'Jerry'}]
```
get a Iterators from query-set,and in the Iterators every unit is a dict same as above method get().
```python
>>>result = db.iter("SELECT id,name FROM table WHERE id<3")
>>>for item in result:
>>>    print item
$ {'id':1, 'name':'Tom'}
$ {'id':2, 'name':'Jerry'}
```
execute a query,like INSERT or UPDATE,returning the lastrowid from the query.
```python
>>>db.execute("INSERT INTO table (name,passwd) VALUES ('tom','passwd')")
$ 3
>>>db.execute("UPDATE table SET name='Jerry' WHERE id=3")
$ 0
```
get the rowcount of quert-set.
```python
>>>rowcount = db.execute_rowcount("SELECT id,name FROM table WHERE id<3")
>>>print rowcount
$ 2
```
executes the given query against all the given param sequences,return the lastrowid from the query.
```python
>>>db.executemany("INSERT INTO table (name,passwd) VALUES (%s,%s)", (('Tom','passwd'), ('Jerry','passwd')))
$ 5
```