import unittest
import part1

class TestSantaDeliveries(unittest.TestCase):
    def test_simple_build_delivery_grid(self):
        grid = part1.build_delivery_grid('>')
        self.assertEqual(grid[(0,0)], 1)
        self.assertEqual(grid[(1,0)], 1)

    def test_all_directions(self):
        grid = part1.build_delivery_grid('^>v<')
        self.assertEqual(grid[(0,0)], 2)
        self.assertEqual(grid[(0,1)], 1)
        self.assertEqual(grid[(1,1)], 1)
        self.assertEqual(grid[(0,1)], 1)

    def test_up_down(self):
        grid = part1.build_delivery_grid('^v^v^v^v^v')
        self.assertEqual(grid[(0,0)], 6)
        self.assertEqual(grid[(0,1)], 5)

if __name__ == '__main__':
    unittest.main()
