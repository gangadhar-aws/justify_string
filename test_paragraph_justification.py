import unittest
from justify_paragraph import justify_paragraph


class TestJustifyParagraph(unittest.TestCase):

    def test_single_word(self):
        paragraph = "Hello"
        page_width = 10
        expected_output = ["Hello     "]
        self.assertEqual(justify_paragraph(paragraph, page_width), expected_output)


    def test_multiple_words(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        page_width = 20
        expected_output = ["This   is  a  sample", "text      but      a", "complicated  problem", "to  be solved, so we", "are adding more text", "to   see   that   it", "actually      works."]

        self.assertEqual(justify_paragraph(paragraph=paragraph, page_width=page_width), expected_output)


    def test_long_word(self):
        paragraph = "Thisisasampletextbutacomplicatedproblemtobesolved,"
        page_width = 15
        expected_output = ["Thisisasampletextbutacomplicatedproblemtobesolved,"]
        self.assertEqual(justify_paragraph(paragraph, page_width), expected_output)


    def test_empty_paragraph(self):
        paragraph = ""
        page_width = 10
        expected_output = [""]
        self.assertEqual(justify_paragraph(paragraph, page_width), expected_output)


if __name__ == '__main__':
    unittest.main()