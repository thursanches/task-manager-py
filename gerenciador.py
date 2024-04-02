# gerenciador de tarefas
# De forma resumida é um check-list.
def adicionar_tarefa(tarefas, descricao_tarefa):
    
    # tarefa: descricao da tarefa 
    #completada: indicar se essa tarefa foi completada ou não
    tarefa = {"tarefa": descricao_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {descricao_tarefa} foi adicionada com sucesso!")
    return

tarefas = []

while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Cadastrar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == 1:
        descricao_tarefa = input("Digite a descricao da tarefa: ")
        adicionar_tarefa(tarefas, descricao_tarefa)

    elif escolha == 6:
        break
    
print("Programa finalizado")
