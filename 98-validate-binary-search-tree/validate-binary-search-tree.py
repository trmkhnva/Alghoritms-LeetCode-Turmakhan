class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, low, high):
            # Если дошло до конца и ошибок не нашли то все работает
            if not node:
                return True
            
            # Если число в узле вылезло за границы то дерево неправильное
            if not (low < node.val < high):
                return False
            
            #проверяем лево и право рекурсией,
            return check(node.left, low, node.val) and \
                   check(node.right, node.val, high)
        
        # Запускаем проверку с бесконечными границами в начале
        return check(root, float('-inf'), float('inf'))
        