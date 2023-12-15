class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        num = len(board)
    
        def relabel(label):
            r, c = divmod(label-1,num)
            if r % 2 == 0:
                return num-1-r, c
            else:
                return num-1-r, num-1-c

        visited = set()
        queue = collections.deque()
        queue.append((1,0)) 
        while queue:
            label, step = queue.popleft()
            r, c = relabel(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == num*num:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= num*num and new_label not in visited:
                    visited.add(new_label)
                    queue.append((new_label, step+1))
        return -1
