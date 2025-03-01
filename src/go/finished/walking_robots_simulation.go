package leetcode

import (
	"fmt"
	"math"
)

// https://leetcode.com/problems/walking-robot-simulation

func robotSim(commands []int, obstacles [][]int) int {
	// check is obstacle in O(1)
	obs_lookup := make(map[string]bool)
	for _, obs := range obstacles {
		x, y := obs[0], obs[1]
		key := fmt.Sprintf("%d,%d", x, y)
		obs_lookup[key] = true
	}
	is_obs := func(x int, y int) bool {
		key := fmt.Sprintf("%d,%d", x, y)
		return obs_lookup[key]
	}

	// change dir utility functions
	directions := []string{"N", "E", "S", "W"}
	dir_to_idx := make(map[string]int)
	for i, dir := range directions {
		dir_to_idx[dir] = i
	}
	dir_to_delta := map[string][]int{
		"N": {0, 1},
		"E": {1, 0},
		"S": {0, -1},
		"W": {-1, 0},
	}
	change_dir := func(cmd int, dir string) string {
		idx := dir_to_idx[dir]
		if cmd == -2 {
			idx = (idx - 1 + len(directions)) % len(directions)
		} else if cmd == -1 {
			idx = (idx + 1 + len(directions)) % len(directions)
		} else {
			panic("Invalid cmd for change dir")
		}
		return directions[idx]
	}

	pow := func(num int, exp int) int {
		return int(math.Pow(float64(num), float64(exp)))
	}

	max_dist := 0
	i, j := 0, 0
	dir := "N"
	for _, cmd := range commands {
		if cmd < 0 {
			dir = change_dir(cmd, dir)
			continue
		}

		dist := cmd
		delta := dir_to_delta[dir]
		dx, dy := delta[0], delta[1]
		for k := 0; k < dist; k++ {
			if is_obs(i+dx, j+dy) {
				break
			}
			i, j = i+dx, j+dy
		}

		new_dist := pow(i, 2) + pow(j, 2)
		if new_dist > max_dist {
			max_dist = new_dist
		}
	}

	return max_dist
}
