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
        game = Game.Players()
        message = 'There is less or more than one person in player_container'

        game.add_players('Michael')
        game.add_players('Hillery')
        number_players =  game.how_many_players

        self.assertEqual(number_players, 2, message)

    def test_one_player(self):
        game = Game.Players()
        message = 'The game should not be playable - check that only one player has been added.'

        game.add_players('Michael')
        expect_false = game.is_playable() 

        self.assertEqual(False, expect_false, message)   

    def test_correct_number_players(self):
        game = Game.Players()
        message = 'There are less than two or more than three players added to the players list'

        game.add_players('Michael')
        game.add_players('Hillery')
        expect_true = game.is_playable()

        self.assertEqual(True, expect_true, message)

    def test_more_than_three_players(self):
        game = Game.Players()
        message = 'The game should not be playable - check that more than three players were added.'
  
        for i in range(5):
          game.add_players('Michael %s' % i)
        expect_false = game.is_playable()

        self.assertEqual(False, expect_false, message) 

class Test_Check_Answers(unittest.TestCase):

      def test_purse_increase(self):
          game = Game.StartGame()
          message = 'The purse amount should have gone from zero to one'

          game.add_players('Michael')
          game.roll(8)
          game.was_correctly_answered()
          expect_one = game.purses[0]

          self.assertEqual(1, expect_one, message)
          
        

        
if __name__ == '__main__':
    unittest.main()