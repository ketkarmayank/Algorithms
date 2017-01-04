"""Learning how to work with Segment Trees. Also learning how to work with Docstrings
"""

class Node(object):
    """This will act as Node element
    Args:
        start_idx(int): Suggests where the range starts
        end_idx(int): Suggests where the range ends
        value(int): Stores sum till this point
        left(Node): Stores reference to left child
        right(Node): Stores reference to right child
    """
    def __init__(self, start_idx=None, end_idx=None, value=None, left=None, right=None):
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.value = value
        self.left = left
        self.right = right

class SegmentTree(object):
    """Segment tree implementation to learn why ranges work better
    Args:
        None
    """
    def __init__(self):
        self.root = None

    def populate(self, input_array=None):
        """Populates the tree with sum of range elements
        Args:
            input_array(int[]): input of array of elements
        Returns:
            None
        """
        if input is None:
            raise Exception('Null input array')
        self.root = self.populate_node_helper(input_array, 0, len(input_array) - 1)

    def populate_node_helper(self, arr, start_idx, end_idx):
        """Helper to populate the segment tree
        Args:
            arr(int[]): Array to be converted to segment tree
            start_idx(int): Suggests where the range starts
            end_idx(int): Suggests where the range ends
        Returns:
            Node that is to be attached
        """
        if start_idx == end_idx:
            return Node(None, None, arr[start_idx], None, None)
        mid = (end_idx + start_idx) // 2
        left_child = self.populate_node_helper(arr, start_idx, mid)
        right_child = self.populate_node_helper(arr, mid+1, end_idx)
        value = left_child.value + right_child.value
        return Node(start_idx, end_idx, value, left_child, right_child)

    def printAll(self, node=None):
        """Print all nodes with start index and end index + sum
        Args:
            node(Node): node for the tree
        Returns:
            None
        """
        if node is None:
            node = self.root
        print(
            ' series: '
            + str(node.value)
            + ' start_index: '
            + str(node.start_idx)
            + ' end_index: '
            + str(node.end_idx)
        )
        if node.left is not None:
            self.printAll(node.left)
        if node.right is not None:
            self.printAll(node.right)



INPUT = [1, 3, 5, 6, 7]

TREE = SegmentTree()

TREE.populate(INPUT)

TREE.printAll()
