class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def addPath(result,node,path =''):
    if not node.left and not node.right:
        result.append(path + str(node.value))
    if node.left:
        print '-----left'
        addPath(result, node.left,path + str(node.value) + '->', )
    if node.right:
        print '-----right'
        addPath(result, node.right, path + str(node.value) + '->')
    print result
    return result

def treeDFS(root):
    if not root:
        return root

    result = []

    return addPath(result, root, path = '')


def binaryTreePaths(root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.value)]
        res = binaryTreePaths(root.left) + binaryTreePaths(root.right)
        print res
        
        return [str(root.value) + '->' + i for i in res]



t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

print treeDFS(t)
print '-----------'
# print binaryTreePaths(t)
# print '----------------treeprint----'
# treeprint(t)