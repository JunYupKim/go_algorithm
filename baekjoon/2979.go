package main

import "fmt"

func main() {
	var A, B, C int
	fmt.Scan(&A, &B, &C)

	var price_list = [101]int{0}

	var arrival, departure int
	for i := 0; i < 3; i++ {
		fmt.Scan(&arrival, &departure)
		for j := arrival; j < departure; j++ {
			price_list[j] += 1
		}
	}
	price := 0
	for _, v := range price_list {
		if v == 1 {
			price += A
		} else if v == 2 {
			price += (B * 2)
		} else if v == 3 {
			price += (C * 3)
		}
	}
	fmt.Println(price)

}
