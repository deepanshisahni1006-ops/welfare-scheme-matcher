def is_age_eligible(age, min_age=None, max_age=None):
    """Return True if age is inside the scheme's age limits.

    min_age or max_age can be None, which means "no limit".
    """
    if min_age is not None and age < min_age:
        return False
    if max_age is not None and age > max_age:
        return False
    return True


def is_income_eligible(income, max_income=None):
    """Return True if income is within the scheme's limit.

    max_income=None means the scheme has no income limit."""
    if max_income is not None and income > max_income:
        return False
    return True


def is_category_eligible(category, allowed_categories=None):
    """Return True if the user's category is allowed by the scheme.

    allowed_categories=None means the scheme is open to every category."""
    if allowed_categories is None:
        return True
    return category in allowed_categories


def is_state_eligible(state, allowed_states=None):
    """Return True if the user's state is allowed. None means all India."""
    if allowed_states is None:
        return True
    return state in allowed_states


def is_occupation_eligible(occupation, allowed_occupations=None):
    """Return True if the user's occupation is allowed. None means any occupation."""
    if allowed_occupations is None:
        return True
    return occupation in allowed_occupations


def is_eligible(user, scheme):
    """Return True only if the user passes every rule of the scheme."""
    return (
        is_age_eligible(user["age"], scheme.get("min_age"), scheme.get("max_age"))
        and is_income_eligible(user["income"], scheme.get("max_income"))
        and is_category_eligible(user["category"], scheme.get("categories"))
        and is_state_eligible(user["state"], scheme.get("states"))
        and is_occupation_eligible(user["occupation"], scheme.get("occupations"))
    )


def filter_schemes(user, schemes):
    """Return only the schemes the user is eligible for."""
    return [scheme for scheme in schemes if is_eligible(user, scheme)]