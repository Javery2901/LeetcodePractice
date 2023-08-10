import random
# choices(['red', 'black', 'green'], [18, 18, 2], k=6)


class Solution:
    def weight_distribution(self, weight, frequency):
        index_list = [0, 1, 2, 3]  # index
        count = [0] * len(weight)  # [0,0,0,0]
        freq = 0
        while freq < frequency:
            chosen_indices = random.choices(index_list, weights=weight, k=2)
            if chosen_indices[0] == chosen_indices[1]:
                continue
            # print(chosen_indices[0], chosen_indices[1])
            count[chosen_indices[0]] += 1
            count[chosen_indices[1]] += 1
            freq += 1
        res = [count[i] / sum(count) for i in range(len(count))]
        return res  # [0.128559, 0.2288005, 0.3001, 0.3425405]

    def weight_distribution2(self, weight, frequency):
        # 用sample，从[0,1,2,3]不放回的不重复的取出两个，每次乘以权重系数
        index_list = [0, 1, 2, 3]  # index
        count = [0] * len(weight)
        for _ in range(frequency):
            chosen = random.sample(index_list, 2)  # # element is different
            index1, index2 = chosen[0], chosen[1]
            count[index1] += weight[index1]
            count[index2] += weight[index2]
        res = [count[i] / sum(count) for i in range(len(count))]
        return res


s = Solution()
weight = [10, 20, 30, 40]
frequency = 1000000
print(s.weight_distribution2(weight, frequency))