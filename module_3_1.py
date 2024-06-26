calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(strin):
    count_calls()
    info = (len(strin),strin.upper(),strin.lower())
    return info

def is_contains(string,list_to_search):
    count_calls()
    for i in range(0,len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)


