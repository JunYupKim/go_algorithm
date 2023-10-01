package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	for i := 0; i < N; i++ {
		var n int
		var answer int
		answer = 1
		fmt.Scan(&n)
		m := make(map[string]int)
		for j := 0; j < n; j++ {
			var wear, input string
			fmt.Scan(&wear, &input)
			m[input] += 1
		}

		for _, element := range m {
			answer *= element + 1
		}
		fmt.Println(answer - 1)

	}
}
