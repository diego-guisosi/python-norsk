# super()
# Given a method resolution order and a class C, super() gives you an object which resolves methods using only the part
# of the MRO which comes after C. So, super() does not call the base class method. It calls the method of the
# class in the rest of the MRO that first matches the method name

# super() returns a proxy object which routes method calls

# types of proxies:
#   bound proxies -> bound to a specific class or instance
#   unbound proxies -> not bound to a class or instance (out of scope)

