from src.data_loader import load_schemes
from src.eligibility import (
    filter_schemes,
    is_age_eligible,
    is_category_eligible,
    is_income_eligible,
    is_occupation_eligible,
    is_state_eligible,
)


def make_user(**changes):
    """A starting user. Pass changes like make_user(age=20)."""
    user = {
        "age": 30,
        "income": 100000,
        "category": "General",
        "state": "Punjab",
        "occupation": "job",
    }
    user.update(changes)
    return user


def matching_ids(user):
    return [scheme["id"] for scheme in filter_schemes(user, load_schemes())]


def test_age_inside_limits():
    assert is_age_eligible(20, 18, 25) is True


def test_age_too_young():
    assert is_age_eligible(17, 18, 25) is False


def test_age_no_limits():
    assert is_age_eligible(70, None, None) is True


def test_income_at_the_limit_is_allowed():
    assert is_income_eligible(250000, 250000) is True


def test_income_above_the_limit():
    assert is_income_eligible(250001, 250000) is False


def test_income_no_limit():
    assert is_income_eligible(900000, None) is True


def test_category_allowed():
    assert is_category_eligible("SC", ["SC", "ST"]) is True


def test_category_not_allowed():
    assert is_category_eligible("General", ["SC", "ST"]) is False


def test_category_open_to_all():
    assert is_category_eligible("OBC", None) is True


def test_state_open_to_all():
    assert is_state_eligible("Punjab", None) is True


def test_state_not_allowed():
    assert is_state_eligible("Punjab", ["Kerala"]) is False


def test_occupation_not_allowed():
    assert is_occupation_eligible("student", ["farmer"]) is False


def test_sc_student_gets_only_the_scholarship():
    user = make_user(age=20, income=200000, category="SC", occupation="student")
    assert matching_ids(user) == ["pms-sc"]


def test_farmer_gets_only_pm_kisan():
    assert matching_ids(make_user(occupation="farmer")) == ["pm-kisan"]


def test_worker_gets_only_pm_sym():
    assert matching_ids(make_user(income=150000)) == ["pm-sym"]


def test_scholarship_income_limit_boundary():
    at_limit = make_user(age=20, income=250000, category="SC", occupation="student")
    above_limit = make_user(age=20, income=250001, category="SC", occupation="student")
    assert "pms-sc" in matching_ids(at_limit)
    assert "pms-sc" not in matching_ids(above_limit)


def test_every_scheme_has_an_official_link():
    for scheme in load_schemes():
        assert scheme["official_link"].startswith("https://")
        