class InsufficientBalanceError(Exception):
    """Raised when a withdrawal amount exceeds the available balance."""
    pass

class InvalidPinError(Exception):
    """Raised when an invalid PIN is entered."""
    pass
