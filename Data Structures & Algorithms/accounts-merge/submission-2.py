class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        email_idx = {} # email -> id
        emails = [] # set of emails of all accounts
        email_acc = {} # email_idx -> account id

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

        email_groups = defaultdict(list)
        visited = set()
        def bfs(start, acc_idx):
            q = deque([start])
            visited.add(start)
            while q:
                node = q.popleft()
                email_groups[acc_idx].append(emails[node])
                for nb in graph[node]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
    
        for i in range(m):
            if i not in visited:
                bfs(i, email_acc[i])

        res = []
        for acc_idx in email_groups:
            name = accounts[acc_idx][0]
            res.append([name] + sorted(email_groups[acc_idx]))
        
        return res