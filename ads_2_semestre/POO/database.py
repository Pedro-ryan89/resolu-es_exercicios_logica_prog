def criar_tabela():
    try:
        conn = conectar()
        conn.execute("""CREATE TABLE IF NOT EXISTS usuarios (id integer PRIMARY KEY,
                    nome text NOT NULL, email text NOT NULL UNIQUE,
                    senha text NOT NULL,perfil text NOT NULL)""")
        conn.commit()
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        if conn:
            conn.close()