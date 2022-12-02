#include <stdio.h>

int main(void) {
	
	FILE *inputFile;

	char games[3000][2];

	char line[5];

	inputFile = fopen("input.txt", "r");

	int gameIndex = 0;

	while(fgets(line, sizeof(line), inputFile) != NULL) {
		games[gameIndex][0] = line[0];
		games[gameIndex][1] = line[2];
		gameIndex++;
	}


	int total = 0;

	// A = 0
	// B = 0
	// C = 0
	// X = 0
	// Y = 0
	// Z = 0

	int scores[3][3];

	scores[0][0] = 4;
	scores[0][1] = 8;
	scores[0][2] = 3;
	scores[1][0] = 1;
	scores[1][1] = 5;
	scores[1][2] = 9;
	scores[2][0] = 7;
	scores[2][1] = 2;
	scores[2][2] = 6;

	int firstIndex, secondIndex;

	for(int i = 0; i < gameIndex; i++) {
		if(games[i][0] == 'A') {
			firstIndex = 0;
		} else if(games[i][0] == 'B') {
			firstIndex = 1;
		} else if(games[i][0] == 'C') {
			firstIndex = 2;
		}

		if(games[i][1] == 'X') {
			secondIndex = 0;
		} else if(games[i][1] == 'Y') {
			secondIndex = 1;
		} else if(games[i][1] == 'Z') {
			secondIndex = 2;
		}

		total += scores[firstIndex][secondIndex];
	}

	printf("%d\n", total);

	return 0;
}
