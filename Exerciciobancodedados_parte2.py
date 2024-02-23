import sqlite3

conexao = sqlite3.connect('C:\\Users\\macka\\Desktop\\Data Analytics\\Projects\\banco.db')

cursor = conexao.cursor()

#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY, nome VARCHAR(100), idade INT, saldo float);')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1,"Ana", "31", "2000")')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2,"Bianca", "26", "1900")')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3,"Caio", "36", "2800")')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4,"Daniele", "21", "700")')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5,"Eliseu", "42", "5000")')

#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
#for clientes in dados:
#    print(clientes)  

#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for clientes in dados:
#    print(clientes)    

#dados = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#for clientes in dados:
#   print(clientes)  

#dados = cursor.execute('SELECT * FROM clientes WHERE saldo > 1000')
#for clientes in dados:
#   print(clientes)

#cursor.execute('DELETE FROM clientes WHERE id=3')

#cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor INT, saldo float);')

#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1,"Ana", "Ameixa", "2")')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2,"Bianca", "Biscoito", "5")')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4,"Daniele", "Danone", "8")')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5,"Eliseu", "Edamame", "10")')

#dados = cursor.execute('SELECT * FROM clientes RIGHT JOIN compras ON clientes.id = compras.id')
#for clientes in dados:
#	print(clientes)

#cursor.execute('ALTER TABLE compras DROP COLUMN saldo')

#dados = cursor.execute('SELECT * FROM compras WHERE id IN (SELECT id FROM clientes)')
#for clientes in dados:
#	print(clientes)

conexao.commit()
conexao.close