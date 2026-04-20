class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        email_idx = {} # email -> email_idx
        emails = [] # set of unique emails
        email_acc = {} # email_idx -> acc_idx

        m = 0
        for acc_idx, acc in enumerate(accounts):
            for i in range(1, len(acc)):
                email = acc[i]
                if email in email_idx:
                    continue
                
                email_idx[email] = m
                emails.append(email)
                email_acc[m] = acc_idx

                m += 1
        
        graph = { c : [] for c in range(m) }
        for acc in accounts:
            for i in range(2, len(acc)):
                idx1 = email_idx[acc[i]]
                idx2 = email_idx[acc[i - 1]]
                graph[idx1].append(idx2)
                graph[idx2].append(idx1)
        
        email_group = defaultdict(list) # acc_idx -> unique emails
        visited = set()
        def bfs(start, acc_idx):
            q = deque([start])
            visited.add(start)
            while q:
                node = q.popleft()
                email_group[acc_idx].append(emails[node])
                for nxt in graph[node]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

        for email_idx in range(m):
            if email_idx not in visited:
                bfs(email_idx, email_acc[email_idx])
        
        res = []
        for acc_idx in email_group:
            name = accounts[acc_idx][0]
            res.append([name] + sorted(email_group[acc_idx]))
        
        return res