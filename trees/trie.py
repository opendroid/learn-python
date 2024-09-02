class TrieNode:
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.children = {}
        return


class Trie:
    def __init__(self, value):
        self.root = TrieNode(value)
        return

    def add(self, path):
        current = self.root
        current.count += 1
        for action in path:
            # Traverse the tree
            if action not in current.children:
                current.children[action] = TrieNode(action)

            current.children[action].count += 1
            current = current.children[action]
        return


def add_recursive(node: TrieNode, value):
    if len(value) == 0:
        return
    if value[0] not in node.children:
        node.children[value[0]] = TrieNode(value[0])
    node.children[value[0]].count += 1
    add_recursive(node.children[value[0]], value[1:])
    return


def print_trie(node: TrieNode, prefix):

    prefix += f"{node.value}({node.count})"
    if len(node.children) == 0:
        print(prefix)

    for child in node.children:
        print_trie(node.children[child], prefix + "  ")
    return


top = Trie('#')
top.add("ABC")
top.add("ABC")
top.add("ADE")
top.add("BDE")
top.add("BDE")
top.add("BDE")
top.add("BDEF")
top.add("BDEFG")

print_trie(top.root, "")
second = TrieNode("#")
add_recursive(second, "ABC")
add_recursive(second, "ABC")
add_recursive(second, "ADE")
add_recursive(second, "BDE")
add_recursive(second, "BDE")
add_recursive(second, "BDE")
add_recursive(second, "BDEF")
add_recursive(second, "BDEFG")
print("Second:")
print_trie(second, "")
