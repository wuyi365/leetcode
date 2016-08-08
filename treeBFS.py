class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def traverse2(rootnode):
    result = []
    stack = [rootnode]
    while stack:
        level = []
        n = len(stack)
        for i in range(n):
            node = stack.pop(0)
            level.append(node.value)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        result.append(level)

    return result

def traverse3(rootnode):
    result = []
    stack = [rootnode]
    while stack:
        level = []
        n = len(stack)
        print '-----n'
        print n
        for i in range(n):
            node = stack.pop(0)
            print node.value,
            level.append(node.value)
            print '*'
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        result.append(level)
        print 

    return result

def traverse4(rootnode):
    thislevel = [rootnode]
    while thislevel:
        nextLevl = []
        for n in thislevel:
            print n.value,

            if n.left:nextLevl.append(n.left)
            if n.right:nextLevl.append(n.right)
        print
        thislevel = nextLevl



t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

print traverse2(t)
print traverse3(t)
#traverse4(t)