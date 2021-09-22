Python 3.8.10 (default, Jun  2 2021, 10:49:15)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and true
False
>>> 1==1 and 2 !=1
True
>>> "test" == "test"
True
>>> 1 ==1 or 2!=1
True
>>> True and 1==1
True
>>> False and 0! =0
  File "<stdin>", line 1
    False and 0! =0
               ^
SyntaxError: invalid syntax
>>> False and 0!=0
False
>>> True or 1 == 1
True
>>> "test == "testing"
  File "<stdin>", line 1
    "test == "testing"
              ^
SyntaxError: invalid syntax
>>> "test == "testing"
  File "<stdin>", line 1
    "test == "testing"
              ^
SyntaxError: invalid syntax
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 1000 == 1000)
False
>>> not(1 != 10 or 3 == 4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 ==1 and (not("tesing" == 1 or 1 ==0))
True
>>> "chunky" == "bacon" and (not(3 == 4 or 3 == 3))
False
>>> 3 == 3 and (not("testing" == "testing" or "Python" == "Fun"))
False
