#!/usr/bin/env python3

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

class Players:
  def __init__(self):
      self.players = []
      self.current_player = 0
      self.places = [0] * 6
      self.purses = [0] * 6
      self.in_penalty_box = [0] * 6

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

class Roll():
  def __init__(self, players: Players, questions: Questions):
    self.player_information = players
    self.questions: questions

  @property
  def _current_category(self):
      if self.player_information.places[self.player_information.current_player] in [0, 4, 8]:
        return 'Pop'
      elif self.player_information.places[self.player_information.current_player] in [1, 5, 9]:
        return 'Science'
      elif self.player_information.places[self.player_information.current_player] in [2, 6, 10]:
        return 'Sports'
      else:
        return 'Rock'

  def start_roll(self, roll):
    print("%s is the current player" % self.player_information.players[self.player_information.current_player])
    print("They have rolled a %s" % roll)

    if self.player_information.in_penalty_box[self.player_information.current_player]:
      if roll % 2 != 0:
        self.leaving_penalty_box
      else: 
        print("%s is not getting out of the penalty box" % self.player_information.players[self.player_information.current_player])
        self.is_getting_out_of_penalty_box = False
    else:
      self.determine_new_current_player_place
      self._ask_question

  def leaving_penalty_box(self):
    self.is_getting_out_of_penalty_box = True
    print("%s is getting out of the penalty box" % self.player_information.players[self.player_information.current_player])

    self.determine_new_current_player_place
    
  def determine_new_current_player_place(self, roll):
    self.player_information.places[self.player_information.current_player] = self.player_information.places[self.player_information.current_player] + roll

    if self.player_information.places[self.player_information.current_player] > 11:
        self.player_information.places[self.player_information.current_player] = self.player_information.places[self.player_information.current_player] - 12

    print(self.player_information.players[self.player_information.current_player] + \
      '\'s new location is ' + \
      str(self.player_information.places[self.player_information.current_player]))

  def _ask_question(self):
    print("The category is %s" % self._current_category)
    if self._current_category == 'Pop': print(self.questions.pop_questions.pop(0))
    if self._current_category == 'Science': print(self.questions.science_questions.pop(0))
    if self._current_category == 'Sports': print(self.questions.sports_questions.pop(0))
    if self._current_category == 'Rock': print(self.questions.rock_questions.pop(0))


class Game:
    def __init__(self, questions: Questions, players: Players):
        self.questions = questions
        self.player_information = players

        self.is_getting_out_of_penalty_box = False 
        

    def was_correctly_answered(self):
        if self.player_information.in_penalty_box[self.player_information.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.player_information.purses[self.player_information.current_player] += 1
                print(self.player_information.players[self.player_information.current_player] + \
                    ' now has ' + \
                    str(self.player_information.purses[self.player_information.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                self.player_information.current_player += 1
                if self.player_information.current_player == len(self.player_information.players): self.player_information.current_player = 0

                return winner
            else:
                self.player_information.current_player += 1
                if self.player_information.current_player == len(self.player_information.players): self.player_information.current_player = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.player_information.purses[self.player_information.current_player] += 1
            print(self.player_information.players[self.player_information.current_player] + \
                ' now has ' + \
                str(self.player_information.purses[self.player_information.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.player_information.current_player += 1
            if self.player_information.current_player == len(self.player_information.players): self.player_information.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.player_information.players[self.player_information.current_player] + " was sent to the penalty box")
        self.player_information.in_penalty_box[self.player_information.current_player] = True

        self.player_information.current_player += 1
        if self.player_information.current_player == len(self.player_information.players): self.player_information.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.player_information.purses[self.player_information.current_player] == 6)


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    questions = Questions()
    players = Players()
    roll_logic = Roll(players, questions)
    game = Game(questions, players)

    players.add_players('Chet')
    players.add_players('Pat')
    players.add_players('Sue')

    while True:
        roll_logic.start_roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break