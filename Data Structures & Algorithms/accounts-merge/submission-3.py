class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        email_idx = {} # email -> email_idx
        emails = [] # set of unique emails
        email_acc = {} # email_idx -> account_idx

        m = 0
        for acc_idx, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in email_idx:
                    continue

                email_idx[email] = m
                emails.append(email)
                email_acc[m] = acc_idx 

                m += 1

        graph = { c : [] for c in range(m) }
        for a in accounts:
            for i in range(2, len(a)):
                id1 = email_idx[a[i]]
                id2 = email_idx[a[i - 1]]
                graph[id1].append(id2)
                graph[id2].append(id1)
        
        visited = set()
        email_group = defaultdict(list)
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
        
        for n in range(m):
            if n not in visited:
                bfs(n, email_acc[n])
        
        res = []
        for acc_idx in email_group:
            name = accounts[acc_idx][0]
            res.append([name] + sorted(email_group[acc_idx]))
        
        return res