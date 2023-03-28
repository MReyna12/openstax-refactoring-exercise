import refactoring_exercise as Game
import unittest

class Test_Game(unittest.TestCase):
    player_information = Game.Players()
    
    def test_add_a_player(self):
        self.player_information.add_players('Michael')
        container = self.player_information.players
        message = 'Player was not added to the players list'
        self.assertIn('Michael', container, message)    

        

        
if __name__ == '__main__':
    unittest.main()