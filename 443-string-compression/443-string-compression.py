class Solution:
    def compress(self, chars: List[str]) -> int:
        count, i = 1, 0
        for j in range(1, len(chars)+1):
            if j< len(chars) and chars[j] == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 1
        return i