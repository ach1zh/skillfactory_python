#M11-L4

'''
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

root = TreeNode("C:")
documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))

root.add_child(TreeNode('secret.key'))

def print_file_system(node, indent=""):
    
    print(indent + node.name + ("/" if not node.children else "\\"))
    
    if node.children:
        for child in node.children:
            print_file_system(child, indent + "  ")

print("\n--->\n")
print_file_system(root)


###
print("\n--->\n")

class Queue:
   def __init__(self):
       self.queue = []

   def is_empty(self):
       return len(self.queue) == 0

   def enqueue(self, item):
       self.queue.append(item)

   def dequeue(self):
       if not self.is_empty():
           return self.queue.pop(0)
       else:
           print("Queue is empty")
           return None

#queue = Queue()
#queue.enqueue((root, ""))
#for qqq in queue:
#    print(qqq)

def breadth_first_search_for_file(root, target_file):
    queue = Queue()
    queue.enqueue((root, ""))

    while not queue.is_empty():
        
        current_node, current_path = queue.dequeue()
        current_path += current_node.name + "/"

        if current_node.name == target_file:
            return current_path

        for child in current_node.children:
            queue.enqueue((child, current_path))

    return None

file_path = breadth_first_search_for_file(root, 'Report.docx')
if file_path: # Если файл был найден
    print(file_path[:-1])    
# C:/Documents/Report.docx

print("\n--->\n")

'''

#Задание 22.3
#print("\n--> Задание 22.3 -->\n")

'''
Как мы уже выяснили, текущий алгоритм поиска в ширину файла в N-арном дереве файловой
системы не учитывает ситуацию, когда в системе может быть несколько файлов с одним и тем же именем. 
Для решения этой проблемы вам предлагается модифицировать алгоритм таким образом,
чтобы он возвращал все пути к файлам с заданным именем.
'''

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

root = TreeNode("D:")
documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))
pictures.add_child(TreeNode("Report.docx"))

root.add_child(TreeNode('secret.key'))

def print_file_system(node, indent=""):
    
    print(indent + node.name + ("/" if not node.children else "\\"))
    
    if node.children:
        for child in node.children:
            print_file_system(child, indent + "  ")

print("\n--->\n")
print_file_system(root)

class Queue:
   def __init__(self):
       self.queue = []

   def is_empty(self):
       return len(self.queue) == 0

   def enqueue(self, item):
       self.queue.append(item)

   def dequeue(self):
       if not self.is_empty():
           return self.queue.pop(0)
       else:
           print("Queue is empty")
           return None

def breadth_first_search_for_file(root, target_file):
    # Создаем очередь для обхода в ширину
    queue = Queue()
    queue.enqueue((root, ""))

    result = []
    while not queue.is_empty():
        current_node, current_path = queue.dequeue()

        # Обновляем текущий путь, добавляя текущее имя узла
        current_path += current_node.name + "/"

        if current_node.name == target_file:
            # Если текущий узел содержит искомый файл, возвращаем текущий путь
            #return current_path
            result.append(current_path)

        # Добавляем детей текущего узла в очередь для дальнейшего обхода
        for child in current_node.children:
            queue.enqueue((child, current_path))

    # Если файл не найден в дереве, возвращаем None
    if result:
        return result
    else: 
        return None    

print("\n---Result---\n")

file_path = breadth_first_search_for_file(root, 'Report.docx')
if file_path: # Если файл был найден
    print(file_path)    
    print("\n") 