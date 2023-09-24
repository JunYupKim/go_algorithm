package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, err := reader.ReadString('\n')

	if err != nil {
		fmt.Println("an error")
		return
	}

	for _, v := range input {
		if int('a') <= int(v) && int(v) <= int('z') {
			if int('z')-13 < int(v) {
				fmt.Print(string(int('a') + (12 - (int('z') - int(v)))))
			} else {
				fmt.Print(string(int(v) + 13))
			}

		} else if int('A') <= int(v) && int(v) <= int('Z') {
			if int('M') < int(v) {
				fmt.Print(string(int('A') + 12 - (int('Z') - int(v))))
			} else {
				fmt.Print(string(int(v) + 13))
			}
		} else {
			fmt.Print(string(v))
		}
	}

}
