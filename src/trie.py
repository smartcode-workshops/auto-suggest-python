class TrieNode:
    def __init__(self, value=' '):
        self.children = {}
        self.is_end_of_word = False
        self._value = value

    def has_child(self, c):
        return c in self.children


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if not current.has_child(c):
                current.children[c] = TrieNode(c)
            current = current.children[c]
        if current.is_end_of_word:
            return False
        current.is_end_of_word = True
        return True

    def auto_suggest(self, prefix):
        current_node = self.root
        for c in prefix:
            if not current_node.has_child(c):
                return []
            current_node = current_node.children[c]
        return self.get_all_words_with_prefix(current_node, prefix)

    def get_all_words_with_prefix(self, root, prefix):
        return None

    def get_all_words(self):
        return self.get_all_words_with_prefix(self.root, "")

    def print_trie_structure(self):
        print("\nroot")
        self._print_trie_nodes(self.root)

    def _print_trie_nodes(self, root, format=" ", is_last_child=True):
        if root is None:
            return

        print(f"{format}", end='')

        if is_last_child:
            print("└─", end='')
            format += "  "
        else:
            print("├─", end='')
            format += "│ "

        print(f"{root._value}")

        child_count = len(root.children)
        i = 0
        children = sorted(root.children.items())

        for key, child in children:
            i += 1
            is_last = i == child_count
            self._print_trie_nodes(child, format, is_last)

    def get_spelling_suggestions(self, word):
        first_letter = word[0]
        suggestions = []
        words = self.get_all_words_with_prefix(self.root.children[first_letter], first_letter)

        for w in words:
            distance = self.levenshtein_distance(word, w)
            if distance <= 2:
                suggestions.append(w)

        return suggestions

    def levenshtein_distance(self, s, t):
        m = len(s)
        n = len(t)
        d = [[0] * n for _ in range(m)]

        if m == 0:
            return n

        if n == 0:
            return m

        for i in range(m + 1):
            d[i][0] = i

        for j in range(n + 1):
            d[0][j] = j

        for j in range(n):
            for i in range(m):
                cost = 0 if s[i] == t[j] else 1
                d[i][j] = min(min(d[i][j] + 1, d[i][j] + 1), d[i][j] + cost)

        return d[m - 1][n - 1]