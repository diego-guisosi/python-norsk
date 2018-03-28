# C3 algorithm

# Subclasses come before base classes
# Base class order from class definition is preserved
# First two qualities are preserved no matter where you start in the inheritance graph


class A: pass
class B(A): pass
class C(A): pass

try:
    class D(B, A, C) : pass  # this will not compile, because C3 expect that subclasses come before base classes
except TypeError as e:
    print(str(e))
