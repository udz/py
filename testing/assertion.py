class Base:
    def foo(self):
        return 'foo'
    
from Library import Base

assert hasattr(Base,'foo'), "The library is broken. Doesn't have method foo"

class Derived(Base):
    def bar(self):
        return self.foo()
