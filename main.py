from board import Board


def run():
	#pygame.init()

	game_board = Board('arcade catcher', (800, 600), 60)
	game_board.display_board()
	error_item = ErrorItem(game_board.res[0])
	
	#will add these changes later on
	#while True:
		#error_item.fall()
		#error_item.draw(game_board) 

		#if error_item.disappear():
			#error_item.spawn()


if __name__ == '__main__':
	run()
