package leetcode

func letterCombinations(digits string) []string {
	if digits == "" {
		return []string{}
	}
	return helper("", digits)
}

func helper(accum string, remaining string) []string {
	if remaining == "" {
		return []string{accum}
	}

	first := int(remaining[0])
	var one []string
	var two []string
	var three []string
	var four []string

	if first == '2' {
		one = helper(accum+"a", remaining[1:])
		two = helper(accum+"b", remaining[1:])
		three = helper(accum+"c", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '3' {
		one = helper(accum+"d", remaining[1:])
		two = helper(accum+"e", remaining[1:])
		three = helper(accum+"f", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '4' {
		one = helper(accum+"g", remaining[1:])
		two = helper(accum+"h", remaining[1:])
		three = helper(accum+"i", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '5' {
		one = helper(accum+"j", remaining[1:])
		two = helper(accum+"k", remaining[1:])
		three = helper(accum+"l", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '6' {
		one = helper(accum+"m", remaining[1:])
		two = helper(accum+"n", remaining[1:])
		three = helper(accum+"o", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '7' {
		one = helper(accum+"p", remaining[1:])
		two = helper(accum+"q", remaining[1:])
		three = helper(accum+"r", remaining[1:])
		four = helper(accum+"s", remaining[1:])
		return append(one, append(two, append(three, four...)...)...)
	}

	if first == '8' {
		one = helper(accum+"t", remaining[1:])
		two = helper(accum+"u", remaining[1:])
		three = helper(accum+"v", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '9' {
		one = helper(accum+"w", remaining[1:])
		two = helper(accum+"x", remaining[1:])
		three = helper(accum+"y", remaining[1:])
		four = helper(accum+"z", remaining[1:])
		return append(one, append(two, append(three, four...)...)...)
	}

	return []string{}
}
