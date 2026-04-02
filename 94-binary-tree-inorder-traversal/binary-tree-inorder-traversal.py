class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = [] # здесь хранятся все числа
        
        def walk(node):
            if not node: # Если узла нет, то ничего не делаем
                return
            
            walk(node.left)  # Сначала идем до конца влево
            ans.append(node.val) # Записываем число, которое нашли
            walk(node.right) # что будет справа
            
        walk(root) 
        return ans # Отдаем готовый список
        