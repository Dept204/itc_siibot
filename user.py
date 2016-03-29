from sql import SQL
from itc import ITCSII


class User:
    def __init__(self, uid):
        self.uid = uid
        self.sii = ITCSII()
        self.register_status = self._is_registered()

    def _is_registered(self):
        sql = SQL()
        sql._query_("SELECT user, password FROM user WHERE user_id = '" + str(self.uid) + "'")
        data = sql.get_last_result()
        if data is not None:
            return True
        return False

    def register(self, data):
        # Parse input into dict, so we know all values are correctly specified
        dat = dict()
        for x in range(0, len(data), 2):
            dat[data[x]] = data[x+1]
        # Begin with the process
        sql = SQL()
        query = "SELECT registrar(" + str(self.uid) + ", '" + dat['user'] + "','" + dat['password'] + "')"
        return sql.function(query)

    def show_grades(self):
        sql = SQL()
        sql._query_("SELECT user, password FROM user WHERE user_id = '" + str(self.uid) + "'")
        data = sql.get_last_result()
        self.sii.set_userdata(data['user'], data['password'])
        return self.sii.get_grades()

    def update_data(self, data):
        # Parse input into dict, so we know all values are correctly specified
        values = dict()
        for x in range(0, len(data), 2):
            values[data[x]] = data[x+1]
        # Begin with the process
        query = "SELECT actualiza(" + str(self.uid)
        if 'user' in values and 'password' in values:
            query += ", '" + values['user'] + "','" + values['password'] + "')"
        elif 'user' in values:
            query += ", '" + values['user'] + "', NULL)"
        elif 'password' in values:
            query += ", NULL, '" + values['password'] + "')"
        else:
            query += ", NULL, NULL)"
        sql = SQL()
        return sql.function(query)

    def delete(self):
        query = 'SELECT eliminar(' + str(self.uid) + ')'
        sql = SQL()
        return sql.function(query)

    def command(self, command):
        clist = command.split()
        if 'grades' in clist:
            return self.show_grades()
        else:
            return 'Comando no reconocido'
