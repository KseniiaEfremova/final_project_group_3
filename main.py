from board import Board


def run():
	

	game_board = Board('arcade catcher', (800, 600), 60)
	game_board.display_board()
	error_item = ErrorItem(game_board.res[0])
	warning_item = WarningItem(game_board.res[0])
	bug_item = BugItem(game_board.res[0])
	
	




if __name__ == '__main__':
	run()
