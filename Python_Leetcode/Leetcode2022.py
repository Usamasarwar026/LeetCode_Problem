from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        total = len(original)
        if m * n != total:
            return []
        answer = []
        itr = 0
        for i in range(1, m + 1):
            arr = []
            while itr < i * n:
                arr.append(original[itr])
                itr += 1
            answer.append(arr)
        return answer

if __name__ == "__main__":
    solution = Solution()
    original = [1, 2, 3, 4]
    m, n = 2, 2
    print(solution.construct2DArray(original, m, n))  # Output: [[1, 2], [3, 4]]
