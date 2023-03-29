import refactoring_exercise as Game
import unittest
import random

class Test_Players_Class(unittest.TestCase):  
    
    def test_add_a_player(self):
        player_information = Game.Players()
        player_information.add_players('Michael')
        player_information.add_players('Hillery')
        player_container = player_information.players
        message = 'Player was not added to the players list'
        self.assertIn('Michael', player_container, message)    

    def test_how_many_players(self):
        player_information = Game.Players()
        player_information.add_players('Michael')
        player_information.add_players('Hillery')
        number_players =  player_information.how_many_players
        message = 'There is less or more than one person in player_container'
        self.assertEqual(number_players, 2, message)

    def test_one_player(self):
        player_information = Game.Players()
        player_information.add_players('Michael')
        expectFalse = player_information.is_playable() 
        self.assertEqual(False, expectFalse, 'The game should not be playable - check that only one player has been added.')   

    def test_correct_number_players(self):
        player_information = Game.Players()
        player_information.add_players('Michael')
        player_information.add_players('Hillery')
        expectTrue = player_information.is_playable()
        self.assertEqual(True, expectTrue, 'There are less than two or more than three players added to the players list')

    def test_more_than_three_players(self):
        player_information = Game.Players()
        for i in range(5):
          player_information.add_players('Michael %s' % i)
        expectFalse = player_information.is_playable()
        self.assertEqual(False, expectFalse, 'The game should not be playable because more than three players were added.') 

""" class Test_Check_Answers(unittest.TestCase):
      player_information = Game.Players()
      answers = Game.Check_Answer()
      game = Game.StartGame()

      def test_correctly_answered(self):
          self.player_information.add_players('Michael')
          self.player_information.add_players('Jordan')
          print('This is players list: %s' % self.player_information.players)
          print('This is current_player value: %s' % self.player_information.current_player)
          self.game.roll(8)
          self.answers.was_correctly_answered() """
        

        
if __name__ == '__main__':
    unittest.main()