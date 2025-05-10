from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Given a string s containing only digits, return all possible valid IP addresses 
        that can be obtained by inserting dots into s. You are not allowed to reorder 
        or remove any digits in s. You may return the valid IP addresses in any order.

        A valid IP address consists of exactly four integers, each between 0 and 255, 
        separated by single dots, and cannot have leading zeros (except for "0" itself).

        Constraints:
        - 1 <= len(s) <= 20

        Example:
        Input: s = "25525511135"
        Output: ["255.255.11.135", "255.255.111.35"]
        """

        def isValid(segment: str) -> bool:
            # Segment must not have leading zeros unless it's "0"
            if len(segment) > 1 and segment[0] == "0":
                return False
            # Segment must be <= 255
            if int(segment) > 255:
                return False
            return True

        res = []

        def backtrack(idx: int, ip: str, depth: int):
            if idx >= len(s):
                return

            if depth == 0:
                if isValid(s[idx:]):
                    res.append(ip + s[idx:])
                return

            for i in range(idx, len(s)):
                remaining = len(s) - (i + 1)
                # can we form rest of segments using remaining
                if depth <= remaining <= depth * 3:
                    segment = s[idx:i+1]
                    if not isValid(segment):
                        # early return as well
                        return
                    backtrack(i + 1, ip + segment + ".", depth - 1)

        backtrack(0, "", 3)
        return res
