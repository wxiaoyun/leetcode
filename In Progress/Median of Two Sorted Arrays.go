package inprogress

import "math"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	len1 := len(nums1)
	len2 := len(nums2)

	if len1 > len2 {
		return findMedianSortedArrays(nums2, nums1)
	}

	l := 0
	r := len1 - 1

	for l <= r {
		mid1 := (l + r) / 2
		mid2 := (len1+len2+1)/2 - mid1

		var nums1leftmax, nums1rightmin, nums2leftmax, nums2rightmin int
		if mid1 == 0 {
			nums1leftmax = math.MinInt
		} else {
			nums1leftmax = nums1[mid1-1]
		}

		if mid1 == len1 {
			nums1rightmin = math.MaxInt
		} else {
			nums1rightmin = nums1[mid1]
		}

		if mid2 == 0 {
			nums2leftmax = math.MinInt
		} else {
			nums2leftmax = nums2[mid2-1]
		}

		if mid2 == len2 {
			nums2rightmin = math.MaxInt
		} else {
			nums2rightmin = nums2[mid2]
		}

		if nums1leftmax <= nums2rightmin && nums2leftmax <= nums1rightmin {
			if (len1+len2)%2 == 0 {
				return (math.Max(float64(nums1leftmax), float64(nums2leftmax)) +
					math.Min(float64(nums1rightmin), float64(nums2rightmin))) / 2
			} else {
				return math.Max(float64(nums1leftmax), float64(nums2leftmax))
			}
		} else if nums1leftmax > nums2rightmin {
			r = mid1 - 1
		} else {
			l = mid1 + 1
		}
	}
	return -1.0
}
