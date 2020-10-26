import logging

class PatriciaTrie:
    def __init__(self):
        self.root = Node()

    def find(self, prefix, node=None, collector=""):
        if not node: return self.find(prefix, self.root)

        logging.debug(f"Looking for prefix {prefix} at {node.elem}")
        if not prefix:
            res = []
            if node.leaf:
                logging.debug(f"Found leaf {node.elem}")
                res.append(collector)
            for child in node.children:
                logging.debug(f"Looking for leafs in {node.elem}")
                res.extend(self._find(prefix, child, collector+child.elem))
            logging.debug(f"Result for {node.elem}: {res}")
            return res

        for child in node.children:
            if prefix.startswith(child.elem):
                return self._find(prefix[len(child.elem):], child, collector+child.elem)

        return []

    def add(self, elem):
        (node, split_idx, elem_rest) = self.find_longest_match(elem, self.root)

        def new_child():
            return Node(elem=elem_rest, parent=node, leaf=True, children=[])

        def split_node(leaf):
            (oelem, ochild, oleaf) = (node.elem, node.children, node.leaf)
            node.leaf = leaf
            node.elem = oelem[:split_idx]
            node.children = []

            node.children.append(Node(elem=oelem[split_idx:], parent=node, leaf=oleaf, children=ochild))

        # elem already found in trie
        # just make sure node is marked as leaf
        if not split_idx and not elem_rest:
            node.leaf = True
            return

        # - elem not in trie
        # - parent node exhausted
        # This can happen if parent is root, or elem is larger than
        # largest matching elem in trie so far
        if not split_idx:
            node.children.append(Node(elem=elem_rest, parent=node, leaf=True, children=[]))
            return

        # - elem already found in trie
        # - elem ends in the middle of a node
        # This can happen if an existing node up to index and its
        # parents make up the entire elem. We need to split
        # the node at split_idx and mark it as leaf.
        if not elem_rest:
            old_elem = node.elem
            old_children = node.children
            old_leaf = node.leaf

            node.leaf = True
            node.elem = old_elem[:split_idx]
            node.children = []

            split_node = Node(elem=old_elem[split_idx:], parent=node, leaf=old_leaf, children=old_children)

            node.children.append(split_node)
            return


        # - elem not found in trie
        # - node up to split_idx and its parent make up elem
        # Node needs to be split at split_idx (preserving leaf status for split off old node) and
        # a new child is added for elem
        old_children = node.children
        old_leaf = node.leaf

        node.leaf = False
        node.elem = old_elem[:split_idx]
        node.children = []

        node_a = Node(elem=old_elem[split_idx:], parent=node, leaf=old_leaf, children=old_children)
        node_b = Node(elem=elem_rest, parent=node, leaf=True, children=[])
        node.children.append(node_a)
        node.children.append(node_b)

    def find_longest_match(self, elem, node):
        for child in node.children:
            if not child.elem or not elem: continue

            # child does not match
            if child.elem[0] is not elem[0]: continue

            # child matches completely
            if elem.startswith(child.elem):
                # special case: the node already exists
                if len(elem) == len(child.elem):
                    return (child, None, None)
                # recourse down the trie
                return self.find_longest_match(elem[len(child.elem):], child)

            # elem matches completely, implies that elem is shorter
            # than child.elem. Split child at len(elem)
            if child.elem.startswith(elem):
                return (child, len(elem), None)

            # child does not match completely but at least first char matches
            # find longest split index
            for i in range(len(elem)):
                if elem[i] == child.elem[i]: continue
                else: return (child, i, elem[i:])

        # No child(-prefix) matched, create another child
        return (node, None, elem)

    def to_dot(self):
        print("graph {")
        self._to_dot(self.root)
        print("}")

    def _to_dot(self, node):
        for child in node.children:
            if not node.elem: print(f'root -- "{child.elem}";')
            else: print(f'"{node.elem}" -- "{child.elem}";')

            if child.leaf:
                print(f'"{child.elem}" [color=blue];')

            self._to_dot(child)

class Node:
    def __init__(self, elem=None, parent=None, children=[],
                 leaf=False, offset=0, title=None, info=None):
        self.elem = elem
        self.parent = parent
        self.children = children
        self.leaf = leaf

        # payload
        self.offset = offset
        self.title = title if title else elem
        self.info = info
