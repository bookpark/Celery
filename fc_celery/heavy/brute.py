# import zipfile
#
# import itertools
#
#
# def brute_force(password):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     attempts = 0
#     for password_length in range(1, 9):
#         for guess in itertools.product(alphabet, repeat=password_length):
#             attempts += 1
#             guess = ''.join(guess)
#             if guess == password:
#                 return 'password is {}. found in {} guesses.'.format(guess, attempts)
#             print(guess, attempts)
#
#
# print(brute_force('asdas'))

# chars = string.ascii_lowercase

# def add_char_to_list(ori_list=None):
#     if not ori_list:
#         return list(chars)
#     ret = []
#     for char in chars:
#         for item in ori_list:
#             ret.append(char + item)
#     return ret

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for password_length in range(1, 9):
    for guess in itertools.product(alphabet, repeat=password_length):
        guess = ''.join(guess)
        z = zipfile.ZipFile('origin.txt.zip')
        z.setpassword(bytes(guess, encoding='utf-8'))
        z.extract('origin.txt')
