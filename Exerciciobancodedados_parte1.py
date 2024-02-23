import sqlite3

conexao = sqlite3.connect('C:\\Users\\macka\\Desktop\\Data Analytics\\Projects\\banco.db')

cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), indade INT, curso VARCHAR(100));')
#cursor.execute('ALTER TABLE alunos RENAME COLUMN indade TO idade') 

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1,"Ana", "12", "Artes")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2,"Beatriz", "13", "Biologia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3,"Caio", "12", "Ciências")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4,"Eric", "11", "Educação Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5,"Fernanda", "13", "Física")')


#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#    print(alunos)

#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
#for alunos in dados:
#    print(alunos)    

#dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
#for aluno in dados:
#    print(aluno)

#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for aluno in dados:
#    print(aluno)

#cursor.execute('UPDATE alunos SET idade=15 Where id=2')
#cursor.execute('DELETE FROM alunos WHERE id=3')

conexao.commit()
conexao.close