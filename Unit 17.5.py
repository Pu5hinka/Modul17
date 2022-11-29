G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}
D = {k : 100 for k in G.keys()} # расстояния
P = {k : None for k in G.keys()}
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от неё до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин

D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин
P = {k : None for k in G.keys()} # предки

pointer = 'Владимирская' # куда должны прийти
while pointer is not None: # перемещаемся, пока не придём в стартовую точку
    print(pointer)
    pointer = P[pointer]

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v] # то фиксируем его
            P[v] = min_k # и записываем как предок
    U[min_k] = True # просмотренную вершину помечаем
print(D)
print(P)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки


node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

node_root.post_order()