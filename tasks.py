class Node:
    """Клас для представлення вузла дерева."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    """Клас для представлення двійкового дерева пошуку."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставка нового елемента в дерево."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # Якщо ключ вже існує, ігноруємо його

    # --- Завдання 1: Пошук найбільшого значення ---
    def find_max(self):
        """Знаходить найбільше значення у двійковому дереві пошуку."""
        if self.root is None:
            return None
        
        current = self.root
        # Найбільший елемент завжди знаходиться в крайньому правому вузлі
        while current.right is not None:
            current = current.right
        return current.val

    # --- Завдання 2: Пошук найменшого значення ---
    def find_min(self):
        """Знаходить найменше значення у двійковому дереві пошуку."""
        if self.root is None:
            return None
        
        current = self.root
        # Найменший елемент завжди знаходиться в крайньому лівому вузлі
        while current.left is not None:
            current = current.left
        return current.val

    # --- Завдання 3: Пошук суми всіх значень ---
    def find_sum(self):
        """Знаходить суму всіх значень у двійковому дереві пошуку."""
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        """Рекурсивний допоміжний метод для підрахунку суми."""
        if node is None:
            return 0
        
        # Сума = значення поточного вузла + сума лівого піддерева + сума правого піддерева
        return node.val + self._sum_recursive(node.left) + self._sum_recursive(node.right)

# --- Демонстрація роботи з Двійковим деревом пошуку ---
print("--- Демонстрація роботи з Двійковим деревом пошуку ---")
bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80, 25, 75]
for el in elements:
    bst.insert(el)

print(f"Елементи в дереві: {elements}")
print(f"Найбільше значення в дереві: {bst.find_max()}")  # Очікуваний результат: 80
print(f"Найменше значення в дереві: {bst.find_min()}")    # Очікуваний результат: 20
print(f"Сума всіх значень в дереві: {bst.find_sum()}")      # Очікуваний результат: 450
print("-" * 50)

# Частина 2: Система коментарів (Завдання 4)
class Comment:
    """
    Клас для представлення ієрархічної структури коментарів.
    """
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додає нову відповідь до коментаря."""
        self.replies.append(reply)

    def remove(self):        
        self.text = "Цей коментар було видалено."
        self.author = "" # Автор видаленого коментаря не відображається
        self.is_deleted = True

    def display(self, level=0):        
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        
        for reply in self.replies:
            reply.display(level + 1)

# --- Демонстрація роботи системи коментарів (за вашим прикладом) ---
print("\n--- Демонстрація роботи системи коментарів ---")

# Створення коментарів
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# Додавання відповідей першого рівня
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Додавання відповіді другого рівня
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# "Видалення" коментаря. Його текст змінюється, але відповіді залишаються.
# Зверніть увагу: метод .remove() викликається на самому об'єкті, який "видаляється".
reply1.remove() 

# Відображення всієї гілки коментарів
root_comment.display()
print("-" * 50)