import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunc(unittest.TestCase):
    
    # Позитивные тесты
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
    
    # Негативные тесты
    def test_negative_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)
    
    def test_zero_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)
    
    def test_triangle_inequality(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 10)
    
    def test_invalid_input_type(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 2, 3)

if __name__ == '__main__':
    unittest.main()