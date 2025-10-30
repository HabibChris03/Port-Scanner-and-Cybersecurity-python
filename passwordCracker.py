import time

password = input("Enter password: ")
guess = []
chars = "ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
start = time.time()
for val in range(0, len(password)):
    a = [i for i in chars]
    for y in range(val):
        a=[x + i for i in chars for x in a]
    guess =guess + a
    if password in guess:
        print("Password Found" + password)
        break
end = time.time()
clock= end - start
print("Password Found\n" + password)
print("Time Taken:", clock)