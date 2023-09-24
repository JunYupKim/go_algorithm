package main

import (
	"fmt"
)

// select five players who share the same first letter
// if not print
func main() {
	var n int
	fmt.Scan(&n)
	var list = [27]int{0}

	for i := 0; i < n; i++ {
		var name string
		fmt.Scan(&name)
		list[int(name[0])-int('a')] += 1
	}
	var check bool
	check = false

	for idx, v := range list {
		if v >= 5 {
			charVar := string(idx + int('a'))
			fmt.Print(charVar)
			check = true
		}
	}
	if check == false {
		fmt.Print("PREDAJA")
	}
	fmt.Println()
}
