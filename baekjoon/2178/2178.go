package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// 전역 변수
var (
	graph [][]string
	count [][]int
	dx    = []int{0, 0, -1, 1}
	dy    = []int{-1, 1, 0, 0}
	n, m  int
)

func bfs(x, y int) int {
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &n, &m)

	count = make([][]int, n)
	for i := 0; i < n; i++ {
		count[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		input, _ := reader.ReadString('\n') // 공백 포함하여 입력 받기 위해 ReadString() 사용
		inputs := strings.Split(strings.ReplaceAll(input, "\n", ""), "")
		graph = append(graph, inputs)
	}

	fmt.Println(bfs(0, 0))

}
