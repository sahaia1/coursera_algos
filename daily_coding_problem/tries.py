'''
Problem # 11

Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def insert_word_into_trie(root, word):
    node = root
    for c in word:
        found = False
        for child in node.children:
            if child.val == c:
                node = child
                found = True
        if not found:
            new_node = Node(c)
            node.children.append(new_node)
            node = new_node


def insert_dict_into_trie(dictionary):
    root = Node('')
    for word in dictionary:
        insert_word_into_trie(root, word)
    return root


def build_suggestions(node, chars):
    suggestions = []

    def dfs(n, word_so_far):
        nonlocal suggestions
        if n:
            if not n.children:
                suggestions.append(word_so_far + [n.val])
            else:
                for child in n.children:
                    dfs(child, word_so_far + [n.val])

    for c in node.children:
        dfs(c, [])
    if suggestions:
        for i in range(len(suggestions)):
            import pdb
            pdb.set_trace()
            suggestions[i] = [chars] + suggestions[i]
    else:
        return [chars]
    return [''.join(s) for s in suggestions]


def query_trie(root, chars):
    node = root
    for char in chars:
        for child in node.children:
            if child.val == char:
                node = child

    return build_suggestions(node, chars)


def driver(dictionary):
    trie = insert_dict_into_trie(dictionary)
    print(query_trie(trie, 'de'))