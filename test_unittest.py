from random import randint
import refactoring_exercise as Game
import unittest

class Test_Questions_Class(unittest.TestCase):
    def test_question_categories_added_question_bank(self):
        game = Game.StartGame()
        message = 'At least one of the question categories does not match the categories that should have been added.'
        
        game.add_question_categories('sports')
        game.add_question_categories('rock')
        game.add_question_categories('oceans')
        game.add_question_categories('countries')
        
        categories_list = ['Sports', 'Rock', 'Oceans', 'Countries']
        expected_keys = list(game.question_bank.keys())
  
        self.assertCountEqual(categories_list, expected_keys, message)

class Test_Players_Class(unittest.TestCase):  
    
    def test_add_player(self):
        game = Game.StartGame()
        message = 'Player was not added to the players list'
        player_container = game.players

        game.add_players('Michael')
        
        self.assertIn('Michael', player_container, message)    

    def test_how_many_players_exist(self):
        game = Game.StartGame()
        message = 'There is less or more than one person in player_container'

        game.add_players('Jacob')
        game.add_players('Jessica')
        number_players =  game.how_many_players

        self.assertEqual(number_players, 2, message)

    def test_one_player_does_not_start_game(self):
        game = Game.StartGame()
        message = 'The game should not be playable - check that only one player has been added.'

        game.add_players('Nicholas')
        expect_false = game.is_playable() 

        self.assertEqual(False, expect_false, message)   

    def test_two_players_allows_start_game(self):
        game = Game.StartGame()
        message = 'There are less than two or more than three players added to the players list'

        game.add_players('Priscilla')
        game.add_players('Bailey')
        expect_true = game.is_playable()

        self.assertEqual(True, expect_true, message)

    def test_more_than_three_players_does_not_start_game(self):
        game = Game.StartGame()
        message = 'The game should not be playable - check that more than three players were added.'
  
        for i in range(5):
          game.add_players('Michael %s' % i)
        expect_false = game.is_playable()

        self.assertEqual(False, expect_false, message) 

class Test_Check_Answers(unittest.TestCase):

      def test_purse_increase_by_one(self):
          game = Game.StartGame()
          message = 'The purse amount should have gone from zero to one'

          game.add_question_categories('parks')
          game.add_question_categories('holidays')
          game.add_question_categories('books')
          game.add_question_categories('politics')

          game.add_players('Nicole')
          game.roll(3)
          game.actions_taken_for_correct_answer()
          expect_one = game.purses[0]

          self.assertEqual(1, expect_one, message)

      def test_go_to_next_player_turn(self):
          game = Game.StartGame()
          message = 'current_player was not increased by one'

          game.add_question_categories('computers')
          game.add_question_categories('fitness')
          game.add_question_categories('fishing')
          game.add_question_categories('hunting')
          
          game.add_players('Stephanie')
          game.add_players('Jaime')
          game.roll(6)
          
          game.increment_current_player_position()
          expect_kira = game.players[game.current_player]

          self.assertEqual('Jaime', expect_kira, message)

      def test_roll_order_restarts_after_all_players_roll(self):
          game = Game.StartGame()
          message = 'current_player was not set to 0'

          game.add_question_categories('celebrity')
          game.add_question_categories('news')
          game.add_question_categories('slogans')
          game.add_question_categories('business')
          
          game.add_players('Bill')
          game.add_players('Jill')
          game.roll(6)
          game.increment_current_player_position()
          game.roll(2)
          game.increment_current_player_position()

          expect_bill = game.players[game.current_player]

          self.assertEqual('Bill', expect_bill, message)

      def test_winner_returns_bool(self):
          game = Game.StartGame()
          message = 'The return value should be True or False'

          game.add_question_categories('geography')
          game.add_question_categories('science')
          game.add_question_categories('history')
          game.add_question_categories('literature')

          game.add_players('Chris')
          game.add_players('Samantha')
          game.roll(3)

          expect_bool = game.actions_taken_for_correct_answer()

          self.assertIsInstance(expect_bool, bool, message)

      def test_player_won_when_purse_contains_six_gold_coins(self):
          game = Game.StartGame()
          message = 'expect_false should be False'

          game.current_player = 0
          game.purses[0] = 6

          expect_false = game._did_player_win()

          self.assertEqual(False, expect_false, message)

class Test_Roll(unittest.TestCase):

      def test_selected_category_pop(self):
          game = Game.StartGame()
          message = 'places[current_player] should equal one of 0, 4, or 8'

          game.add_question_categories('pop')
          game.add_question_categories('rock')
          game.add_question_categories('metal')
          game.add_question_categories('rap')

          game.add_players('Jerry')
          game.roll(0)
          self.assertEqual('Pop', game._current_category, message)

          game.roll(4)
          self.assertEqual('Pop', game._current_category, message)

          game.roll(4)
          self.assertEqual('Pop', game._current_category, message)

      def test_selected_category_monitors(self):
          game = Game.StartGame()
          message = 'places[current_player] should equal one of 1, 5, or 9'

          game.add_question_categories('keyboards')
          game.add_question_categories('monitors')
          game.add_question_categories('motherboards')
          game.add_question_categories('fans')

          game.add_players('Jenny')
          game.roll(1)
          self.assertEqual('Monitors', game._current_category, message)

          game.roll(4)
          self.assertEqual('Monitors', game._current_category, message)

          game.roll(4)
          self.assertEqual('Monitors', game._current_category, message)

      def test_selected_category_orange(self):
          game = Game.StartGame()
          message = 'places[current_player] should equal one of 2, 6, or 10'

          game.add_question_categories('grape')
          game.add_question_categories('banana')
          game.add_question_categories('orange')
          game.add_question_categories('pineapple')

          game.add_players('Ava')
          game.roll(2)
          self.assertEqual('Orange', game._current_category, message)

          game.roll(4)
          self.assertEqual('Orange', game._current_category, message)

          game.roll(4)
          self.assertEqual('Orange', game._current_category, message)

      def test_selected_category_rock(self):
          game = Game.StartGame()
          message = 'places[current_player] should equal one of 3, 7, or 11'

          game.add_question_categories('suburban')
          game.add_question_categories('tahoe')
          game.add_question_categories('camaro')
          game.add_question_categories('corvette')

          game.add_players('Ana')
          game.roll(3)
          self.assertEqual('Corvette', game._current_category, message)

          game.roll(4)
          self.assertEqual('Corvette', game._current_category, message)

          game.roll(4)
          self.assertEqual('Corvette', game._current_category, message)

      def test_new_player_place_less_than_eleven(self):
          game = Game.StartGame()
          message = 'The rolled number is greater than 11.'

          game.add_players('Abigail')
          game.determine_new_current_player_place(6)
          expect_six = game.places[game.current_player]
          self.assertEqual(6, expect_six, message)

      def test_new_player_greater_than_eleven(self):
          game = Game.StartGame()
          message = 'The rolled number is greater than 12.'

          game.add_players('Abigail')
          number_from_twelve_to_seventeen = randint(12, 17)
          game.determine_new_current_player_place(number_from_twelve_to_seventeen)
          expect_less_than_twelve = game.places[game.current_player]
          self.assertLess(expect_less_than_twelve, 12, message)

        
if __name__ == '__main__':
    unittest.main()