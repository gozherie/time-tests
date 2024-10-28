from times import time_range, compute_overlap_time
import pytest

@pytest.mark.parametrize(
    "time_range_1_args, time_range_2_args, expected",
    [
        # test given inputs
        (
            ("2010-01-12 10:00:00", "2010-01-12 12:00:00"), 
            ("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [
                ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
            ]
        ),
        # test no overlap
        (
            ("2010-01-12 08:00:00", "2010-01-12 09:00:00"),
            ("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            []
        ),
        # test multiple intervals
        (
            ("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60),
            ("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2, 60),
            [
                ('2010-01-12 10:30:30', '2010-01-12 10:59:30')
            ]
        ),
        # test end to start
        (
            ("2010-01-12 10:00:00", "2010-01-12 10:30:00"),
            ("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
            []
        ),
    ]
)
def test_compute_overlap_time(time_range_1_args, time_range_2_args, expected):
    
    range1 = time_range(*time_range_1_args)
    range2 = time_range(*time_range_2_args)
    result = compute_overlap_time(range1, range2)

    assert result == expected

def test_input_validation():
    with pytest.raises(ValueError):
        # End time before start time
        time_range("2023-10-20 12:00:00", "2023-10-20 10:00:00")
