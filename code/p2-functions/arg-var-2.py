# Programa: arg-var-2.py
# Creación: 25/07/2025

def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', '')
    }
    print(conn_params)
    # we then connect to the database (commented out)
    # db.connect(**conn_params)

# Main code
connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')
