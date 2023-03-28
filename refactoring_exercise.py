#!/usr/bin/env python3
from random import randrange

class Questions:
    """
    Creates the categories and questions for the game.

    Instance Attributes
    ----------
    pop_questions (list): A list containing integers 0 - 49.
    science_questions (list): A list containing integers 0 - 49.
    sports_questions (list): A list containing integers 0 - 49.
    rock_questions (list): A list containing integers 0 - 49.
    """
    def __init__(self):
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        for i in range(50):
              self.pop_questions.append(self.create_question("Pop Question", i))
              self.science_questions.append(self.create_question("Science Question", i))
              self.sports_questions.append(self.create_question("Sports Question", i))
              self.rock_questions.append(self.create_question("Rock Question", i))

    def create_question(self, question_category, index):
          """
          Creates a string containing the question category name and the question number. 

          Args:
              question_category (str): Name of a player to be added to the game.
              index (int): A number, starting at 0 and going until 49, meant to represent the question number.
          Returns: 
              str: A string containing the question category name and question number.    
          """
          return f'{question_category} {index}'

class Players(Questions):
    """
    Creates the initial values for information connected to the players and determines if enough players have been added to play the game.

    Instance Attributes
    ----------
    players (list): A list containing the names of each player added to the game.
    current_player (int): An integer used as an index to determine the player currently playing the game.
    places (list): A list containing integers used to determine each players place and which question category will be selected for a respective player's turn.
    purses (list): A list containing the total gold coins for each player.
    in_penalty_box (list): A list containing a True/False value for each player as it relates to their penalty box status.
    is_getting_out_of_penalty_box (bool): A variable used to track whether a player will be removed from the penalty box.
    """
    def __init__(self):
        super().__init__()
        self.players = []
        self.current_player = 0
        self.places = [0] * 3
        self.purses = [0] * 3
        self.in_penalty_box = [False] * 3
        self.is_getting_out_of_penalty_box = False

    def is_playable(self):
        """
        Determines if there are at least two players in the game.

        Returns: 
            bool: True if players in the game is equal or greater than two, False otherwise.
        """
        return self.how_many_players >= 2

    def add_players(self, player_name):
        """
        Adds a player name to the players[] and states the name and player number of the player that was added to the game. 

        Args:
            player_name (str): Name of a player to be added to the game.

        Returns: 
            None    
        """
        self.players.append(player_name)
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

    @property
    def how_many_players(self):
      """
        Returns:
            int: An integer related to the length of the players list.
      """
      return len(self.players)

class Roll(Players, Questions):
    def __init__(self):
        super().__init__()

    @property
    def _current_category(self):
        if self.places[self.current_player] in [0, 4, 8]:
            return 'Pop'
        elif self.places[self.current_player] in [1, 5, 9]:
            return 'Science'
        elif self.places[self.current_player] in [2, 6, 10]:
            return 'Sports'
        else:
            return 'Rock'

    def start_roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.leaving_penalty_box(roll)
            else: 
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.determine_new_current_player_place(roll)

        self._ask_question()

    def leaving_penalty_box(self, roll):
        self.is_getting_out_of_penalty_box = True
        print("%s is getting out of the penalty box" % self.players[self.current_player])

        self.determine_new_current_player_place(roll)
      
    def determine_new_current_player_place(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll

        if self.places[self.current_player] > 11:
              self.places[self.current_player] = self.places[self.current_player] - 12

        print(self.players[self.current_player] + \
          '\'s new location is ' + \
          str(self.places[self.current_player]))

    def _ask_question(self):
        print("The category is %s" % self._current_category)
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

class CheckAnswer(Players):
  def __init__(self):
      super().__init__()


  def was_correctly_answered(self):
      if self.in_penalty_box[self.current_player]:
          if self.is_getting_out_of_penalty_box:
              return self.actions_taken_for_correct_answer()
          else:
              return self.increment_current_player_position()
      else:
          return self.actions_taken_for_correct_answer()

  def actions_taken_for_correct_answer(self):
      print('Answer was correct!!!!')

      self.purses[self.current_player] += 1

      print(self.players[self.current_player] + \
          ' now has ' + \
          str(self.purses[self.current_player]) + \
          ' Gold Coins.')

      winner = self._did_player_win()
      self.increment_current_player_position()

      return winner

  def increment_current_player_position(self):
      self.current_player += 1
      if self.current_player == len(self.players): self.current_player = 0
      return True
  
  def wrong_answer(self):
      print('Question was incorrectly answered')
      print(self.players[self.current_player] + " was sent to the penalty box")
      self.in_penalty_box[self.current_player] = True

      self.current_player += 1
      if self.current_player == len(self.players): self.current_player = 0
      return True

  def _did_player_win(self):
      return not (self.purses[self.current_player] == 6)

class StartGame(CheckAnswer, Roll, Players):
      def __init__(self):
          super().__init__()

      def add(self, player_name):
          self.add_players(player_name)

      def roll(self, roll_number):
          self.start_roll(roll_number)

if __name__ == '__main__':
    not_a_winner = False

    game = StartGame()
    game.add_players('Chet')
    game.add_players('Pat')
    game.add_players('Sue')

    if game.is_playable():
      while True:
          game.roll(randrange(5) + 1)

          if randrange(9) == 7:
              not_a_winner = game.wrong_answer()
          else:
              not_a_winner = game.was_correctly_answered()

          if not not_a_winner: break
    else:
      print('You\'ve either added too many or not enough players. Please make sure there are at least two, but no more than three players in order to play!')