import sqlite3

con = sqlite3.connect("Alimentos.db")

con.execute("PRAGMA foreign_keys = ON;")

table_user = '''
CREATE TABLE IF NOT EXISTS user (
id_user INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL);
'''

con.execute(table_user)

table_task = '''
CREATE TABLE IF NOT EXISTS task (
task_id INTEGER PRIMARY KEY,
id_user INTEGER,
desc_task TEXT NOT NULL,
sector_n TEXT NOT NULL,
priority TEXT NOT NULL,
cad_data TEXT NOT NULL,
status TEXT NOT NULL,
FOREIGN KEY (id_user) REFERENCES user(id_user) ON DELETE SET NULL);
'''

con.execute(table_task)

############################################
#INSERT ITEMS INTO DB
############################################

insert_user = '''
INSERT INTO user(id_user,name,email)
VALUES  (1,'Ana Silva', 'ana.silva@email.com'),
        (2,'João Souza', 'joao.souza@email.com'),
        (3,'Maria Oliveira', 'maria.oliveira@email.com'),
        (4,'Carlos Pereira', 'carlos.pereira@email.com'),
        (5,'Fernanda Costa', 'fernanda.costa@email.com'),
        (6,'Rafael Lima', 'rafael.lima@email.com'),
        (7,'Beatriz Gomes', 'beatriz.gomes@email.com'),
        (8,'Lucas Andrade', 'lucas.andrade@email.com');
'''

con.execute(insert_user)


insert_task = '''
INSERT INTO task(task_id,id_user,desc_task,sector_n,priority,cad_data,status)
VALUES  (1,1, 'Preparar relatório mensal', 'Financeiro', 'Alta', '2025-11-12', 'Em andamento'),
        (2,2, 'Revisar código de produção', 'TI', 'Média', '2025-11-10', 'Concluído'),
        (3,3, 'Organizar documentos de clientes', 'Administrativo', 'Baixa', '2025-11-11', 'Pendente'),
        (4,2, 'Planejar reunião com fornecedores', 'Compras', 'Alta', '2025-11-13', 'Pendente'),
        (5,4, 'Atualizar planilhas de estoque', 'Logística', 'Média', '2025-11-09', 'Em andamento'),
        (6,5, 'Criar campanha de marketing digital', 'Marketing', 'Alta', '2025-11-08', 'Em andamento'),
        (7,6, 'Implementar backup automático do sistema', 'TI', 'Alta', '2025-11-10', 'Pendente'),
        (8,7, 'Elaborar proposta comercial', 'Vendas', 'Média', '2025-11-12', 'Concluído'),
        (9,8, 'Manutenção preventiva em servidores', 'Infraestrutura', 'Alta', '2025-11-11', 'Em andamento'),
        (10,1, 'Analisar custos de projetos anteriores', 'Financeiro', 'Baixa', '2025-11-07', 'Concluído');
'''

con.execute(insert_task)




con.commit()
con.close()