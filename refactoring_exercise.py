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
        self.question_bank = {}

        for i in range(50):
              self.pop_questions.append(self.create_question("Pop Question", i))
              self.science_questions.append(self.create_question("Science Question", i))
              self.sports_questions.append(self.create_question("Sports Question", i))
              self.rock_questions.append(self.create_question("Rock Question", i))

    def add_question_categories(self, question_category):
        if question_category in self.question_bank:
            print('This question category already exists, please add a different question category.')
        else:
            self.question_bank[question_category] = []
            self.create_question_test(question_category)

    def create_question_test(self, question_category):  
        for i in range(50):
              self.question_bank[question_category].append(f'{question_category} Question {i}')

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
            bool: True if players in the game is greater than one and less than four, False otherwise.
        """
        return self.how_many_players > 1 and self.how_many_players < 4

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

class Roll(Players):
    """
    Rolls the game piece for each player, determines if a player leaves the penalty box and their new place, as well as the question to be asked.
    """
    def __init__(self):
        super().__init__()

    @property
    def _current_category(self):
        """
        Determines the question category for the player based on the value in places[current_player].

        Returns: 
            str: A one word string that contains the name of a question category.
        """
        categories = list(self.question_bank.keys())
        first_category = categories[0]
        second_category = categories[1]
        third_category = categories[2]
        fourth_category = categories[3]

        if self.places[self.current_player] in [0, 4, 8]:
            return first_category
        elif self.places[self.current_player] in [1, 5, 9]:
            return second_category
        elif self.places[self.current_player] in [2, 6, 10]:
            return third_category
        else:
            return fourth_category

    def start_roll(self, roll):
        """
        Prints statements related to the who the current player is and their roll.

        If the current_player is in the penalty box and their roll % 2 has a remainder of 1, then they will leave the penalty box.
        Otherwise, the current_player remains in the penalty box.

        If the current_player is not in the penalty box, then only their new place is determined.

        After the conditionals run, _ask_question() is called to "pull" a question from the applicable category.
        """
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
        """
        The current_player leaves the penalty box by setting is_getting_out_of_penalty_box to True.

        Prints a statement regarding the current_player leaving the penalty box.

        Generate a new place for the current_player via determine_new_current_player_place.
        """
        self.is_getting_out_of_penalty_box = True
        print("%s is getting out of the penalty box" % self.players[self.current_player])

        self.determine_new_current_player_place(roll)
      
    def determine_new_current_player_place(self, roll):
        """
        Generates a new place for the current_player by taking places[current_player] and adding roll.

        If the aforementioned value is greater than 11, then subtract that value by 12.

        Print the current player's new location.
        """
        self.places[self.current_player] = self.places[self.current_player] + roll

        if self.places[self.current_player] > 11:
              self.places[self.current_player] = self.places[self.current_player] - 12

        print(self.players[self.current_player] + \
          '\'s new location is ' + \
          str(self.places[self.current_player]))

    def _ask_question(self):
        """
        Prints a statement regarding the current_category.

        Prints the question from one of the four categories based on the value of _current_category.
        """
        print("The category is %s" % self._current_category)
        
        categories = list(self.question_bank.keys())
        first_category = categories[0]
        second_category = categories[1]
        third_category = categories[2]
        fourth_category = categories[3]

        if self._current_category == first_category: print(self.question_bank[first_category].pop(0))
        if self._current_category == second_category: print(self.question_bank[second_category].pop(0))
        if self._current_category == third_category: print(self.question_bank[third_category].pop(0))
        if self._current_category == fourth_category: print(self.question_bank[fourth_category].pop(0))

class Check_Answer(Roll):
    """
    Checks to determine if an answer is correct or wrong and the actions to take based on said check.
    """
    def __init__(self):
        super().__init__()


    def was_correctly_answered(self):
        """
        First if statement:
            Check to see if the in_penalty_box[current_player] value is truthy (aka inside the penalty box).
            Nested if statement: 
                If truthy then check to see the is_getting_out_of_penalty_box is also truthy. 
                If that value is also truthy, then the actions_taken_for_correct_answer() method runs and returns a truthy/falsy value. 
            Nested else statement:
                If falsy, then the answer was not correct and increment_current_player_position() runs and returns True.
        Second else statement:
            If the current_player is not in the penalty box, then run actions_taken_for_correct_answer(). 

        Returns:
            bool: Truthy/falsy value depending on the results of the method calls in the conditionals.  
        """
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                return self.actions_taken_for_correct_answer()
            else:
                return self.increment_current_player_position()
        else:
            return self.actions_taken_for_correct_answer()

    def actions_taken_for_correct_answer(self):
        """
        Print statements that state the player got the answer correct and the number of coins said player now has.

        Increases the number of coins in the applicable player's purse by 1.

        Updates the current_players position only if the current_player does not have 6 coins.

        Returns:
            bool: True if the number of coins for the current_player in the purse is not 6, False otherwise.  
        """
        print('Answer was correct!!!!')

        self.purses[self.current_player] += 1

        print(self.players[self.current_player] + \
            ' now has ' + \
            str(self.purses[self.current_player]) + \
            ' Gold Coins.')

        winner = self._did_player_win()

        if winner:
            self.increment_current_player_position()        

        return winner

    def increment_current_player_position(self):
        """
        Increase current_player by 1. If the increase is equal to the length of the players list then set current_player to 0 (aka going back to the first player and continuing the game)

        Returns:
          bool: True
        """
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True
    
    def wrong_answer(self):
        """
        Print statements regarding incorrect answer and moving to the penalty box.

        Places the current_player in the penalty box.

        Runs increment_current_player_position to increase current_player by 1.

        Returns:
          bool: True
        """
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        return self.increment_current_player_position()

    def _did_player_win(self):
        """
        Returns:
          bool: If a player's purse does not equal 6 then return True, otherwise False.
        """
        return (self.purses[self.current_player] != 6)

class StartGame(Check_Answer, Roll):
    """
    Starts the game by calling on two methods contained in parent classes.
    """
    def __init__(self):
        super().__init__()

    def add(self, player_name):
        """
        Adds the player to the game by calling the add_players() method located in the Players class.

        Returns: 
            None
        """
        self.add_players(player_name)

    def roll(self, roll_number):
        """
        Rolls the game piece to generate an integer by calling the start_roll() method located in the Roll class.

        Returns: 
            None
        """
        self.start_roll(roll_number)

if __name__ == '__main__':
    not_a_winner = False

    game = StartGame()

    game.add_question_categories('Food')
    game.add_question_categories('Music')
    game.add_question_categories('TV')
    game.add_question_categories('Gaming')

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

          if not not_a_winner: 
              print('%s won the game' % game.players[game.current_player])
              break
    else:
      print('You\'ve either added too many or not enough players. Please make sure there are 2-3 players in order to play!')