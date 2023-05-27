def count_vowels(string:str) -> int:
    string = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += string.count(i)
    return result

print(count_vowels(input("")))