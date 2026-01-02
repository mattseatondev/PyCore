# import pytest
# import numpy as np

# class NotEvenError(ValueError):
#     """Raised when a value is not an even int"""
#     def __init__(self, val):
#         self.value = val
#         super().__init__(f"Expected an even integer, got {val!r}")

# def even_only(x: int):
#     if x % 2 == 0:
#         return x
#     raise NotEvenError(x)

# def test_even_only_raises():
#     with pytest.raises(NotEvenError) as excinfo:
#         even_only(1)

#     assert "Expected an even integer" in str(excinfo.value)


# # Approximate Equality

# def test_floats():
#     assert(0.1 + 0.2) == pytest.approx(0.3)
    
# def test_arrays():
#     a = np.array([1.0, 2.0, 3.0])
#     b = np.array([0.9999, 2.0001, 3.0])
#     assert a == pytest.approx(b)
    
# # Expected Exceptions

# def test_recursion_depth():
#     with pytest.raises(RuntimeError) as excinfo:
#         def f():
#             f()
            
#         f()
#     assert 'maximum recursion' in str(excinfo.value)
    
# # ExceptionGroup

# class FiveSucksException(Exception):
#     """Raised because five can suck it"""
#     def __init__(self, val):
#         self.value = val
#         super().__init__(f"Five is the result of two monkeys having sex with a fish-frog {val!r}")

# def process_items(items):
#     errors = []
#     for item in items:
#         if item < 0:
#             errors.append(ValueError(f"Negative value: {item}"))
#         elif item == 0:
#             errors.append(TypeError(f"Zero is not allowed: {item}"))
#         elif item == 5:
#             errors.append(FiveSucksException(item))
    
#     if errors:
#         raise ExceptionGroup("Item processing errors", errors)

#     return [item * 2 for item in items]

# def test_exception_in_group():
#     items = [-1, -2, 0, 10, -4, 5, 3, 1, 0, -12, 7, 7]
#     with pytest.raises(ExceptionGroup) as excinfo:
#         process_items(items)
#     types_raised = [type(e) for e in excinfo.value.exceptions]
#     assert ValueError in types_raised
#     assert TypeError in types_raised
#     assert FiveSucksException in types_raised
#     # assert ValueError in excinfo.value
#     # with pytest.RaisesGroup(ValueError):
#     #     raise ExceptionGroup('group msg', [ValueError('value msg')])
#     # with pytest.RaisesGroup(ValueError, TypeError):
#     #     raise ExceptionGroup('msg', [ValueError('foo'), TypeError('bar')])