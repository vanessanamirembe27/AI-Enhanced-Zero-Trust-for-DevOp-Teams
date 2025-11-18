import os

def test_policy_exists():
    assert os.path.exists("zero-trust-poc/policies/network-policy.json")