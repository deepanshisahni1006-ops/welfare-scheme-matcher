def is_age_eligible(age, min_age=None, max_age=None):
    """Return True if age is inside the scheme's age limits.

    min_age or max_age can be None, which means "no limit".
    """
    if min_age is not None and age < min_age:
        return False
    if max_age is not None and age > max_age:
        return False
    return True

def is_income_eligible(income,max_income=None):
    """Return True if income is within the scheme's limit.
    
    max_income=None means the scheme has no income limit."""
    if max_income is not None and income>max_income:
        return False
    return True

def is_category_eligible(category, allowed_categories=None):
    """Return True if the user's category is allowed by the scheme.
    
    allowed_categories=None means the scheme is open to every category."""
    if allowed_categories is None:
        return True
    return category in allowed_categories
