class CoffeeShopError(Exception):
    """Base exception class for all coffee shop exceptions"""
    pass

class ValidationError(CoffeeShopError):
    """Raised when validation fails"""
    pass

class CustomerValidationError(ValidationError):
    """Customer-specific validation errors"""
    pass

class CoffeeValidationError(ValidationError):
    """Coffee-specific validation errors"""
    pass

class OrderValidationError(ValidationError):
    """Order-specific validation errors"""
    pass