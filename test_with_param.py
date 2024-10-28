import pytest
import yaml
from times import time_range, compute_overlap_time

# load fixture.yaml 
def load_yaml_data():
    with open("fixture.yaml", "r") as file:
        return yaml.safe_load(file)

# parametrization
yaml_data = load_yaml_data()

@pytest.mark.parametrize("test_case", yaml_data)
def test_compute_overlap_time(test_case):
    # time ranges and expected results
    case_data = list(test_case.values())[0]
    time_range_1 = case_data["time_range_1"]
    time_range_2 = case_data["time_range_2"]
    expected = [tuple(pair) for pair in case_data["expected"]]

    range1 = time_range(*time_range_1)
    range2 = time_range(*time_range_2)

    result = compute_overlap_time(range1, range2)

    assert result == expected


def test_input_validation():
    with pytest.raises(ValueError):
        # End time before start time
        time_range("2023-10-20 12:00:00", "2023-10-20 10:00:00")
