package util

func QuickSort(arr []int) {
	partition := func(i, j int) int {
		arr[i], arr[j] = arr[j], arr[i]
		pivot := arr[j]

		k := i
		for p := i; p < j; p++ {
			if arr[p] < pivot {
				arr[p], arr[k] = arr[k], arr[p]
				k++
			}
		}

		arr[k], arr[j] = arr[j], arr[k]
		return k
	}

	var sort func(int, int)
	sort = func(i, j int) {
		if i >= j {
			return
		}

		p := partition(i, j)
		sort(i, p-1)
		sort(p+1, j)
	}

	sort(0, len(arr)-1)
}
