import time
a=10
b=20
try:
    print("1st try is running....")
    print(a+b)
    time.sleep(2)
except NameError as ne:
    print("NameError :",ne)
    time.sleep(2)
else:
    print("2nd try is running inside else....")
    time.sleep(2)
    try:
        b=5
        print(a+b)
        time.sleep(2)
        print(a+b+c)
        print("try within else runned successfully...")
        time.sleep(2)
    except NameError as ne:
        print("NameError:",ne)
        time.sleep(2)
    else:
        print("try within else runned successfully...")
        time.sleep(2)
    finally:
        print("try within else runned successfully...")
        time.sleep(2)
finally:
    print("Program runned successfully....")

