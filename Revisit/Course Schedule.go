package leetcode

// https://leetcode.com/problems/course-schedule/

func canFinish(numCourses int, prerequisites [][]int) bool {
	// We can construct a graph from the prerequisites
	// and then check if there is a cycle in the graph
	// if there is a cycle, then we can't finish the courses, vice versa

	// construct the graph
	graph := make([][]int, numCourses)
	for _, p := range prerequisites {
		graph[p[0]] = append(graph[p[0]], p[1])
	}

	// we need to keep track of the visited nodes
	// if we visit a node that is already visited, then there is a cycle
	visited := make([]bool, numCourses)
	// we also need to keep track of the nodes that are currently being visited
	// if we visit a node that is currently being visited, then there is a cycle
	visiting := make([]bool, numCourses)

	// for each node, we check if there is a cycle
	for i := range graph {
		if hasCycle(graph, visited, visiting, i) {
			return false
		}
	}

	return true
}

func hasCycle(graph [][]int, visited, visiting []bool, node int) bool {
	// if the node is currently being visited, then there is a cycle
	if visiting[node] {
		return true
	}
	// if the node is already visited, then there is no cycle
	if visited[node] {
		return false
	}

	// mark the node as currently being visited
	visiting[node] = true
	// for each neighbor of the node
	for _, n := range graph[node] {
		// if there is a cycle, then return true
		if hasCycle(graph, visited, visiting, n) {
			return true
		}
	}
	// mark the node as visited
	visited[node] = true
	// mark the node as not currently being visited
	visiting[node] = false
	return false
}
