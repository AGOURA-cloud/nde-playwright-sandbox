"""PW-04 auth gating is fail-closed, and never guesses credentials exist."""
import unittest
from auth_gate import classify

class AuthGateTests(unittest.TestCase):
    def test_no_auth(self):
        self.assertEqual(classify(1, "Not logged in"), "NO_AUTH")
    def test_auth_present_needs_permission(self):
        self.assertEqual(classify(0, "Logged in using ChatGPT"), "AUTH_PRESENT_NOT_APPROVED")
    def test_api_key_auth_present_needs_permission(self):
        self.assertEqual(classify(0, "Logged in using an API key"), "AUTH_PRESENT_NOT_APPROVED")
    def test_arbitrary_zero_exit_is_not_login_proof(self):
        self.assertEqual(classify(0, "OK"), "INDETERMINATE")
    def test_unknown_error_is_not_login_proof(self):
        self.assertEqual(classify(2, "network failure"), "INDETERMINATE")
    def test_any_error_with_not_logged_in_denies(self):
        self.assertEqual(classify(2, "Not logged in"), "NO_AUTH")

if __name__ == "__main__":
    unittest.main()
