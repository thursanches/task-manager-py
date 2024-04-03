# gerenciador de tarefas
# De forma resumida é um check-list.
def adicionar_tarefa(tarefas, descricao_tarefa):
    
    # tarefa: descricao da tarefa 
    #completada: indicar se essa tarefa foi completada ou não
    tarefa = {"tarefa": descricao_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {descricao_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        print(f"{indice}. [{status}] {tarefa["tarefa"]}")
    return

def atualizar_tarefas(tarefas, indice_tarefa, nova_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    if indice_tarefa_ajustado <= 0 or indice_tarefa_ajustado > len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = nova_tarefa
        print(f"Tarefa {indice_tarefa} foi atualizada para{nova_tarefa}!")
    else:
        print("Indice não existe!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print("Tarefa {indice_tarefa} marcada como completada")
    return

def deletar_tarefas_completadas(tarefas, indice_tarefa):
    print("Tarefa {indice_tarefa} deletada")
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas deletadas com sucesso!")
    return

tarefas = []

while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Cadastrar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        descricao_tarefa = input("Digite a descricao da tarefa: ")
        adicionar_tarefa(tarefas, descricao_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite a nova tarefa: ")
        atualizar_tarefas(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja marcar como completada: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break
    
print("Programa finalizado")
