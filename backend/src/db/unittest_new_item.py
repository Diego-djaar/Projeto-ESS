import unittest
from itens_database import Item

class Test_new_item(unittest.TestCase):
    def test_valid_item(self):
        self.assertEqual((Item.new_item(self,
                                        id=12345678,
                                        nome="Camisa vermelha",
                                        description="Camisa de linho vermelha",
                                        price="29.99",
                                        quantidade=8,
                                        img="image.png"))[1][0], "SUCCESS"
                                        )
    def test_valid_item_no_img(self):
        self.assertEqual((Item.new_item(self,
                                        id=12345678,
                                        nome="Camisa vermelha",
                                        description="Camisa de linho vermelha",
                                        price="29.99",
                                        quantidade=8))[1][0], "SUCCESS"
                                        )
    
    def test_invalid_item_ID_length(self):
        self.assertEqual((Item.new_item(self,
                                        id=123456789, # 9 digitos
                                        nome="Camisa vermelha",
                                        description="Camisa de linho vermelha",
                                        price="29.99",
                                        quantidade=8))[1][0], "ID_LENGTH"
                                        )
    
    def test_invalid_item_invalid_img(self):
        self.assertEqual((Item.new_item(self,
                                        id=12345678,
                                        nome="Camisa vermelha",
                                        description="Camisa de linho vermelha",
                                        price="29.99",
                                        quantidade=8,
                                        img="aaaaa"))[1][0], "PATH"
                                        )
    
        
if __name__ == '__main__':
    unittest.main()