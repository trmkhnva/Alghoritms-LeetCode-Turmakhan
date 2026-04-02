class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def walk(node):
            if not node:
                return
            
            
            ans.append(node.val)
            
            
            walk(node.left)
            walk(node.right)
            
        # Запускаем 
        walk(root)
        
        # Возвращаем список
        return ans