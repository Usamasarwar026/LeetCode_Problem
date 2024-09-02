from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Reduce k by the total sum of chalk using modulus
        k = k % sum(chalk)
        i = 0
        # Iterate through the students
        while k > 0:
            k -= chalk[i]
            if k < 0:
                return i  # Return the index of the student who needs to replace the chalk
            i += 1
        return i  # This line is just for syntax and won't actually be reached

if __name__ == "__main__":
    # Example test case
    solution = Solution()
    chalk = [5, 1, 5]
    k = 22
    result = solution.chalkReplacer(chalk, k)
    print(f"The student who needs to replace the chalk is at index: {result}")
