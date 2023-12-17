import pygame
from board import Board
from utils import assets_library
from decorators.sounds import Sounds
from models.falling_items.points_falling_item import PointsFallingItem
from models.falling_items.damage_falling_item import DamageFallingItem
from db.user import *


class Player(pygame.sprite.Sprite):

    """
    Class representing the Player in Code Quest.

    Attributes:
        x (int): The initial x-coordinate of the player on the game board.
        y (int): The initial y-coordinate of the player on the game board.
        board_instance (Board): An instance of the game board.
        falling_group: A group containing falling items.
        name (str): The name of the player.
        sprites_right (list): A list of player sprites when moving right.
        sprites_left (list): A list of player sprites when moving left.
        current_sprite (int): The index of the current player sprite.
        width (int): The width of the player's sprite.
        height (int): The height of the player's sprite.
        rect (pygame.Rect): The rectangle representing the player's position.
        image (pygame.Surface): The surface representing the player's sprite.
        life (int): The player's remaining life points.
        points (int): The player's current points.
        level (int): The player's current level.
        is_winner (bool): A flag indicating if the player is the winner.
        leveled_up (bool): A flag indicating if the player has leveled up.
        is_loser (bool): A flag indicating if the player has lost the game.
    """
    
    def __init__(self, x, y, board_instance: Board, falling_group, name):

        """
        Initialise a Player object.

        Parameters:
            x (int): The initial x-coordinate of the player on the game board.
            y (int): The initial y-coordinate of the player on the game board.
            board_instance (Board): An instance of the game board.
            falling_group: A group containing falling items.
            name (str): The name of the player.
        """

        super().__init__()
        self.sprites_right = []
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right1']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right2']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right3']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right4']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right5']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right6']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right7']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right8']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']
            ['player_right9']))
        self.sprites_left = []
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left1']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left2']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left3']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left4']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left5']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left6']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left7']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left8']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left9']))
        self.current_sprite = 0
        self.width = 100
        self.height = 238
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.image = pygame.transform.scale(
            self.sprites_right[self.current_sprite],
            (self.width, self.height))
        self.board_instance = board_instance
        self.falling_group = falling_group
        self.name = name
        self.life = 90
        self.points = 0
        self.level = 1
        self.is_winner = False
        self.leveled_up = False
        self.is_loser = False

    def draw_player(self):

        """
        Draw the Player on the game board.
        """

        self.board_instance.board.blit(self.image, (self.rect.x,
                                                    self.rect.y - 10))

    def constrain_move_within_board(self, dx, dy):

        """
        Constrain the Player's movement within the boundaries of the game board.

        Parameters:
            dx (int): The change in the x-coordinate.
            dy (int): The change in the y-coordinate.

        Returns:
            Tuple[int, int]: The adjusted changes in x and y coordinates.
        """

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > self.board_instance.res[0]:
            dx = self.board_instance.res[0] - self.rect.right
        return dx, dy

    def animate(self, direction):

        """
        Animate the Player's movement.

        Parameters:
            direction (str): The direction of movement ('right' or 'left').
        """

        self.current_sprite += 1
        if self.current_sprite >= 8:
            self.current_sprite = 0
        if direction == 'right':
            self.image = self.sprites_right[self.current_sprite]
            self.image = pygame.transform.scale(
                self.sprites_right[self.current_sprite],
                (self.width, self.height))
        else:
            self.image = self.sprites_left[self.current_sprite]
            self.image = pygame.transform.scale(
                self.sprites_left[self.current_sprite],
                (self.width, self.height))

    def move(self):

        """
        Move the Player based on keyboard input.
        Constrain the move within the board.
        """

        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -10
            self.animate('left')
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = 10
            self.animate('right')
        dx, dy = self.constrain_move_within_board(dx, dy)    

        self.rect.x += dx
        self.rect.y += dy

    @Sounds(assets_library['sounds']['bonus'], loop=False)
    def points_collision(self, item):

        """
        Handle collision with a points-falling item, updating points and life.

        Parameters:
            item (PointsFallingItem): The points-falling item.
        """

        self.points += item.points
        self.life += item.damage

    @Sounds(assets_library['sounds']['damage'], loop=False)
    def damage_collision(self, item):

        """
        Handle collision with a damage-falling item, updating points and damage.

        Parameters:
            item (DamageFallingItem): The damage-falling item.
        """

        self.points -= item.points
        self.life -= item.damage

    def check_falling_item_collision(self):

        """
        Check for collisions between the Player and falling items.

        If the Player's life is greater than 0, check for collisions with
        falling items (both points and damage items). Handle the collisions
        and update the Player's points and life accordingly. If the Player's
        life becomes zero, set the Player as a loser.

        Returns:
            Tuple[int, bool]: A tuple containing the updated points and a flag
            indicating if the player is a loser.
        """

        if self.life > 0:
            collisions = pygame.sprite.spritecollide(
                self, self.falling_group.falling_items, True)
            for item in collisions:
                item.rect.topleft = (-10, -10)
                item.x = 1000
                item.rect.x = 1000
                self.kill()
                if isinstance(item, PointsFallingItem):
                    self.points_collision(item)
                if isinstance(item, DamageFallingItem):
                    self.damage_collision(item)
        else:
            self.is_loser = True
        return self.points, self.is_loser

    def get_lives(self):

        """
        Get the current number of lives of the Player.

        Returns:
            int: The current number of lives.
        """

        return self.life

    def get_points(self):

        """
        Get the current points of the Player.

        Returns:
            int: The current points.
        """

        return self.points

    def get_level(self):

        """
        Get the current level of the Player.

        Returns:
            int: The current level.
        """

        return self.level

    def get_is_winner(self):

        """
        Check if the Player is the winner.

        Returns:
            bool: True if the Player is the winner, False otherwise.
        """

        return self.is_winner

    def get_is_loser(self):

        """
        Check if the Player is the loser.

        Returns:
            bool: True if the player is the loser, False otherwise.
        """

        return self.is_loser

    def check_is_winner(self):

        """
        Check if the Player is the winner.

        If the Player's life is greater than 0 and the level is 3, toggle the
        winner status.

        Returns:
            None
        """

        if self.life > 0 and self.level == 3:
            self.toggle_is_winner()
        return

    def toggle_is_winner(self):

        """
        Toggle the winner status of the Player.

        Returns:
            bool: The updated winner status.
        """

        self.is_winner = not self.is_winner
        return self.is_winner

    def toggle_is_loser(self):

        """
        Toggle the loser status of the Player.

        Returns:
            bool: The updated loser status.
        """

        self.is_loser = not self.is_loser
        return self.is_loser

    def check_for_level_up(self):

        """
        Check if the Player has leveled up.

        If the Player's life is greater than 0, set the leveled_up flag.

        Returns:
            bool: True if the Player has leveled up, False otherwise.
        """

        if self.life > 0:
            self.leveled_up = True
            return self.leveled_up
        
    def level_up_player(self):

        """
        Level up the Player.

        Increment the Player's level by 1.

        Returns:
            int: The updated level.
        """

        self.level += 1
        return self.level
        
    def reset_player(self):

        """
        Reset the Player's position and the leveled_up flag.

        Returns:
            bool: The updated leveled_up status.
        """

        self.rect.center = (800 - 725, 600 - 200)
        self.leveled_up = False
        return self.leveled_up

    def reset_player_stats(self):

        """
        Reset the Player's level, points, and life.

        Returns:
            Tuple[int, int, int]: The updated level, points, and life.
        """

        self.level = 1
        self.points = 0
        self.life = 90
        return self.level, self.points, self.life

    def update_db(self):

        """
        Update the Player's statistics in the database.

        Fetch the user ID and update the user's statistics in the database.

        Returns:
            None
        """

        user_id = get_user_id(DB_NAME, users_table, self.name)
        update_user_statistics(DB_NAME, statistics_table, self.points,
                               self.life, self.level, user_id)
