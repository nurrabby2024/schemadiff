"""Typed exceptions for SchemaDiff."""


class schemadiffError(Exception):
 """Base error for the whole package."""

 exit_code = 1


class ConfigurationError(schemadiffError):
 """Raised when configuration is invalid or missing."""

 exit_code = 2


class ValidationError(schemadiffError):
 """Raised when input data fails validation."""

 exit_code = 3


class NotFoundError(schemadiffError):
 """Raised when a requested resource does not exist."""

 exit_code = 4


class ConflictError(schemadiffError):
 """Raised when an operation conflicts with existing state."""

 exit_code = 5


class RateLimitError(schemadiffError):
 """Raised when a rate limit is exceeded."""

 exit_code = 6


class TimeoutError(schemadiffError):
 """Raised when an operation takes too long."""

 exit_code = 7


class UnsupportedError(schemadiffError):
 """Raised for unsupported inputs or platforms."""

 exit_code = 8


class StateError(schemadiffError):
 """Raised when internal state is inconsistent."""

 exit_code = 9


def guard(condition, message, exc=ValidationError):
 """Raise exc(message) when condition is False."""
 if not condition:
 raise exc(message)