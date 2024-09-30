"""
Crie um programa que cadastra um lista de tarefas do dia. Ao final, o programa deve exibir a lista de tarefas.

"""
# Lista de tarefa do dia
tarefa_dia = []

while True:
    try:
        nova_tarefa = input("Informe a nova tarefa que deseja fazer ao longo do dia: ")
        if nova_tarefa:
           tarefa_dia.append(nova_tarefa)
           print(f"{nova_tarefa} cadastrada.")
           continue
        else:
            break
    except Exception as e:
        print(f"Não foi possível cadastrar o nome. {e}")


for tarefa in tarefa_dia:
    print(tarefa)  
