# def first_unique1(string):
#     if len(string) == 1:
#         return string
#     if string.upper().isupper():
#         for index,char in enumerate(string):
#             if index != 0 and index != len(string)-1:
#                  if char != string[index+1] and char != string[index-1]:
#                     return char
#                     break
#             elif index == 0 and char != string[index+1]:
#                  return char
#                  break
#             elif index == len(string)-1 and char != string[index-1]:
#                  return char
#                  break
#             elif index == len(string)-1:
#                  return -1
#     else:
#         return None

def first_unique(string):
    if string.upper().isupper(): # if it has letters
        if len(string) == 1:
            return string
        else:
            letter = {}
            for index,char in enumerate(string):
                if letter.get(char) == None:
                    letter[char] = [1,index]
                else:
                    letter[char] = [letter[char][0]+1,index]

            for key,value in letter.items():
                if value[0] == 1:
                    return key
                
    else:
        return None





print(first_unique('aabbcdd123'))
print(first_unique('a'))
print(first_unique('112233'))
