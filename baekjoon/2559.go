package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	temp_list := []int{}

	for i := 0; i < n; i++ {
		var number int
		fmt.Scan(&number)
		temp_list = append(temp_list, number)
	}

	answer_list := []int{}
	for i := 0; i < len(temp_list); i++ {
		answer_list = append(answer_list, 0)
	}

	for i := 0; i < len(temp_list)-k+1; i++ {
		answer_list[i] = temp_list[i]
		for j := i + 1; j < i+k; j++ {
			answer_list[i] += temp_list[j]
		}
	}
	var max int
	max = 0
	for i := 0; i < len(answer_list); i++ {
		if max < answer_list[i] {
			max = answer_list[i]
		}
	}

	fmt.Println(max)

}
