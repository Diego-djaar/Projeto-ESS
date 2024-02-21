import unittest
from itens_database import Item

class Test_is_image_path(unittest.TestCase):
    def test_path(self):
        self.assertTrue(Item.is_image_path("foto.jpg"))
        self.assertTrue(Item.is_image_path("imagem.PNG"))
        self.assertTrue(Item.is_image_path("picture.png"))

    def test_path_with_other_extensions(self):
        self.assertFalse(Item.is_image_path("documento.pdf"))
        self.assertFalse(Item.is_image_path("arquivo.txt"))
        self.assertFalse(Item.is_image_path("?.extensao"))

    def test_path_with_more_than_one_point(self):
        self.assertFalse(Item.is_image_path("arquivo.com.jpg"))
        self.assertFalse(Item.is_image_path("documento.pdf.jpg"))
        self.assertFalse(Item.is_image_path("item..jpg"))

if __name__ == '__main__':
    unittest.main()
