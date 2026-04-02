class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Если дерево пустое, то новое число и станет корнем
        if not root:
            return TreeNode(val)

        def put(node, value):
            # Если новое число больше текущего, идем направо
            if value > node.val:
                if not node.right:
                    node.right = TreeNode(value) # Нашли пустое место - вставляем
                else:
                    put(node.right, value) # Идем дальше направо
            # Если меньше - идем налево
            else:
                if not node.left:
                    node.left = TreeNode(value) # Нашли пустое место - вставляем
                else:
                    put(node.left, value) # Идем дальше налево
        
        # Запускаем нашу функцию
        put(root, val)
        
        # Возвращаем обновленное дерево
        return root