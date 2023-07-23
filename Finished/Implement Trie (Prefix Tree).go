package leetcode

// https://leetcode.com/problems/implement-trie-prefix-tree/

type Trie struct {
	Children map[byte]*Trie
	IsEnd    bool
}

func TrieConstructor() Trie {
	return Trie{
		Children: make(map[byte]*Trie),
		IsEnd:    false,
	}
}

func (this *Trie) Insert(word string) {
	if word == "" {
		this.IsEnd = true
		return
	}

	if _, ok := this.Children[word[0]]; !ok {
		newTrie := TrieConstructor()
		this.Children[word[0]] = &newTrie
	}

	this.Children[word[0]].Insert(word[1:])
}

func (this *Trie) Search(word string) bool {
	if len(word) == 0 {
		if this.IsEnd {
			return true
		} else {
			return false
		}
	}

	child, ok := this.Children[word[0]]
	if !ok {
		return false
	}
	return child.Search(word[1:])
}

func (this *Trie) StartsWith(prefix string) bool {
	if len(prefix) == 0 {
		return true
	}

	child, ok := this.Children[prefix[0]]
	if !ok {
		return false
	}
	return child.StartsWith(prefix[1:])
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
