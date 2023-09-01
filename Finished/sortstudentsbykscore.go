package leetcode

func sortTheStudents(score [][]int, k int) [][]int {
	quickSort(score, 0, len(score)-1, k)
	return score
}

func quickSort(score [][]int, start, end, k int) {
	if start >= end {
		return
	}

	pivot := partition(score, start, end, k)
	quickSort(score, start, pivot-1, k)
	quickSort(score, pivot+1, end, k)
}

func partition(score [][]int, start, end, k int) int {
	pivot := end

	i := start
	for j := start; j < pivot; j++ {
		if score[j][k] > score[pivot][k] {
			swap(score, i, j)
			i++
		}
	}

	swap(score, i, pivot)
	return i
}

func swap(score [][]int, a, b int) {
	score[a], score[b] = score[b], score[a]
}
