class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    @classmethod
    def from_array(cls, data):
        root = TreeNode(data[0])
        for i in data[1:]:
            tmp_root = root
            n = TreeNode(i)
            while True:
                if n.val <= tmp_root.val:
                    if tmp_root.left:
                        tmp_root = tmp_root.left
                    else:
                        tmp_root.left = n
                        break
                else:
                    if tmp_root.right:
                        tmp_root = tmp_root.right
                    else:
                        tmp_root.right = n
                        break
        return cls(root)

    def __init__(self, root):
        self.root = root


if __name__ == '__main__':
    t = BinaryTree.from_array([4, 2, 7, 9, 6, 3, 1])
