package leetcode

// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

type dlll struct {
	c     rune
	left  *dlll
	right *dlll
}

func (l *dlll) Len() int {
	ln := 0

	for l != nil {
		ln++
		l = l.right
	}

	return ln
}

func minLength(s string) int {
	if len(s) < 2 {
		return len(s)
	}

	dummyHead := &dlll{c: '0'}
	current := dummyHead
	for _, c := range s {
		node := &dlll{
			c:    c,
			left: current,
		}
		current.right = node
		current = node
	}
	end := &dlll{
		c:    '0',
		left: current,
	}
	current.right = end

	l, r := dummyHead.right, dummyHead.right.right
	for r != nil {
		if (l.c == 'A' && r.c == 'B') || (l.c == 'C' && r.c == 'D') {
			left := l.left
			right := r.right

			left.right = right
			right.left = left

			l.left = nil
			r.right = nil

			l = left
			r = right
			continue
		}

		l = l.right
		r = r.right
	}

	return dummyHead.Len() - 2
}
