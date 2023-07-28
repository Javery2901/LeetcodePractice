import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ls = [i for i in range(len(accounts))]
        # ls = [0, 1, 2, 3]
        dic = {}  # {email: index}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                # 遍历每个account 里的email，若第一次出现，则正常加入
                # 若已经存在，则说明应该合并。则利用并查集，将accounts账户里的序列号合并在一起
                if email in dic:
                    self.union(i, dic[email], ls)
                else:
                    dic[email] = i
        # print(ls)  # [0, 0, 2, 3]
        # 现在只需要根据并查集的ls，输入
        account = collections.defaultdict(list)
        for email, index in dic.items():
            account[self.find(index, ls)].append(email)
        # print(account)
        res = []
        for index, emails in account.items():
            ls = [accounts[index][0]] + sorted(emails)
            res.append(ls)
        return res

    def find(self, x, ls):
        if x == ls[x]:
            return x
        cur = x
        while cur != ls[cur]:
            cur = ls[cur]
        return cur

    def union(self, x, y, ls):
        if self.find(x, ls) == self.find(y, ls):
            return
        x_parent = self.find(x, ls)
        y_parent = self.find(y, ls)
        ls[x_parent] = y_parent
        return


s = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
test = s.accountsMerge(accounts)
print(test)