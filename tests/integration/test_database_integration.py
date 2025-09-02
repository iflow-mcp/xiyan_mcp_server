import pytest
from src.xiyan_mcp_server.utils.db_util import remove_sql_comments, preprocess_sql_query

def test_remove_sql_comments():
    # Test removing SQL comments
    sql_with_comments = "-- This is a comment\nSELECT * FROM users; /* Another comment */"
    expected = "SELECT * FROM users;"
    result = remove_sql_comments(sql_with_comments)
    assert result == expected

def test_preprocess_sql_query():
    # Test preprocessing SQL query
    sql_without_semicolon = "SELECT * FROM users"
    result = preprocess_sql_query(sql_without_semicolon)
    assert result == "SELECT * FROM users;"

def test_import():
    # Basic test to ensure the module can be imported
    assert True

if __name__ == '__main__':
    pytest.main()