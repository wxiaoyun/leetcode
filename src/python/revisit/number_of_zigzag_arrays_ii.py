# TLE (due to python slowness)
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # let f_inc(i, j) = sum(k=0..j)(f_dec(i - 1, k))

        # A_inc = sum(k=0..0)(B_(i_1)(k)) = 0
        #         sum(k=0..1)(B_(i_1)(k)) = B_i-1_0
        #         sum(k=0..2)(B_(i_1)(k)) = B_i-1_0 + B_i-1_1
        #         sum(k=0..3)(B_(i_1)(k)) = B_i-1_0 + ... + B_i-1_2
        #         sum(k=0..m)(B_(i_1)(k)) = B_i-1_0 + ... + B_i-1_m-1
        #
        # [0 1 1 ... 1 1] = C
        # [0 0 1 ... 1 1]
        # [ ... ... ... ]
        # [0 0 0 ... 1 1]
        # [0 0 0 ... 0 1]
        # [0 0 0 ... 0 0]

        # A_1 = [1 1 ... 1 1]^T
        # A_n = AC^(n-1)

        # C^2 =
        # [0 1 1 ... 1 1]# [0 1 1 ... 1 1]= [0 0 1 ... m-3 m-2]
        # [0 0 1 ... 1 1]# [0 0 1 ... 1 1]  [0 0 0 ... m-4 m-3]
        # [ ... ... ... ]# [ ... ... ... ]  [ ... ... ... ... ]
        # [0 0 0 ... 1 1]# [0 0 0 ... 1 1]  [0 0 0 ... 0   1  ]
        # [0 0 0 ... 0 1]# [0 0 0 ... 0 1]  [0 0 0 ... 0   0  ]
        # [0 0 0 ... 0 0]# [0 0 0 ... 0 0]  [0 0 0 ... 0   0  ]

        m = r - l + 1
        A = [[1] * (2 * m)]
        C = []
        for i in range(m):
            row = []
            row.extend([0] * (m + i + 1))
            row.extend([1] * (m - 1 - i))
            assert len(row) == 2 * m
            C.append(row)
        for i in range(m):
            row = []
            row.extend([1] * i)
            row.extend([0] * (2 * m - i))
            assert len(row) == 2 * m
            C.append(row)
        # for row in C:
        #     print(row)
        # print()

        MOD = 10**9 + 7

        def mat_mul(a, b):
            l1, l2, l3, l4 = len(a), len(a[0]), len(b), len(b[0])
            assert l2 == l3

            c = [[0] * l4 for _ in range(l1)]
            for i in range(l1):
                for j in range(l4):
                    for k in range(l2):
                        c[i][j] += a[i][k] * b[k][j]
                        c[i][j] %= MOD
            return c

        def mat_exp(a, e: int):
            if e == 1:
                return a

            e1, e2 = e // 2, (e + 1) // 2
            a1 = mat_exp(a, e1)
            a2 = a1
            if e % 2 == 1:
                a2 = mat_mul(a2, a)
            return mat_mul(a1, a2)

        Cn = mat_exp(C, n - 1)
        # for row in Cn:
        #     print(row)
        An = mat_mul(A, Cn)
        return sum(An[0]) % MOD


# fast mat_mul using builtin zip and sum
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # let f_inc(i, j) = sum(k=0..j)(f_dec(i - 1, k))

        # A_inc = sum(k=0..0)(B_(i_1)(k)) = 0
        #         sum(k=0..1)(B_(i_1)(k)) = B_i-1_0
        #         sum(k=0..2)(B_(i_1)(k)) = B_i-1_0 + B_i-1_1
        #         sum(k=0..3)(B_(i_1)(k)) = B_i-1_0 + ... + B_i-1_2
        #         sum(k=0..m)(B_(i_1)(k)) = B_i-1_0 + ... + B_i-1_m-1
        #
        # [0 1 1 ... 1 1] = C
        # [0 0 1 ... 1 1]
        # [ ... ... ... ]
        # [0 0 0 ... 1 1]
        # [0 0 0 ... 0 1]
        # [0 0 0 ... 0 0]

        # A_1 = [1 1 ... 1 1]^T
        # A_n = AC^(n-1)

        # C^2 =
        # [0 1 1 ... 1 1]# [0 1 1 ... 1 1]= [0 0 1 ... m-3 m-2]
        # [0 0 1 ... 1 1]# [0 0 1 ... 1 1]  [0 0 0 ... m-4 m-3]
        # [ ... ... ... ]# [ ... ... ... ]  [ ... ... ... ... ]
        # [0 0 0 ... 1 1]# [0 0 0 ... 1 1]  [0 0 0 ... 0   1  ]
        # [0 0 0 ... 0 1]# [0 0 0 ... 0 1]  [0 0 0 ... 0   0  ]
        # [0 0 0 ... 0 0]# [0 0 0 ... 0 0]  [0 0 0 ... 0   0  ]

        m = r - l + 1
        A = [[1] * (2 * m)]
        C = []
        for i in range(m):
            row = []
            row.extend([0] * (m + i + 1))
            row.extend([1] * (m - 1 - i))
            assert len(row) == 2 * m
            C.append(row)
        for i in range(m):
            row = []
            row.extend([1] * i)
            row.extend([0] * (2 * m - i))
            assert len(row) == 2 * m
            C.append(row)
        # for row in C:
        #     print(row)
        # print()

        MOD = 10**9 + 7

        def mat_mul(a, b):
            l1, l2, l3, l4 = len(a), len(a[0]), len(b), len(b[0])
            assert l2 == l3

            bt = list(zip(*b))
            c = [
                [sum(aa * bb for aa, bb in zip(a[i], bt[j])) % MOD for j in range(l4)]
                for i in range(l1)
            ]
            return c

        def mat_exp(a, e: int):
            if e == 1:
                return a

            e1, e2 = e // 2, (e + 1) // 2
            a1 = mat_exp(a, e1)
            a2 = a1
            if e % 2 == 1:
                a2 = mat_mul(a2, a)
            return mat_mul(a1, a2)

        Cn = mat_exp(C, n - 1)
        # for row in Cn:
        #     print(row)
        An = mat_mul(A, Cn)
        return sum(An[0]) % MOD
