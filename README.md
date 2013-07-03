tomdb
=====

A simple wrapper around MySQLdb.

Installation
=====

requires: **MySQLdb**

``$ pip install tomdb``

Getting Started
=====

create connection

```python
import tomdb
db = tomdb.Connection("localhost", "database", "user", "passwd")
```
get a table-cell from database.if the result more than one,raise erroe.

```python
>>>cell = db.one("SELECT id FROM table WHERE id=1")
>>>print cell
$ 1
```
