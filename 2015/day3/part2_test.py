import unittest
import part2

class TestSantaDeliveries(unittest.TestCase):
    def test_simple_build_delivery_grid(self):
        grid = part2.build_delivery_grid('>')
        self.assertEqual(grid[(0,0)], 2)
        self.assertEqual(grid[(1,0)], 1)

    def test_all_directions(self):
        grid = part2.build_delivery_grid('^>v<')
        self.assertEqual(grid[(0,0)], 4)
        self.assertEqual(grid[(0,1)], 1)
        self.assertEqual(grid[(1,0)], 1)

    def test_up_down(self):
        grid = part2.build_delivery_grid('^v^v^v^v^v')
        self.assertEqual(grid[(0,0)], 2)
        self.assertEqual(grid[(0,1)], 1)
        self.assertEqual(grid[(0,-1)], 1)
        self.assertEqual(grid[(0,2)], 1)
        self.assertEqual(grid[(0,-2)], 1)
        self.assertEqual(grid[(0,3)], 1)
        self.assertEqual(grid[(0,-3)], 1)
        self.assertEqual(grid[(0,4)], 1)
        self.assertEqual(grid[(0,-4)], 1)
        self.assertEqual(grid[(0,5)], 1)
        self.assertEqual(grid[(0,-5)], 1)

if __name__ == '__main__':
    unittest.main()
