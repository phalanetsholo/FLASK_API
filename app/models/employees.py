import psycopg2
from config import Config

def get_db_connection():
    conn = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    return conn
def create_employee(first_name, last_name, email, phone, department):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (first_name, last_name, email, phone, department) VALUES (%s, %s, %s, %s, %s)",     (first_name, last_name, email, phone, department))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees;')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return employees

def update_employee(id, first_name, last_name, email, phone, department):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET first_name = %s, last_name = %s, email = %s, phone = %s, department = %s WHERE id = %s',
                   (first_name, last_name, email, phone, department, id))
    conn.commit()
    cursor.close()
    conn.close()
    
    def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
