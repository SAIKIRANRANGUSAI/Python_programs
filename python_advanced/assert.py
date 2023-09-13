#test the condition.if it returns false then the AssertionError is raised

x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
