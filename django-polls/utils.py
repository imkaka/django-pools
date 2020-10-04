class Dummy:
    
    def foo(self):
        pass
        
    @classmethod
    def bar(cls):
        pass
        
print(Dummy.foo is Dummy.foo)
print(Dummy.bar is Dummy.bar)        
