import io

def carregar_dados(conn, df, tabela, colunas):
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    try:
        cur.copy_from(output, tabela, null="", columns=colunas)
        conn.commit()
        print(f"✅ Dados inseridos com sucesso na tabela '{tabela}'")
    except Exception as e:
        print(f"❌ Erro ao inserir na tabela '{tabela}':", e)
        conn.rollback()
