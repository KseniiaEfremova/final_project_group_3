from board import Board
#import pygame

def run():
	#pygame.init()

	game_board = Board('arcade catcher', (800, 600), 60)
	game_board.display_board()
	error_item = ErrorItem(game_board.res[0])
	
	#falling_items = [error_item]

	#While True: 
	# for item in falling_items:
	#     item.fall()
	#     item.draw(game_board)
	#     if item.disappear():
	#        item.spawn()


if __name__ == '__main__':
	run()
