# To an object be a context manager, it must implement the methods:
#   __enter__()
#   __exit__()
#
# Use:
#   with expression as x:
#       body
# Where:
#   expression  -> must return an object that implements both __enter__() and __exit__() methods (context manager)
#   x           -> is assigned to __enter__() return value, if "as" keyword is used
#   __enter__() -> initializes the context manager. If an exception occurs, the execution is interrupted and the
#                  exception is raised. If the execution is successful, the body of with statement is executed
#   body        -> body can either execute without error or can be interrupted by an exception
#                  if the execution is successful, the __exit__() method is called
#                  if the execution raises an exception, __exit__() is called with additional parameters related to the
#                  exception