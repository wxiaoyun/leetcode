function quicksort(arr) {
	function swap(i, j) {
		const temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	function partition(start, end) {
		let pivot = arr[end];
		let pivot_index = start;

		for (let i = start; i < end; i++) {
			if (arr[i] < pivot) {
				swap(i, pivot_index);
				pivot_index++;
			}

			swap(pivot_index, end);
			return pivot_index;
		}
	}

	function quicksort_helper(start, end) {
		if (start >= end) return;
		const pivot_index = partition(start, end);
		quicksort_helper(start, pivot_index - 1);
		quicksort_helper(pivot_index + 1, end);
	}

	return quicksort_helper(0, arr.length - 1);
}

function expect(a, b) {
	if (a !== b) {
		console.log("Expected ", a, " but got ", b);
	}
}

const arr = [3, 2, 1, 4, 5];
quicksort(arr);

expect(arr, [1, 2, 3, 4, 5]);
