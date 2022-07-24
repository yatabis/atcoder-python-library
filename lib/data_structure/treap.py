from random import random
from typing import Optional


class TreapNode:
    def __init__(self, value):
        self.value = value
        self.priority = random()
        self.left: Optional[TreapNode] = None
        self.right: Optional[TreapNode] = None
        self.parent: Optional[TreapNode] = None

    def rotate_left(self):
        pivot = self.right
        self.right = pivot.left
        if pivot.left is not None:
            pivot.left.parent = self
        pivot.left = self
        pivot.parent = self.parent
        self.parent = pivot
        if pivot.parent is not None:
            parent = pivot.parent
            if parent.left is self:
                parent.left = pivot
            elif parent.right is self:
                parent.right = pivot

    def rotate_right(self):
        pivot = self.left
        self.left = pivot.right
        if pivot.right is not None:
            pivot.right.parent = self
        pivot.right = self
        pivot.parent = self.parent
        self.parent = pivot
        if pivot.parent is not None:
            parent = pivot.parent
            if parent.left is self:
                parent.left = pivot
            elif parent.right is self:
                parent.right = pivot

    def tree(self):
        nodes = []
        if self.left is not None:
            nodes += self.left.tree()
        nodes.append(str(self))
        if self.right is not None:
            nodes += self.right.tree()
        return nodes

    def __str__(self):
        return f"{self.value}({self.priority} p{self.parent.value if self.parent else ''})"


class Treap:
    def __init__(self):
        self.root: Optional[TreapNode] = None

    def _rotate_left(self, node: TreapNode):
        if node is self.root:
            self.root = node.right
        node.rotate_left()

    def _rotate_right(self, node: TreapNode):
        if node is self.root:
            self.root = node.left
        node.rotate_right()

    def contains(self, x) -> bool:
        node = self.root
        while node is not None:
            if x == node.value:
                return True
            if x < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, x):
        new_node = TreapNode(x)

        if self.root is None:
            self.root = new_node
            return

        node = self.root
        while True:
            if x < node.value:
                if node.left is None:
                    new_node.parent = node
                    node.left = new_node
                    break
                node = node.left
            else:
                if node.right is None:
                    new_node.parent = node
                    node.right = new_node
                    break
                node = node.right

        while new_node.parent is not None and new_node.priority > new_node.parent.priority:
            if new_node is new_node.parent.left:
                self._rotate_right(new_node.parent)
            elif new_node is new_node.parent.right:
                self._rotate_left(new_node.parent)
            else:
                raise ValueError

    def delete(self, x):
        if self.root is None:
            raise KeyError('delete(): Treap is empty')

        node = self.root
        while node.value != x:
            if x < node.value:
                if node.left is None:
                    raise KeyError(x)
                node = node.left
            else:
                if node.right is None:
                    raise KeyError(x)
                node = node.right

        while node.left is not None or node.right is not None:
            if node.left is None:
                self._rotate_left(node)
            else:
                self._rotate_right(node)

        if node is node.parent.left:
            node.parent.left = None
        elif node is node.parent.right:
            node.parent.right = None
        else:
            raise ValueError

    def lt(self, x) -> Optional:
        if self.root is None:
            return None

        node = self.root
        lt = None
        while node is not None:
            value = node.value
            if value < x:
                if lt is None or value > lt:
                    lt = value
                node = node.right
            else:
                node = node.left
        return lt

    def le(self, x) -> Optional:
        if self.root is None:
            return None

        node = self.root
        le = None
        while node is not None:
            value = node.value
            if value <= x:
                if le is None or value > le:
                    le = value
                node = node.right
            else:
                node = node.left
        return le

    def gt(self, x) -> Optional:
        if self.root is None:
            return None

        node = self.root
        gt = None
        while node is not None:
            value = node.value
            if value > x:
                if gt is None or value < gt:
                    gt = value
                node = node.left
            else:
                node = node.right
        return gt

    def ge(self, x) -> Optional:
        if self.root is None:
            return None

        node = self.root
        ge = None
        while node is not None:
            value = node.value
            if value >= x:
                if ge is None or value < ge:
                    ge = value
                node = node.left
            else:
                node = node.right
        return ge

    def __str__(self):
        return f"Treap<{', '.join(self.root.tree())}>"
