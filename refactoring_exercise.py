#!/usr/bin/env python3
from random import randrange

class Questions:
    def __init__(self):
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        for i in range(50):
              self.pop_questions.append(self.create_question(i, "Pop Question"))
              self.science_questions.append(self.create_question(i, "Science Question"))
              self.sports_questions.append(self.create_question(i, "Sports Question"))
              self.rock_questions.append(self.create_question(i, "Rock Question"))

    def create_question(self, index, question_category):
          return f'{question_category} {index}'

class Players(Questions):
    def __init__(self):
        super().__init__()
        self.players = []
        self.current_player = 0
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.is_getting_out_of_penalty_box = False

    def is_playable(self):
        """Determines if there are at least two players in the game
        
            Return: A boolean value - true if players in the game is equal or greater than two or false otherwise.
        """
        return self.how_many_players >= 2

    def add_players(self, player_name):
        """Adds a player name to the players[] and states the name of the player that was added to the game. 
          Passes the player_name into a method that adds a variety of attributes for that particular player.

            Return: None    
        """
        self.players.append(player_name)
        print(player_name + " was added")
        self.add_player_attributes()

    def add_player_attributes(self):
        """Upon a player being added to the game, sets initial values for their place, purse amount, and penalty box status.

            Return: True
        """
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        print("They are player number %s" % len(self.players))
        
        return True

    @property
    def how_many_players(self):
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

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break