def composer(stringFunc, listFunc):
    def func(li):
        return listFunc(map(stringFunc, li))
    return func

li = ["hello", "world", "this", "is", "a", "list"]
function = composer(str.upper, sorted)
print(function(li))
