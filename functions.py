# definisco una variabile di default nel caso la funzione venga richiamata senza parametri
FILEPATH = "todos.txt"
def get_todo(list_todos=FILEPATH):
    with open(list_todos, "r") as file:
        todos = file.readlines()
    return todos

def write_todo(todos_arg, list_todos=FILEPATH):
    # with open(list_todos, "r") as file:
    #     todos = file.readlines()
    # todos.append(todo + "\n")

    with open(list_todos, "w") as file:
        file.writelines(todos_arg)




if __name__ == "__main__":
    print("hello")