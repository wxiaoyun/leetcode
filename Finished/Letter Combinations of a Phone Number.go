package leetcode

func letterCombinations(digits string) []string {
	if digits == "" {
		return []string{}
	}
	return helper3("", digits)
}

func helper3(accum string, remaining string) []string {
	if remaining == "" {
		return []string{accum}
	}

	first := int(remaining[0])
	var one []string
	var two []string
	var three []string
	var four []string

	if first == '2' {
		one = helper3(accum+"a", remaining[1:])
		two = helper3(accum+"b", remaining[1:])
		three = helper3(accum+"c", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '3' {
		one = helper3(accum+"d", remaining[1:])
		two = helper3(accum+"e", remaining[1:])
		three = helper3(accum+"f", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '4' {
		one = helper3(accum+"g", remaining[1:])
		two = helper3(accum+"h", remaining[1:])
		three = helper3(accum+"i", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '5' {
		one = helper3(accum+"j", remaining[1:])
		two = helper3(accum+"k", remaining[1:])
		three = helper3(accum+"l", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '6' {
		one = helper3(accum+"m", remaining[1:])
		two = helper3(accum+"n", remaining[1:])
		three = helper3(accum+"o", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '7' {
		one = helper3(accum+"p", remaining[1:])
		two = helper3(accum+"q", remaining[1:])
		three = helper3(accum+"r", remaining[1:])
		four = helper3(accum+"s", remaining[1:])
		return append(one, append(two, append(three, four...)...)...)
	}

	if first == '8' {
		one = helper3(accum+"t", remaining[1:])
		two = helper3(accum+"u", remaining[1:])
		three = helper3(accum+"v", remaining[1:])
		return append(one, append(two, three...)...)
	}

	if first == '9' {
		one = helper3(accum+"w", remaining[1:])
		two = helper3(accum+"x", remaining[1:])
		three = helper3(accum+"y", remaining[1:])
		four = helper3(accum+"z", remaining[1:])
		return append(one, append(two, append(three, four...)...)...)
	}

	return []string{}
}
