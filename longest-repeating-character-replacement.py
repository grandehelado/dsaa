class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # optimized for O(n)
        count = {}

        result = 0

        left = 0

        maxf = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            maxf = max(maxf, count[s[right]])

            # while (right - left + 1) - max(count.values()) > k:
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
