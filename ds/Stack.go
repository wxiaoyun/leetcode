package ds

type Stack[T any] []T

func (s *Stack[T]) Push(n T) {
	*s = append(*s, n)
}

func (s *Stack[T]) Pop() T {
	n := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return n
}
