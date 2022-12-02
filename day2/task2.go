package main

import (
	"bufio"
	"fmt"
	"os"
)

type Game struct {
	elf, me string
}

func main() {

	readFile, _ := os.Open("input.txt")

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	games := make([]Game, 0)

	var line string

	for fileScanner.Scan() {
		line = fileScanner.Text()
		games = append(games, Game{elf: string(line[0]), me: string(line[2])})
	}

	readFile.Close()

	scores := map[string]map[string]int{
		"A": {"X": 3, "Y": 4, "Z": 8},
		"B": {"X": 1, "Y": 5, "Z": 9},
		"C": {"X": 2, "Y": 6, "Z": 7},
	}

	total := 0

	for _, game := range games {
		total += scores[game.elf][game.me]
	}

	fmt.Println(total)
}
