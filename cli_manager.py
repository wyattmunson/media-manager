import sys

def flag_processor():
    print(sys.argv)
    all_args = sys.argv
    if "--debug" in all_args:
        print("found debug ")

# flag_processor()

def get_input(prompt=">: ", leading_newline=True, trailing_newline=True):
    if leading_newline: print("")
    response = input(prompt)
    if trailing_newline: print("")
    
    return response
    