"""
이진 트리의 최대 깊이를 구하라

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
import collections



def maxDepth(self, root):
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    # BFS 반복 횟수 == 깊이
    return depth
