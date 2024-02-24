import psycopg2


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def connection(self):
        try:
            connection =  psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            return connection
        except Exception as e:
            print('Error : ', e)


    def insert(self, table: str, data: dict):
        try:
            columns = ', '.join(data.keys())
            values = ', '.join(['%s' for _ in data.values()])
            
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            
            with self.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, tuple(data.values()))
                conn.commit()
        except psycopg2.IntegrityError as e:
            print(f"Skipped insertion due to IntegrityError: {e}")

    def select(self, table: str, condition: str = None, limit: int = None, random: bool = False, params: tuple = ()):
        query = f"SELECT * FROM {table}"

        if condition:
            query += f" WHERE {condition}"
        if random:
            query += f" ORDER BY RANDOM()"
        if limit is not None:
            query += f" LIMIT {limit}"

        

        with self.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        return rows
    
    def update(self, table: str, data: dict, condition: str = None, params: tuple = ()):
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause}"

        if condition:
            query += f" WHERE {condition}"

        with self.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, tuple(data.values()) + params)
            conn.commit()

    def delete(self, table: str, condition: str = None, params: tuple = ()):
        query = f"DELETE FROM {table}"

        if condition:
            query += f" WHERE {condition}"

        with self.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
            conn.commit()
    