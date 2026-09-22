import sys

def test_matrix_version():
    major = sys.version_info.major
    minor = sys.version_info.minor
    
    print(f"\nRunning on Python {major}.{minor}")
    
    # Intentionally fail ONLY when running Python 3.11
    if (major, minor) == (3, 11):
        assert False, "Intentional failure to test matrix isolation in Python 3.11"
        
    # For 3.10 and 3.12, this test passes!
    assert True