# python -m unittest -v
# [After pip install coverage] coverage run --include=vectortypes.py tests.py; coverage report; coverage html
import unittest
from vectortypes import Vector2

class TestVector2Constructor(unittest.TestCase):
    def test_create_empty_vector(self):
        '''Vector2() returns vector with coords (0, 0)'''
        v = Vector2()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)

    def test_create_vector_from_int(self):
        '''Vector2(2) returns vector with coords (2, 2)'''
        v = Vector2(2)
        self.assertEqual(v.x, 2)
        self.assertEqual(v.y, 2)

    def test_create_vector_from_float(self):
        '''Vector2(2.5) returns vector with coords (2.5, 2.5)'''
        v = Vector2(2.5)
        self.assertEqual(v.x, 2.5)
        self.assertEqual(v.y, 2.5)
    
    def test_create_vector_from_int_and_float(self):
        '''Vector2(3, 4.4) returns vector with coords (3, 4.4)'''
        v = Vector2(3, 4.4)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4.4)

    def test_create_vector_from_float_and_int(self):
        '''Vector2(3.3, 4) returns vector with coords (3.3, 4)'''
        v = Vector2(3.3, 4)
        self.assertEqual(v.x, 3.3)
        self.assertEqual(v.y, 4)

    def test_create_vector_from_two_floats(self):
        '''Vector2(3.3, 4.4) returns vector with coords (3.3, 4.4)'''
        v = Vector2(3.3, 4.4)
        self.assertEqual(v.x, 3.3)
        self.assertEqual(v.y, 4.4)

    def test_create_vector_from_two_ints(self):
        '''Vector2(3, 4) returns vector with coords (3, 4)'''
        v = Vector2(3, 4)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)

    def test_create_vector_from_string(self):
        '''Vector2('a') raises an Exception'''
        with self.assertRaises(TypeError):
            Vector2('a')

    def test_create_vector_from_iterable(self):
        '''Vector2((2,2)) raises an Exception'''
        with self.assertRaises(TypeError):
            Vector2((2, 2))

    def test_create_vector_from_string_and_int(self):
        '''Vector2('3', 4) raises an Exception'''
        with self.assertRaises(TypeError):
            Vector2('3', 4)

    def test_create_vector_from_int_and_string(self):
        '''Vector2(3, '4') raises an Exception'''
        with self.assertRaises(TypeError):
            Vector2(3, '4')
    
    def test_create_vector_from_more_than_2_dimensions(self):
        '''Vector2(3, 4, 5) raises an Exception'''
        with self.assertRaises(ValueError):
            Vector2(3, 4, 5)

class TestVector2DunderMethods(unittest.TestCase):
    def test_dunder_len(self):
        '''Length of Vector2 is always 2'''
        self.assertEqual(len(Vector2()), 2)
        self.assertEqual(len(Vector2(4, 9)), 2)

    def test_dunder_repr(self):
        '''Shows correct object representations'''
        self.assertEqual(Vector2(3, 4).__repr__(), 'Vector2(3,4)')
        self.assertEqual(Vector2(3.3, 4).__repr__(), 'Vector2(3.3,4)')
        self.assertEqual(Vector2(7.239).__repr__(), 'Vector2(7.239,7.239)')

    def test_dunder_str(self):
        '''Shows correct object string'''
        self.assertEqual(Vector2(1,1).__str__(), "{'x': 1, 'y': 1, 'magnitude': 1.4142135623730951, 'angle': 45.0}")
        self.assertEqual(Vector2(3,4).__str__(), "{'x': 3, 'y': 4, 'magnitude': 5.0, 'angle': 53.13010235415598}")

    def test_dunder_eq(self):
        '''Check vector equality'''
        v1 = Vector2(1,1)
        v2 = Vector2(1,1)
        v3 = Vector2(1,2)
        v4 = Vector2(2,1)
        v5 = Vector2(1.0,1.000)
        self.assertEqual(v1==v2, True)
        self.assertEqual(v1==v5, True)
        self.assertEqual(v1==v3, False)
        self.assertEqual(v1==v4, False)

        with self.assertRaises(TypeError):
            v1 == 1

    def test_dunder_ne(self):
        '''Check vector inequality'''
        v1 = Vector2(1,1)
        v2 = Vector2(1,1)
        v3 = Vector2(1,2)
        v4 = Vector2(2,1)
        v5 = Vector2(1.0,1.000)
        self.assertEqual(v1!=v2, False)
        self.assertEqual(v1!=v5, False)
        self.assertEqual(v1!=v3, True)
        self.assertEqual(v1!=v4, True)

        with self.assertRaises(TypeError): 
            v1 != 1

    def test_dunder_iter_and_next(self):
        '''Check iterable behaviour works correctly'''
        v = Vector2(3, 4)

        for index, coord in enumerate(v):
            if index == 0:
                self.assertEqual(coord, 3)
            elif index == 1:
                self.assertEqual(coord, 4)
        
        i = iter(v)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 4)

        with self.assertRaises(StopIteration): 
            next(i)

    def test_dunder_getitem(self):
        '''Object key values are returned correctly'''
        v = Vector2(3, 4)
        self.assertEqual(v[0], 3)
        self.assertEqual(v[1], 4)
        self.assertEqual(v['x'], 3)
        self.assertEqual(v['y'], 4)
        self.assertEqual(v['magnitude'], 5)
        self.assertEqual(v['angle'], 53.13010235415598)

        with self.assertRaises(KeyError):
            v[-1]
        
        with self.assertRaises(KeyError):
            v[2]
        
        with self.assertRaises(KeyError):
            v['test']
        
        with self.assertRaises(TypeError):
            v[('','')]

    def test_dunder_setitem(self):
        '''Object item assignment raises Exception'''
        v = Vector2()
        with self.assertRaises(TypeError):
            v[0] = 2


if __name__ == "__main__":
    unittest.main(verbosity=2)
