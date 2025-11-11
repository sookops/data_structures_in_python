from collections import defaultdict

# int를 기본값 팩토리로 사용
mydict = defaultdict(int)
mydict['a'] = 1
print(mydict['b'])	    # 기본값 0
print(mydict)		    # defaultdict(<class 'int'>, {'a': 1, 'b': 0})

# list를 기본값 팩토리로 사용
mydict2 = defaultdict(list)
mydict2[1] = ['a']
print(mydict2[2])	    # 기본값 []
print(mydict2)		    # defaultdict(<class 'list'>, {1: ['a'], 2: []})
