from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large, short)
    print(result)
    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]
    
    assert result == expected

# No overlap intervals
def test_no_overlap():
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    
    result = compute_overlap_time(range1, range2)
    print(result)
    expected = []
    
    assert result == expected

# both contain several intervals each
def test_multiple_intervals_each():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2, 60)
    
    result = compute_overlap_time(range1, range2)
    print(result)
    expected = [
        ('2010-01-12 10:30:30', '2010-01-12 10:59:30')
    ]
    
    assert result == expected

# two time ranges that end exactly at the same time when the other starts
def test_end_exactly_at_start():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00")
    
    result = compute_overlap_time(range1, range2)
    print(result)
    expected = []
    
    assert result == expected
