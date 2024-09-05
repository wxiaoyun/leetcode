package util

func MergeSort(arr []int) []int {
	merge := func(a, b []int) []int {
		output := make([]int, 0, len(a)+len(b))
		i, j := 0, 0

		for i < len(a) && j < len(b) {
			if a[i] > b[j] {
				output = append(output, b[j])
				j++
			} else {
				output = append(output, a[i])
				i++
			}
		}

		for i < len(a) {
			output = append(output, a[i])
			i++
		}

		for j < len(b) {
			output = append(output, b[j])
			j++
		}

		return output
	}

	var sort func([]int) []int
	sort = func(arr []int) []int {
		if len(arr) <= 1 {
			return arr
		}

		mid := len(arr) / 2
		a, b := sort(arr[:mid]), sort(arr[mid:])
		return merge(a, b)
	}

	return sort(arr)
}
