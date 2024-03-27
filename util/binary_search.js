function binary_search(arr, target) {
	let low = 0;
	let high = arr.length;

	while (low < high) {
		const mid = Math.floor((high - low) / 2 + low);

		if (arr[mid] < target) {
			low = mid + 1;
		} else {
			high = mid;
		}
	}

	return low;
}

const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

console.log(binary_search(arr, 0));
console.log(binary_search(arr, 1));
console.log(binary_search(arr, 2));
console.log(binary_search(arr, 3));
console.log(binary_search(arr, 4));
console.log(binary_search(arr, 5));
console.log(binary_search(arr, 7));
console.log(binary_search(arr, 9));
