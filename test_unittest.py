import refactoring_exercise as Game
import unittest

class Test_Players_Class(unittest.TestCase):
    player_information = Game.Players()
    player_container = player_information.players
    
    def test_add_a_player(self):
        self.player_information.add_players('Michael')
        self.player_information.add_players('Hillery')
        message = 'Player was not added to the players list'
        self.assertIn('Michael', self.player_container, message)    

    def test_how_many_players(self):
        number_players = self.player_information.how_many_players
        message = 'There is less or more than one person in player_container'
        self.assertEqual(number_players, 2, message)

    def test_correct_number_players(self):
        two_players = self.player_information.is_playable()
        self.assertEqual(True, two_players, 'There are less than two or more than three players added to the players list')


        

        
if __name__ == '__main__':
    unittest.main()