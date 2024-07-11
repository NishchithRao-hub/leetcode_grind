class Solution:
    def simplifyPath(self, path: str) -> str:
        output = []
        directory = path.split('/')
        for dir in directory:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if output:
                    output.pop()
            else:
                output.append(dir)
        return '/' + '/'.join(output)
