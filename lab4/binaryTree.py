class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

def main():
    n = input()
    bst = BSTNode(n)
    print(bst.data)
    print(bst.left)
    print(bst.right)
main()

