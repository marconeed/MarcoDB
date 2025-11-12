# Em main.py (ATUALIZADO PARA TESTE DE ESTRESSE MÁXIMO)

import os
from pager import Pager
from btree import BPlusTree

DB_FILENAME = "meu_banco_stress_max.db" # Novo nome

def main():
    if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)

    pager = Pager(DB_FILENAME)
    tree = BPlusTree(pager)
    
    print("\n--- INSERINDO 25000 ITENS (TESTE DE SPLIT DE NÓ INTERNO) ---")
    
    # --- MUDANÇA AQUI ---
    num_items = 25000
    
    for i in range(num_items):
        key = f"chave_{str(i).zfill(5)}" # zfill(5) para '00001'
        value = f"valor_de_teste_{i}"
        tree.insert(key, value)
    
    print("\n--- BUSCANDO DADOS PÓS-MÚLTIPLOS-SPLITS ---")
    
    print(f"Buscando 'chave_00001': {tree.search('chave_00001')}")
    print(f"Buscando 'chave_12000': {tree.search('chave_12000')}")
    print(f"Buscando 'chave_24999': {tree.search('chave_24999')}")
    
    print("\nSalvando banco de dados...")
    pager.close()
    
    # --- Teste de Persistência ---
    print("\n--- REABRINDO O BANCO (TESTE DE PERSISTÊNCIA) ---")
    pager = Pager(DB_FILENAME)
    tree = BPlusTree(pager)

    print(f"Buscando 'chave_05000': {tree.search('chave_05000')}")
    print(f"Buscando 'chave_20000': {tree.search('chave_20000')}")
    pager.close()
    
    print("Feito.")

if __name__ == "__main__":
    main()