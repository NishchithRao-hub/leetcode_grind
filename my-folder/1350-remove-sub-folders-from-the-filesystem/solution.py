class Trie:
    def __init__(self):
        self.children = {}
        self.end_of_folder = False

    def add(self, path: str) -> None:
        curr = self

        for f in path.split("/"):
            if f not in curr.children:
                curr.children[f] = Trie()
            curr = curr.children[f]
        curr.end_of_folder = True

    def prefix_search(self, path: str) -> None:
        curr = self
        folders = path.split("/")
        for i in range(len(folders)-1):
            curr = curr.children[folders[i]]
            if curr.end_of_folder:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)

        result = []
        for f in folder:
            if not trie.prefix_search(f):
                result.append(f)

        return result

# Time -> O(N*L) (Twice)
# Space -> (N*L)
# (N is number of folders and L is avg length of folders)
