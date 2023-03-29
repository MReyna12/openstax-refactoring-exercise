import refactoring_exercise as Game
import unittest


class Test_Players_Class(unittest.TestCase):  
    
    def test_add_a_player(self):
        game = Game.StartGame()
        message = 'Player was not added to the players list'
        player_container = game.players

        game.add_players('Michael')
        game.add_players('Hillery')
        
        self.assertIn('Michael', player_container, message)    

    def test_how_many_players_exist(self):
        game = Game.StartGame()
        message = 'There is less or more than one person in player_container'

        game.add_players('Jacob')
        game.add_players('Jessica')
        number_players =  game.how_many_players

        self.assertEqual(number_players, 2, message)

    def test_one_player(self):
        game = Game.StartGame()
        message = 'The game should not be playable - check that only one player has been added.'

        game.add_players('Nicholas')
        expect_false = game.is_playable() 

        self.assertEqual(False, expect_false, message)   

    def test_correct_number_players(self):
        game = Game.StartGame()
        message = 'There are less than two or more than three players added to the players list'

        game.add_players('Priscilla')
        game.add_players('Bailey')
        expect_true = game.is_playable()

        self.assertEqual(True, expect_true, message)

    def test_more_than_three_players(self):
        game = Game.StartGame()
        message = 'The game should not be playable - check that more than three players were added.'
  
        for i in range(5):
          game.add_players('Michael %s' % i)
        expect_false = game.is_playable()

        self.assertEqual(False, expect_false, message) 

class Test_Check_Answers(unittest.TestCase):

      def test_purse_increase(self):
          game = Game.StartGame()
          message = 'The purse amount should have gone from zero to one'

          game.add_players('Nicole')
          game.roll(8)
          game.actions_taken_for_correct_answer()
          expect_one = game.purses[0]

          self.assertEqual(1, expect_one, message)

      def test_go_to_next_player(self):
          game = Game.StartGame()
          message = 'current_player was not increased by one'

          game.add_players('Stephanie')
          game.add_players('Jaime')
          game.roll(6)
          
          game.increment_current_player_position()
          expect_kira = game.players[game.current_player]

          self.assertEqual('Jaime', expect_kira, message)

      def test_reset_current_player_to_zero(self):
          game = Game.StartGame()
          message = 'current_player was not set to 0'

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

          game.add_players('Chris')
          game.add_players('Samantha')
          game.roll(3)

          expect_bool = game.actions_taken_for_correct_answer()

          self.assertIsInstance(expect_bool, bool, message)

      def test_player_won(self):
          game = Game.StartGame()
          message = 'expect_false should be False'

          game.add_players('Tom')
          game.add_players('Ana')
          game.current_player = 0
          game.purses[0] = 6

          expect_false = game._did_player_win()

          self.assertEqual(False, expect_false, message)
        

        
if __name__ == '__main__':
    unittest.main()