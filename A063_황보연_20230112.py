class Solution:
    def addBinary(self, a: str, b: str) -> str:
        new_a = int(a,2)
        new_b = int(b,2)
        sum_a_b = new_a + new_b

        temp = format(sum_a_b, "b")

        return str(temp)