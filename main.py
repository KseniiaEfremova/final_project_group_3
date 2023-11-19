from board import Board


def run():
	game_board = Board('arcade catcher', (800, 600), 60)
	game_board.display_board()
	error_item = ErrorItem(game_board.res[0])
	
	while True:
		



if __name__ == '__main__':
	run()
