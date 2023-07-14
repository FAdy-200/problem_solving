# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from USEFUL_CODES.LC import *


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj: DefaultDict[int, List[TreeNode]] = defaultdict(list)
        d: Deque[TreeNode] = deque()
        d.append(root)
        while d:
            node = d.popleft()
            if node.left:
                adj[node.left.val].append(node)
                adj[node.val].append(node.left)
                d.append(node.left)
            if node.right:
                adj[node.right.val].append(node)
                adj[node.val].append(node.right)
                d.append(node.right)
        d: Deque[Tuple[int, int]] = deque()
        d.append((target.val, k))
        seen = {target.val}
        ans = []
        while d:
            node, dist = d.popleft()
            seen.add(node)
            if dist != 0:
                for i in adj[node]:
                    if i.val not in seen:
                        d.append((i.val, dist - 1))
            else:
                ans.append(node)
        return ans


S = Solution()
tree = create_tree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])
X = S.distanceK(tree, tree, 2)
print(X)
