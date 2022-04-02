import unittest
from name_function import get_formatted_name

# We create a class, which will contain a series of unit tests
# for get_formatted_name()
class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    
    def test_first_last_name(self):
        """Do names like 'Blessed Manokore' work?"""
        formatted_name = get_formatted_name('blessed', 'manokore')
        # Assert methods verify that a result you received matches
        # the result you expected to receive.
        self.assertEqual(formatted_name, 'Blessed Manokore')
        
    def test_first_last_middle_name(self):
        """Do names like Blessed Nyasha Manokore work?"""
        formatted_name = get_formatted_name('blessed', 'manokore', 'nyasha')
        self.assertEqual(formatted_name, 'Blessed Nyasha Manokore')
        
unittest.main()