from prettytable import PrettyTable 
import json
import os

def loadToDo(fileToDo):
    if os.path.exists(fileToDo):
        with open(fileToDo, 'r') as file:
            return json.load(file)
    return {}

def saveToDo(toDo,fileToDo):
    with open(fileToDo, 'w') as file:
        json.dump(toDo,file)

fileToDo = 'json.list'
toDo = loadToDo(fileToDo)

def addTask():
    newTask = input('Adicione sua nova tarefa: ')
    newDescription =  input('Adicione uma descrição para essa tarefa: ')
    toDo[newTask] = newDescription
    print ('Tarefa adicionada com sucesso') 
    saveToDo (toDo,fileToDo)
    printToDo(toDo)
    
def printToDo(toDo):
    table = PrettyTable()  
    table.field_names = ['#','Terafa','Descrição']
    
    if not toDo:
        print('Nenhuma tarefa encontrada!')
    else:
        for idx, (task, description) in enumerate(toDo.items(), start=1):
            table.add_row([idx, task, description])
    print(table)    

def removeTask(toDo):
    printToDo(toDo)
    taskToRemove = input('Qual tarefa você deseja remover? ')
    if taskToRemove in toDo:
        toDo.pop(taskToRemove)
        print('Tarefa removida com sucesso')
    else:
        print('Tarefa não encontrada')
    printToDo(toDo)



while True:
    choice = int(input('''
        Bem vindo ao seu To-Do List
    Digite 1 para adicionar uma no tarefa
    Digite 2 para remover uma tarefa
    Digite 3 para visualizar sua lista de tarefas
    Digite 4 para sair                  
    '''))
    
    if choice == 1:
        addTask()
    elif choice == 2:
        removeTask(toDo)
    elif choice == 3:
        printToDo(toDo)
    else:
        print('Até mais!')
        break



