package main

import "fmt"

func main() {
	var A, B int
	fmt.Scan(&A, &B)
	if A > B {
		fmt.Println(">")
	} else if A < B {
		fmt.Println("<")
	} else {
		fmt.Println("==")
	}

}
