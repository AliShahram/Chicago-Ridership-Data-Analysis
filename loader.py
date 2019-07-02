import requests
import json
import psycopg2
import pandas as pd

response = requests.get('https://data.cityofchicago.org/resource/5eg2-c264.json')
data = json.loads(response.text)


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user = "",
                            password = "",
                            host = "",
                            port = "",
                            database = "")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Connection Successful")
        except (Exception) as error:
            print("Could not connect to the database:", error)


    def close_connection(self):
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    def create_table(self):
        try:
            create_table_command = "CREATE TABLE cta" + """(
                    stop_id  integer PRIMARY KEY,
                    on_street   varchar(50),
                    cross_street    varchar(50),
                    routes  integer,
                    boardings  decimal,
                    alightings  decimal,
                    month  timestamp,
                    latitude decimal,
                    longitude  decimal
            )"""
            self.cursor.execute(create_table_command)
            print("Table was successfuly created")

        except (Exception, psycopg2.DatabaseError) as error:
            print ("Error while creating PostgreSQL table", error)


    def delete_table(self, name):
        try:
            delete_table_command = "DROP TABLE " + name
            self.cursor.execute(delete_table_command)
            print("Table " + name + " successfuly dropped")
        except (Exception, psycopg2.DatabaseError) as error:
            print ("Error while dropping PostgreSQL table", error)


    def insert_record(self, record):
        try:
            insert_command = """INSERT INTO cta (
                    stop_id,
                    on_street,
                    cross_street,
                    routes,
                    boardings,
                    alightings,
                    month,
                    latitude,
                    longitude)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            self.cursor.execute(insert_command, record)
            print("Record successfuly added to table cta")

        except (Exception, psycopg2.DatabaseError) as error:
            print ("Error while adding record to PostgreSQL table", error)


    def get_graph_data(self, xaxis_name, yaxis_name):
        x_values = []
        y_values = []
        self.cursor.execute("select " + xaxis_name + ", " + yaxis_name
                            + " from cta")
        result = self.cursor.fetchall()
        for i in result:
            x_values.append(i[0])
            y_values.append(i[1])
        return x_values, y_values


    def get_table_data(self):
        query = """ select * from cta"""
        df = pd.read_sql_query(query, self.connection)
        return df


    def get_agg_data(self, xaxis_name, yaxis_name):
        x_values = []
        y_values = []

        if yaxis_name == 'boardings' or yaxis_name == 'alightings':
            self.cursor.execute("select " + xaxis_name + ", sum (" + yaxis_name
                                + ") from cta group by " + xaxis_name)
        elif yaxis_name == 'stop_id' or yaxis_name == 'routes':
            self.cursor.execute("select " + xaxis_name + ", count (" + yaxis_name
                                + ") from cta group by " + xaxis_name)

        result = self.cursor.fetchall()
        for i in result:
            x_values.append(i[0])
            y_values.append(i[1])
        return x_values, y_values


    def get_routes(self):
        query = """select distinct(routes) from cta"""
        self.cursor.execute(query)
        total = self.cursor.fetchall()
        return total


    def get_mean_route(self, route_num):
        query  = """select sum(boardings) +  sum(alightings), count(boardings) from cta where routes = """ + str(route_num)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        total = result[0][0]
        count = result[0][1]
        return total/count

    def get_express_route(self):
        routes = self.get_routes()
        labels = []
        values = []

        for i in routes:
            route = i[0]
            labels.append(route)
            values.append(self.get_mean_route(route))
        return labels, values






"""
db = DatabaseConnection()
db.create_table()
limit = 0
for row in data:
        record = [row['stop_id'], row['on_street'], row['cross_street'],
        row['routes'], row['boardings'], row['alightings'], row['month'], str(row['location']['coordinates'][0]),
        str(row['location']['coordinates'][1])]
        db.insert_record(record)
"""
