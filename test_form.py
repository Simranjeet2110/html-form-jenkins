import unittest
from html.parser import HTMLParser

class FormChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])

class TestForm(unittest.TestCase):
    def test_required_fields(self):
        parser = FormChecker()

        with open("index.html", encoding="utf-8") as f:
            parser.feed(f.read())

        self.assertIn("form", parser.tags)
        self.assertIn("name", parser.ids)
        self.assertIn("email", parser.ids)
        self.assertIn("contact", parser.ids)
        self.assertIn("button", parser.tags)

if __name__ == "__main__":
    unittest.main()
