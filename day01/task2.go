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
	maxCaloriesIndex := 0
	total := 0

	for i := 0; i < 3; i++ {

		for elfIndex, calories := range caloriesByElf {
			if calories > maxCalories {
				maxCalories = calories
				maxCaloriesIndex = elfIndex
			}
		}

		total += maxCalories

		caloriesByElf = append(caloriesByElf[:maxCaloriesIndex], caloriesByElf[maxCaloriesIndex+1:]...)
	}

	fmt.Println(total)
}
