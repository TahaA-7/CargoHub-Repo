# from .models import *
# from .serializers import *
import sqlite3
from enum import Enum


class DB_CRUD_Methods(Enum):
    INSERT = 1
    UPDATE = 2
    DELETE = 3
    SELECT_ONE = 4
    SELECT_ALL = 5


class DBManager:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path

    # private methods
    @staticmethod
    def __translate_enum_to_str(SQL_CRUD_action: DB_CRUD_Methods):
        # if SQL_CRUD_action == DB_CRUD_Methods.INSERT:
        #     return "add"
        # elif SQL_CRUD_action == DB_CRUD_Methods.UPDATE:
        #     return "change"
        # elif SQL_CRUD_action == DB_CRUD_Methods.DELETE:
        #     return "delete"
        # elif SQL_CRUD_action == DB_CRUD_Methods.SELECT_ONE | SQL_CRUD_action == DB_CRUD_Methods.SELECT_ALL:
        #     return "view"
        action_map = {
            DB_CRUD_Methods.INSERT: "add",
            DB_CRUD_Methods.UPDATE: "change",
            DB_CRUD_Methods.DELETE: "delete",
            DB_CRUD_Methods.SELECT_ONE | DB_CRUD_Methods.SELECT_ALL: "view",
        }
        return action_map.get(SQL_CRUD_action, None)

    # query string builder
    # if `pk` is a `str` it is a UUID
    def __query_string_builder(self, SQL_CRUD_action: DB_CRUD_Methods, table_name: str, pk: int|str = None, data_body: dict = None):
        if SQL_CRUD_action == DB_CRUD_Methods.INSERT:
            if not data_body:
                raise ValueError("Data body is required for INSERT operation.")
            columns = ", ".join(data_body.keys())
            placeholders = ", ".join(["?" for _ in data_body.values()])
            query_string = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            values = tuple(data_body.values())
        elif SQL_CRUD_action == DB_CRUD_Methods.SELECT_ONE:
            query_string = f"SELECT * FROM {table_name} WHERE id = ?"
            values = (pk,)
        elif SQL_CRUD_action == DB_CRUD_Methods.SELECT_ALL:
            query_string = f"SELECT * FROM {table_name}"
        elif SQL_CRUD_action == DB_CRUD_Methods.UPDATE:
            set_clause = ", ".join([f"{k} = ?" for k in data_body.keys()])
            query_string = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
            values = tuple(data_body.values()) + (pk,)
        elif SQL_CRUD_action == DB_CRUD_Methods.DELETE:
            query_string = f"DELETE FROM {table_name} WHERE id = ?"
            values = (pk,)
        else:
            raise ValueError("Invalid SQL action.")
        return query_string, values

    # standard DB manager func
    def __standard_db_manager_func(self, user_id, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int|str = None, data_body: dict = None):
        # First check the permission
        permission_bool = self.__permission_checker(user_id, SQL_change_action, table_name)
        if not (isinstance(permission_bool, bool) & permission_bool == True):
            raise Exception("ERROR: incorrect user_id, enum, table name, id or json body")
        # Second build the query string
        query_string, values = self.__query_string_builder(SQL_change_action, table_name, pk, data_body)
        # Now try to perform the SQL command with the (hopefully) built query string
        try:
            if SQL_change_action == DB_CRUD_Methods.SELECT_ONE:
                return query_string
            else:
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute(query_string, values)
                    conn.commit()
        except Exception as ex:
            return f"ERROR: {ex}"


    def __fetch_user_permissions(self, user_id):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Fetch group permissions
                cursor.execute("""
                    SELECT permission_id
                    FROM auth_group_permissions
                    WHERE group_id IN (
                        SELECT group_id FROM auth_user_groups WHERE user_id = ?
                    )
                """, (user_id,))
                group_permissions = [row[0] for row in cursor.fetchall()]

                # Fetch user-specific permissions
                cursor.execute("""
                    SELECT permission_id
                    FROM auth_user_user_permissions
                    WHERE user_id = ?
                """, (user_id,))
                user_permissions = [row[0] for row in cursor.fetchall()]

                return set(group_permissions + user_permissions)
        except Exception as ex:
            raise RuntimeError(f"Error fetching permissions: {ex}")


    def __permission_checker(self, user_id: int, SQL_action: DB_CRUD_Methods, table_name: str):
        permissions_list = self.__fetch_user_permissions(user_id)
        crud_action_str = self.__translate_enum_to_str(SQL_action)
        base_table = table_name.split("_")[0]

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id FROM auth_permission 
                    WHERE codename LIKE ? AND codename LIKE ?
                """, (f"%{base_table}%", f"%{crud_action_str}%"))
                required_permission = cursor.fetchone()
                if required_permission and required_permission[0] in permissions_list:
                    return True
                return False
        except Exception as ex:
            raise RuntimeError(f"Error fetching permissions: {ex}")


    # public methods
    def manage_auth_group(self, user_id: int, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int = None, data_body: dict = None):
        return self.__standard_db_manager_func(user_id, SQL_change_action, table_name, pk, data_body)

    def manage_auth_group_permissions(self, user_id: int, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int = None, data_body: dict = None):
        return self.__standard_db_manager_func(user_id, SQL_change_action, table_name, pk, data_body)

    # REMOVED: should only be auto-editable through migrations
    # def manage_auth_permission(self, user_id: int, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int = None, data_body: dict = None):
        # return self.__standard_db_manager_func(user_id, SQL_change_action, table_name, pk, data_body)

    def manage_auth_user_group(self, user_id: int, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int = None, data_body: dict = None):
        return self.__standard_db_manager_func(user_id, SQL_change_action, table_name, pk, data_body)

    def manage_auth_user_user_permissions(self, user_id: int, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int = None, data_body: dict = None):
        return self.__standard_db_manager_func(user_id, SQL_change_action, table_name, pk, data_body)

    # special user permission role manager
    def manage_user_permission_role(self, user_id_or_username: int|str, column_name: str, grant_role: bool):
        if column_name != "is_superuser" & column_name != "is_staff":
            return ValueError(f"the only valid columns are `is_superuser` and `is_staff`. Your input: {column_name}")

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                if isinstance(user_id_or_username, int):
                    cursor.execute(f"UPDATE auth_user SET {column_name} WHERE id = ?", (user_id_or_username))
                else:
                    cursor.execute(f"UPDATE auth_user SET {column_name} WHERE username = ?", (user_id_or_username))
            return True
        except Exception as ex:
            raise RuntimeError(f"Error updating permissions: {ex}")


    # Check methods
    def user_is_client(self, user_id: int):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT email FROM auth_user WHERE id = ?", (user_id))
                fetched_user_email = cursor.fetchone[0]

                cursor.execute(f"SELECT contact_email FROM clients WHERE contact_email = ?", (fetched_user_email))
                fetched_client_email = cursor.fetchone
                if len(fetched_client_email) != 0:
                    return True
        except Exception as ex:
            raise RuntimeError(f"Error fetching permissions: {ex}")




    # def query_string_builder(self, SQL_change_action: DB_CRUD_Methods, table_name: str, pk: int=None, data_body: dict=None):
    #     query_string = ""

    #     # Example: INSERT INTO table (column1,column2 ,..) VALUES( value1,	value2 ,...);
    #     if SQL_change_action == DB_CRUD_Methods.INSERT:
    #         query_string = f"INSERT INTO {table_name}"

    #         columns_tuple = tuple(data_body.keys())
    #         query_string += f"{columns_tuple} VALUES "

    #         values_tuple = tuple(data_body.values())
    #         query_string += f"{values_tuple}" + ";"

    #     # Example: UPDATE employees SET city = 'Toronto', state = 'ON', postalcode = 'M5P 2N7' WHERE employeeid = 4;
    #     elif SQL_change_action == DB_CRUD_Methods.UPDATE:
    #         query_string = f"UPDATE {table_name} SET "
    #         for k, v in data_body.items():
    #             query_string += f"{k} = {v}, "
    #         query_string = query_string[:len(query_string)-1] # removing the trailing `,` at the end
    #         query_string += f"WHERE id = {pk}" + ";"

    #     # Example: DELETE FROM table WHERE search_condition;
    #     elif SQL_change_action == DB_CRUD_Methods.DELETE:
    #         query_string = f"DELETE FROM {table_name}"
    #         query_string += f" WHERE id = {pk}" + ";"

    #     else:
    #         return ValueError(f"Invalid SQL action. Input: action: {SQL_change_action}, table_name: {table_name}, id={pk}, data: {json(data_body)}")

    #     return query_string

    # # Manage methods
    # def manage_auth_group(self, SQL_change_action: int|str, table_name: str, pk: int, data_body: dict):
    #     sqliteConnection = sqlite3.connect('db.sqlite3')
    #     cursor = sqliteConnection.cursor()

    #     query_string = self.query_string_builder(SQL_change_action, table_name, pk, data_body)
    #     if (query_string == ValueError): 
    #         return ValueError

    #     try:
    #         cursor.execute(query_string)
    #         sqliteConnection.commit(query_string)
    #     except Exception as ex:
    #         return (f"ERROR, we could not perform the action. Reason:\n{ex}")
    #     finally:
    #         if sqliteConnection:
    #             sqliteConnection.close()


    # ^^^ The commented code above was removed because it is unsafe against SQL injections as it had no query parameters ^^^
