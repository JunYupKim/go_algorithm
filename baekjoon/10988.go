package main

import "fmt"

func main() {
	var S string

	fmt.Scan(&S)

	answer := 1
	// check from left to middle
	for i := 0; i < len(S)/2; i++ {
		if S[i] == S[len(S)-i-1] {
			continue
		} else {
			answer = 0
		}
	}
	fmt.Println(answer)
}
