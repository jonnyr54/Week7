import unittest

from adts.array import Array


class ArrayTest(unittest.TestCase):
    def setUp(self):
        self._array = Array(10)
        for i in range(len(self._array)):
            self._array[i] = i

    def test_len(self):
        size = len(self._array)
        self.assertTrue(10, size)

    def test_index_operators(self):
        #Arrange
        my_array = Array(5)
        
        #Act
        for i in range(5):
            my_array[i] = i

        #Assert
        
        for i in range(5):
            self.assertEqual(i, my_array[i])

    def test_clone(self):
        #Arrange & Act
        copy = self._array.clone()
        
        #Assert
        self.assertEqual(self._array, copy)

    def test_resize_should_be_size_five(self):
        #Arrange & Act
        self._array.resize(5)
        
        #Assert
        self.assertEqual(5, len(self._array))
        
    def test_resize_should_not_lose_data(self):
        #Arrange & Act
        self._array.resize(5)
        
        #Assert
        expected_sum = 10
        actual_sum = 0
        for i in range (len(self._array)):
            actual_sum += self._array[i]
            
        self.assertEqual(expected_sum, actual_sum)
        
        
    def test_resize_should_not_lose_data_when_resizing_larger(self):
        #Arrange & Act
        self._array.resize(51)
        
        #Assert
        expected_sum = 45
        actual_sum = 0
        for i in range (len(self._array)):
            if self._array[i] is not None:
                actual_sum += self._array[i]
            
        self.assertEqual(expected_sum, actual_sum)

    def test_eq_should_be_true(self):
        #Arrange
        array_2 = Array(10)
        for i in range (len(array_2)):
            array_2[i] = i
        
        #Act
        result = self._array == array_2
        
        #Assert
        self.assertTrue(result)
        
    def test_eq_should_be_false(self):
        #Arrange
        array_2 = Array(10)
        for i in range (len(array_2)):
            array_2[i] = -i
        
        #Act
        result = self._array == array_2
        
        #Assert
        self.assertFalse(result)
        
    def test_eq_should_be_false_for_other_type(self):
        #Arrange
        other = 'test'
        
        #Act
        result = self._array == other
        
        #Assert
        self.assertFalse(result)

    def test_iter(self):
        counter = 0 
        for i in self._array:
            self.assertEqual(counter, i)
            counter += 1

    def test_del_should_remove_five(self):
        #Arrange
        
        #Act
        del self._array[6]#delete the value five
        
        #Assert
        self._assertNotIn(5, self._array)
        
        
    def test_del_should_be_nine(self):
        #Arrange
        
        #Act
        del self._array[6]#delete the value five
        
        #Assert
        self._assertEqual(9, len(self._array))

    def test_contains(self):
        does_contain = 5 in self._array
        
        self.assertTrue(does_contain)

    def test_index_op_get_exception(self):
        with self.assertRaises(IndexError):
             self._array[100] = 5

    def test_index_op_set_exception(self):
        with self.assertRaises(IndexError):
            self._array[100] = 5

    def test_index_op_set_exception_should_raise_exception_on_boundary(self):
        with self.assertRaises(IndexError):
            self._array[10] = 5

    def test_index_op_set_exception_should_raise_exception_on_boundary_negative(self):
        with self.assertRaises(IndexError):
            self._array[-10] = 5


if __name__ == '__main__':
    unittest.main()
