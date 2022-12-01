package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	readFile, _ := os.Open("input.txt")

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	var caloriesByElf []int

	caloriesByElf = append(caloriesByElf, 0)
	elfIndex := 0

	for _, line := range fileLines {
		number, err := strconv.Atoi(line)
		if err != nil {
			caloriesByElf = append(caloriesByElf, 0)
			elfIndex++
		} else {
			caloriesByElf[elfIndex] += number
		}
	}

	maxCalories := caloriesByElf[0]

	for _, calories := range caloriesByElf {
		if calories > maxCalories {
			maxCalories = calories
		}
	}

	fmt.Println(maxCalories)
}
