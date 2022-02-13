import time
from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is not a TreeNode or not None.
        """
        self._root = root
        self._size = 0 if root is None else 1

        if root is not TreeNode and root is not None:
            raise ValueError(f'root is not a TreeNode')

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError('Key is not an integer')

        if self._root is None:
            self._root = TreeNode(key, value)
        else:
            n = self._root
            prev = self._root
            while n != None:
                if n.key == key:
                    raise KeyError(f'The key is already in the tree')
                prev = n
                if key < n.key:
                    n = n.left
                else:
                    n = n.right
            if prev.key < key:
                prev.right = TreeNode(key, value, parent=prev)
            else:
                prev.left = TreeNode(key, value, parent=prev)
        self._size += 1

    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        if not isinstance(key, int):
            raise ValueError('Key is not an integer')

        if self._root is None:
            raise KeyError('Key is not present in the tree.')
        else:
            n = self._root
            while n != None and n.key != key:
                if key < n.key:
                    n = n.left
                else:
                    n = n.right
            if n is None:
                raise KeyError('Key is not present in the tree.')
            else:
                return n

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""

        return self._size

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        if not isinstance(key, int):
            raise ValueError('Key is not an integer')

        node = self.find(key)
        return node.value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError(f'Key is not an integer')

        if self._root is None:
            raise KeyError('key in not in the tree')

        a = self.find(key)
        if a.left is None and a.right is None:
            if a.parent is not None:
                if a.key < a.parent.key:
                    a.parent.left = None
                else:
                    a.parent.right = None
            else:
                self._root = None
            return

    # Hint: The following 3 methods can be implemented recursively, and 
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root

        # This is needed in the case that there are no nodes.
        return self.recursion_inorder(node)

    def recursion_inorder(self, node: TreeNode):
        if not node:
            return iter(())
        if node is not None:
            yield from self.recursion_inorder(node.left)
            yield node
            yield from self.recursion_inorder(node.right)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        return self.recursion_preorder(node)

    def recursion_preorder(self, node: TreeNode):
        if not node:
            return iter(())

        if node is not None:
            yield node
            yield from self.recursion_preorder(node.left)
            yield from self.recursion_preorder(node.right)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root

        return self.recursion_postorder(node)

    def recursion_postorder(self, node: TreeNode):
        if not node:
            return iter(())

        if node is not None:
            yield from self.recursion_postorder(node.left)
            yield from self.recursion_postorder(node.right)
            yield node

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]:
        yield from self.preorder()

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        if self._root is None:
            return True
        return self.check_val(self._root)

    def check_val(self, node):
        if node is None:
            return True
        if node.right is not None and node.right.key > node.key:
            return False
        if node.left is not None and node.left.key > node.key:
            return False
        r = self.check_val(node.right)
        l = self.check_val(node.left)
        return l and r

    def return_min_key(self) -> TreeNode:
        """Return the node with the smallest key."""
        if self._root is None:
            return None
        for a in self.inorder():
            return a

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for finding the key both in the list and in the BST.
        
           Return the numbers of comparisons for both, the list and the BST
        """

        python_list = list(node.key for node in self.preorder())
        for i, x in enumerate(python_list):
            if key == x:
                index = i
        n = self.find(key)
        tuple = (index, n.depth)
        return tuple

    @property
    def height(self) -> int:
        """Return height of the tree."""
        h = 0
        for n in self.preorder():
            if n.depth > h:
                h = n.depth
            return h

    @property
    def is_complete(self) -> bool:
        """Return if the tree is complete."""
        a = 2 ** (self.height + 1) - 1
        l = len(list(self.preorder()))
        if a == l:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self.inorder())})"

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)
