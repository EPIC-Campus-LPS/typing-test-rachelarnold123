import time
n = 0
m = 0

start = time.time() #Starts timer
aaa = input("Type the Following: \nThis is a typing test \n")
typetest = "This is a typing test"
end = time.time() #Ends Timer
typetime = end - start #Calculates the time inbetween
if typetime > 10:
    print(f"You took wayyyyyy too long... in fact you took {typetime}")
if aaa == typetest:
    print(f"This took you a whole {typetime} seconds.")
    print("You did it!")

else:
    for l in typetest: #takes the amount of errors
        if l != aaa[n]:
            m += 1
    n += 1
    e = m / typetime
    print(first_difference(aaa, typetest))
    print(f"FAILED in {typetime} and you have {m} erros, averaging {e} error per second")