import unittest


class Solution(object):
    def isMatch(self, s, p):
        s = ' ' + s
        p = ' ' + p
        
        table = [[False] * len(s) for _ in range (len(p))]
        table[0][0] = True
        for i in range(2, len(p)):
            table[i][0] = table[i - 2][0] and p[i] == '*'

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] != "*":
                    table[i][j] = table[i - 1][j - 1] and (p[i] == s[j] or p[i] == '.')
                else:
                    table[i][j] = table[i - 2][j] or table[i - 1][j]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        table[i][j] = table[i][j] | table[i][j - 1]
        return table[-1][-1]
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1




class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()