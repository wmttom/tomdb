# coding:utf8
import logging

version = "0.5.1"
version_info = (0, 5, 1, 0)


class Conn(object):

    def __init__(self, engine, autocommit=False):
        try:
            self.reconnect(engine)
            if not autocommit:
                self.begin()
        except Exception:
            logging.error("Cannot connect to MySQL on this engin")

    def __del__(self):
        self.close()

    def reconnect(self, engine):
        """Closes the existing database connection and re-opens it."""
        self.close()
        self._db = engine.connect()
        # print self._db_args

    def close(self):
        """Closes this database connection."""
        if getattr(self, "_db", None) is not None:
            self._db.close()
            self._db = None

    def begin(self):
        """Begin"""
        self.trans = self._db.begin()

    def commit(self):
        """Commit"""
        try:
            self.trans.commit()
        except Exception:
            logging.error("Cannot commit,trans is not found.")

    def rollback(self):
        """Rollback"""
        try:
            self.trans.rollback()
        except Exception:
            logging.error("Cannot rollback,trans not found.")

    def get(self, query, *parameters, **kwparameters):
        """Returns the first row returned for the given query."""
        rows = self.query(query, *parameters, **kwparameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    def query(self, query, *parameters):
        """Returns a row list for the given query and parameters."""
        data = self._db.execute(query, parameters)
        column_names = [d[0] for d in data._cursor_description()]
        return [dict(zip(column_names, row)) for row in data.cursor]

    def onelist(self, query, *parameters):
        """Returns one column of the list for the given query and parameters."""
        data = self._db.execute(query, parameters)
        return [row[0] for row in data.cursor]

    def oneset(self, query, *parameters):
        """Returns one column of the set for the given query and parameters."""
        data = self._db.execute(query, parameters)
        return {row[0] for row in data.cursor}

    def one(self, query, *parameters, **kwparameters):
        """Returns one str for the given query and parameters."""
        data = self._db.execute(query, parameters)
        rows = [row[0] for row in data.cursor]
        if len(rows) == 0:
            return None
        elif len(rows) == 1:
            return rows[0]
        else:
            raise Exception("Multiple rows returned for Database.one() query")

    def execute(self, query, *parameters):
        """Executes the given query, returning the lastrowid from the query."""
        data = self._db.execute(query, parameters)
        return data.lastrowid
