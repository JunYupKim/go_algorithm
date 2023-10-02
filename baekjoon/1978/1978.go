package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(number int) bool {
	if number > 1 {
		for i := 2; i < int(number/2)+1; i++ {
			if (number % i) == 0 {
				return false
			}
		}
		return true
	}
	return false
}

func checkPrime(list *string) int {
	cnt := 0
	for _, v := range *list {
		if string(v) != " " && v != 10 {
			number, err := strconv.Atoi(string(v))
			if err != nil {
				fmt.Println("There was an error!")
				return 0
			}
			if check(number) {
				cnt += 1
			}
		}
	}
	return cnt
}

func main() {
	var N int
	fmt.Scan(&N)
	reader := bufio.NewReader(os.Stdin)

	input, err := reader.ReadString('\n')

	if err != nil {
		fmt.Println("an error")
		return
		
	fmt.Println(checkPrime(&input))

}
