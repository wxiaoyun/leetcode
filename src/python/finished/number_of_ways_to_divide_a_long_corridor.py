# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # number of seats since the previous divider
        seat_cnt = 0
        # number of plants since the previous seat
        plnt_cnt = 0

        MOD = int(1e9) + 7
        ways = 1
        for c in corridor:
            if c == "P":
                plnt_cnt += 1
                continue

            assert c == "S"
            if seat_cnt < 2:
                seat_cnt += 1
                plnt_cnt = 0
                continue

            # seat_cnt == 2
            ways = (ways * (plnt_cnt + 1)) % MOD
            seat_cnt = 1
            plnt_cnt = 0

        return ways if seat_cnt == 2 else 0


# SPPPPPPPS
#  PPP
# SPS
# SS
#  PPPPPPPPPPPPPPPPP
# SPPPPPPPPPPPPPPPPS
#  PPPPP
# SPS
#  PPPPPP
# SPS
#  PP
# SPS
#  PPP
# SPS
#  PP
# SS
#  PPPPP
# SPPS
# SPP
