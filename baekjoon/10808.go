package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)

	var list = [26]int{0}

	for _, v := range S {
		list[int(v)-int('a')] += 1
	}
	for _, v := range list {
		fmt.Print(v, " ")
	}
	fmt.Println()

}
