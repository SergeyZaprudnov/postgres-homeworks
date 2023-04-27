"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

# соединение с бд по заданным параметрам
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='sixteen'
)

# создание курсора для выполнения операций
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/employees_data.csv', newline='', encoding='utf-8') as csvfile:
                read = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(read)
                for row in read:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", row)

            with open('north_data/customers_data.csv', newline='', encoding='utf-8') as csvfile:
                read = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(read)
                for row in read:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)

            with open('north_data/orders_data.csv', newline='', encoding='utf-8') as csvfile:
                read = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(read)
                for row in read:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)

finally:
    conn.close()
