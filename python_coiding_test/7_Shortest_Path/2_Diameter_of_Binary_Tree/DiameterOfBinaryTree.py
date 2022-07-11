"""
이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라
Input: root = [1,2,3,4,5]
Output: 3
"""


class Solution(object):
    longest = 0

    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest
