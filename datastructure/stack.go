// stack implementation
// LIFO (Last In First Out)
package main

import "fmt"

type Stack []interface{}

func (dataList *Stack) push(number int) {
	*dataList = append(*dataList, number)
}

func (dataList *Stack) pop() {

	if len(*dataList) == 0 {
		fmt.Println("There is NO element in the stack")
		return
	}
	// pop the last element in the list
	*dataList = (*dataList)[:len(*dataList)-1]

}

func main() {
	var dataList Stack
	var input int
	for {
		fmt.Scan(&input)
		if input != 0 {
			dataList.push(input)
		} else {
			break
		}
	}
	fmt.Println(dataList)
	dataList.pop()
	dataList.pop()
	fmt.Println(dataList)
}
