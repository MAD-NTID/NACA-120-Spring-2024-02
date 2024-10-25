# if user enter a letter, you'll get exception
# but this is the only way to code it
# so you must handle the error

try:
    age = int(input("Enter your age: "))
except FileExistsError:
    # ofc this error is never going to happen in this case we're asking for age not a file
    print("File not found")
except ValueError:
    print("You entered non-numeric data as age")
except:
    # Catch anything else cuz I am too lazy to figure out what the error is
    print("Well, we don't know what happened, but you do have an error")