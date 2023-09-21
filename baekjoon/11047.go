// https://www.acmicpc.net/problem/11047
package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, k int
	fmt.Scanf("%d %d\n", &n, &k)

	// slice
	var number_list = []int{}

	var i int
	for i = 0; i < int(n); i++ {
		var number int
		fmt.Scan(&number)
		number_list = append(number_list, number)
	}

	// reverse sort
	sort.Sort(sort.Reverse(sort.IntSlice(number_list)))

	// number of coins used
	var count int
	for i = 0; i < int(n); i++ {
		for number_list[i] <= k {
			k -= number_list[i]
			count += 1
		}
	}

	fmt.Println(count)

}
