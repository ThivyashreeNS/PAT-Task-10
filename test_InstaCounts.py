"""test_InstaCounts .py"""

import pytest
from Task_10 import InstaCounts

# Test if the extract_counts method extracts correct follower and following counts
def test_extract_counts():
    obj = InstaCounts()
    followers_count, following_count = obj.extract_counts()
    assert followers_count == "202K"
    assert following_count == "7"
    obj.close_driver()