class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emailIdx = {}        # maps email -> unique index
        emails = []          # list of emails by index
        emailToAcc = {}      # maps email index -> account ID
        m = 0                # running index for emails
        
        # We are assigning a unique index to each unique email.
        # Also, we remember which account ID each email came from.
        # Loop through each account.For each email:
        #     - If it's not seen before, assign it an index m.
        #     - Track which account (accId) it came from.
        for accId, acc in enumerate(accounts):
            for i in range(1, len(acc)):
                email = acc[i]
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = m
                emailToAcc[m] = accId
                m += 1

        # Build the graph:
        # For each account, connect all its emails together in an undirected graph.
        # We do this by linking each email to the previous one in the account list.
        # This way, emails belonging to the same account form a connected component.

        adj = [[] for _ in range(m)]
        for a in accounts:
            for i in range(2, len(a)):
                id1 = emailIdx[a[i]]
                id2 = emailIdx[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)

        emailGroup = defaultdict(list)  # index of acc -> list of emails
        visited = [False] * m

        # Perform DFS - Marks nodes (emails) as visited.
        # Collects all reachable emails (connected emails) into emailGroup[accId].
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)

        # Run DFS on All Unvisited Emails. For each email:If it's not visited,
        # start a DFS from it. All connected emails will get grouped into the same account.
        for i in range(m):
            if not visited[i]:
                dfs(i, emailToAcc[i])

        # Each accId now maps to a set of merged emails.
        # We get the name of that account using the original accounts[accId][0].
        # Sort the emails alphabetically and append to result.
        result = []
        for accId in emailGroup:
            name = accounts[accId][0]
            result.append([name] + sorted(emailGroup[accId]))

        return result


# Time: O((N * M) log(N * M)) or Time: O(N * M + E + V log V)
# N * M: processing each email in each account.
# E: total edges in the graph.
# V log V: sorting emails per account.

# Space: O(N * M)
# - Graph + visited array + mappings.

        
