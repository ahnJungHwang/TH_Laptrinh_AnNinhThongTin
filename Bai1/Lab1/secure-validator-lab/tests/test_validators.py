import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from securevalidator import (
    validate_email, validate_url, validate_filename,
    sanitize_sql_input, sanitize_html_input
)

class TestValidators(unittest.TestCase):
    def setUp(self):
        print("\n Running:", self._testMethodName)

    def test_validate_email_valid(self):
        self.assertTrue(validate_email("user@example.com"))

    def test_validate_email_invalid(self):
        self.assertFalse(validate_email("user@@example..com"))
        self.assertFalse(validate_email("user.@gmail.com"))

    def test_validate_url_valid(self):
        self.assertTrue(validate_url("https://example.com"))

    def test_validate_url_invalid(self):
        self.assertFalse(validate_url("ftp://example.com"))
        self.assertFalse(validate_url("http://.com"))
        self.assertFalse(validate_url("http://exampl$e.com"))

    def test_validate_filename_valid(self):
        self.assertTrue(validate_filename("report.pdf"))

    def test_validate_filename_traversal(self):
        self.assertFalse(validate_filename("../../etc/passwd"))
        self.assertFalse(validate_filename("a.1txt"))
        self.assertFalse(validate_filename("shell.php"))

    def test_sanitize_sql_input_injection(self):
        input_str = "' OR 1=1 --"
        sanitized = sanitize_sql_input(input_str)
        self.assertNotIn("'", sanitized)
        self.assertNotIn("--", sanitized)
        self.assertNotIn("OR", sanitized.upper())

    def test_sanitize_sql_input_safe_text(self):
        input_str = "hello world"
        sanitized = sanitize_sql_input(input_str)
        self.assertEqual(sanitized, "hello world")

    def test_sanitize_html_input_script(self):
        input_str = '<script>alert("XSS")</script>'
        sanitized = sanitize_html_input(input_str)
        self.assertEqual(sanitized, '&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;')

    def test_sanitize_html_input_safe_text(self):
        input_str = "Hello World"
        sanitized = sanitize_html_input(input_str)
        self.assertEqual(sanitized, "Hello World")


if __name__ == "__main__":
    unittest.main()
