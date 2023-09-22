// https://www.acmicpc.net/problem/2309
package main

import (
	"fmt"
	"sort"
)

func sum(a, b int, list []int) bool {
	var cnt int
	for i := 0; i < 9; i++ {
		if i != a && i != b {
			cnt += list[i]
		}
	}
	if cnt == 100 {
		return true
	} else {
		return false
	}
}

func main() {
	// input number
	var number int
	// input list
	var list = []int{}

	var i int
	for i = 0; i < 9; i++ {
		fmt.Scan(&number)
		list = append(list, int(number))
	}

	// sort
	sort.Sort(sort.IntSlice(list))

	var a, b int
	for i = 0; i < 9-1; i++ {
		for j := i + 1; j < 9; j++ {
			if sum(i, j, list) == true {
				a = i
				b = j
				break
			}
		}
	}

	for idx, v := range list {
		if idx == a || idx == b {
			continue
		} else {
			fmt.Println(v)
		}
	}

}
