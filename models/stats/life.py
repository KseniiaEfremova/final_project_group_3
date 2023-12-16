from abc import ABC
import pygame
from models.stats.abstract_stats import Stats
from models.player import Player
from board import Board
from utils import assets_library


class Life(Stats, ABC):

    """
    Class representing the player's remaining lives in Code Quest.

    Attributes:
        player_instance (Player): An instance of the player associated with the lives.
        board_instance (Board): An instance of the game board.
        sprites (list): A list of life sprites.
        lives (int): The current number of lives of the player.
        current_sprite (int): The index of the current sprite to be displayed.
        x_positions (list): A list of x-coordinates for displaying life sprites.
        images (list): A list of scaled life images.
        width (int): The width of the life sprites.
        height (int): The height of the life sprites.
        y (int): The y-coordinate of the life sprites on the game board.
        rect (pygame.Rect): The rectangular area of the life sprites.
    """
    
    def __init__(self, player_instance: Player, board_instance: Board):

        """
        Initialise a Life object.

        Parameters:
            player_instance (Player): An instance of the player associated with the lives.
            board_instance (Board): An instance of the game board.
        """

        super().__init__(player_instance, board_instance)
        self.sprites = []
        self.lives = self.player_instance.life
        self.sprites.append(pygame.image.load(assets_library['sprites']['heart']['heart1']))
        self.sprites.append(pygame.image.load(assets_library['sprites']['heart']['heart2']))
        self.sprites.append(pygame.image.load(assets_library['sprites']['heart']['heart3']))
        self.sprites.append(pygame.image.load(assets_library['sprites']['heart']['heart4']))
        self.sprites.append(pygame.image.load(assets_library['sprites']['heart']['heart5']))
        self.sprites.append(pygame.image.load(assets_library['sprites']['heart']['heart6']))
        self.current_sprite = 0
        self.x_positions = [775, 705, 635]
        self.images = []
        self.width = 60
        self.height = 60
        self.y = 75
        self.rect = pygame.Rect(0, 0, self.width, self.height)
    
    def pick_image_index(self, remainder):

        """
        Determine the index of the life sprite based on the remainder of lives.

        Parameters:
            remainder (int): The remainder of lives.

        Returns:
            int: The index of the life sprite.
        """

        if 30 >= remainder > 25:
            self.current_sprite = 1
        elif 25 >= remainder > 17:
            self.current_sprite = 2
        elif 17 >= remainder > 10:
            self.current_sprite = 3
        elif 10 >= remainder > 5:
            self.current_sprite = 4
        elif 5 >= remainder > 0:
            self.current_sprite = 5
        elif remainder == 0:
            self.current_sprite = 0
        return self.current_sprite
    
    def update(self):

        """
        Update the list of scaled life images based on the current number of lives.

        Returns:
            list: A list of scaled life images.
        """

        self.images = []
        self.lives = self.player_instance.get_lives()
        damage_remainder = self.lives % 30 if self.lives > 0 else 1
        if self.lives >= 60:
            first_sprite = 0
            second_sprite = 0
            third_sprite = self.pick_image_index(damage_remainder)
        elif 30 < self.lives < 60:
            first_sprite = 0
            second_sprite = self.pick_image_index(damage_remainder)
            third_sprite = 5
        elif 0 <= self.lives <= 30:
            first_sprite = self.pick_image_index(damage_remainder)
            second_sprite = 5
            third_sprite = 5
        else:
            first_sprite = 5
            second_sprite = 5
            third_sprite = 5
        
        first_image = pygame.transform.scale(self.sprites[first_sprite],
										   (self.width, self.height))
        second_image = pygame.transform.scale(self.sprites[second_sprite],
									   (self.width, self.height))
        third_image = pygame.transform.scale(self.sprites[third_sprite],
									   (self.width, self.height))
        self.images.append(first_image)
        self.images.append(second_image)
        self.images.append(third_image)
        return self.images
    
    def draw(self, board_instance, **kwargs):

        """
        Draw the scaled life images on the game board.

        Parameters:
            board_instance (Board): An instance of the game board.
            **kwargs: Additional keyword arguments.
        """

        self.update()
        for index, image in enumerate(self.images):
            x = self.x_positions[index]
            board_instance.board.blit(
				image, (x - self.height, self.y - self.height))

