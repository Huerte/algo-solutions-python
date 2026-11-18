// Problem: N-Queens II
// Source: https://leetcode.com/problems/n-queens-ii/
// Note: A simple colution in C. There is probably room to optimize though.

int valid_placement(char board[9][9], int row, int col, int n) {
	// column check
	for(int i = 0; i < n; i++) {
		if(board[i][col] != 0)
			return 0;
	}

	// diagonal check
	// Upper-left diagonal check
    for (int i = 1; row - i >= 0 && col - i >= 0; i++) {
        if (board[row - i][col - i] != 0)
            return 0;
    }

    // Upper-right anti-diagonal check
    for (int i = 1; row - i >= 0 && col + i < n; i++) {
        if (board[row - i][col + i] != 0)
            return 0;
    }

	return 1;
}

void calc_placements(char board[9][9], int row, int n, int *count) {
	// base case
	if(row == n) {
		(*count)++;
		return;
	}

	for(int col = 0; col < n; col++) {
		if(valid_placement(board, row, col, n)) {
			board[row][col] = 1;
			calc_placements(board, row + 1, n, count);
			board[row][col] = 0;
		}
	}
}

int totalNQueens(int n) {
	char board[9][9]; // n is at most 9 by the problem description
	int count = 0;
	calc_placements(board, 0, n, &count);
	return count;
}
