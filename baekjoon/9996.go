package main

import (
	"fmt"
	"strings"
)

func check(input string, input_string string) bool {
	res := strings.Split(input, "*")
	if len(res[0])+len(res[1]) > len(input_string) {
		return false
	}
	if (res[0] == input_string[:len(res[0])]) && (res[1] == input_string[len(input_string)-len(res[1]):len(input_string)]) {
		return true
	} else {
		return false
	}

}

func main() {

	var N int
	var input string
	var input_string string

	fmt.Scan(&N)
	fmt.Scan(&input)

	for i := 0; i < N; i++ {
		fmt.Scan(&input_string)
		if check(input, input_string) == true {
			fmt.Println("DA")
		} else {
			fmt.Println("NE")
		}
	}

}
