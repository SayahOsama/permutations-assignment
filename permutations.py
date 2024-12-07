
def unique_permutations(str):
    
    def backtrack(start):
        if start == len(str):
            unique_permutations.add("".join(current))
            return
        
        for i in range(start,len(str)):
            current[start], current[i] = current[i], current[start]
            backtrack(start+1)
            current[start], current[i] = current[i], current[start]
        
    unique_permutations = set()
    current = list(str)
    backtrack(0)
    return unique_permutations


def permutations(str):
    
    def backtrack(start):
        if start == len(str):
            permutations.append("".join(current))
            return
        
        for i in range(start,len(str)):
            current[start], current[i] = current[i], current[start]
            backtrack(start+1)
            current[start], current[i] = current[i], current[start]
        
    permutations = []
    current = list(str)
    backtrack(0)
    return permutations

print(permutations("123"))
print(permutations("121"))
print(list(unique_permutations("121")))