import re
from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        n = len(code)
        code_reg = "^[a-zA-Z0-9_]+$"
        valid_biz_line = set(["electronics", "grocery", "pharmacy", "restaurant"])

        valid_indices = []
        for i in range(n):
            if not isActive[i]:
                continue
            if businessLine[i] not in valid_biz_line:
                continue
            if not re.search(code_reg, code[i]):
                continue
            valid_indices.append(i)

        valid_indices.sort(key=lambda i: (businessLine[i], code[i]))
        return [code[i] for i in valid_indices]
