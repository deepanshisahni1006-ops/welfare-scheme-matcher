def is_age_eligible(age, min_age=None, max_age=None):
    """Return True if age is inside the scheme's age limits.

    min_age or max_age can be None, which means "no limit".
    """
    if min_age is not None and age < min_age:
        return False
    if max_age is not None and age > max_age:
        return False
    return True