"""PW-05B pure checks; no kernel/network operations."""
import unittest
from probe import classify_namespace


class NamespaceProbeTests(unittest.TestCase):
    def test_namespace_disallowed(self):
        self.assertEqual(classify_namespace(1, "net:[111]", None), "BLOCKED_OR_UNVERIFIED")

    def test_namespace_equal_to_host_is_not_isolation(self):
        self.assertEqual(classify_namespace(0, "net:[111]", "net:[111]"), "NOT_ISOLATED")

    def test_distinct_namespace_is_only_a_capability_probe(self):
        self.assertEqual(classify_namespace(0, "net:[111]", "net:[222]"), "NETWORK_NAMESPACE_CREATED_ONLY")

    def test_missing_namespace_ids_fail_closed(self):
        self.assertEqual(classify_namespace(0, None, "net:[222]"), "BLOCKED_OR_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
