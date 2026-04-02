class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def find(node):
            if not node:
                return
            
            # уходим до конца налево
            find(node.left)
            
            #вправо
            find(node.right)
            
            # в конце записываем число
            ans.append(node.val)
            
        find(root)
        return ans