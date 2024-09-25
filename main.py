import sys


def main_help_message():
    message = """MEDIA MANAGER
    
    COMMANDS:
    tran        Transfer files
    rewrite     Rewrite many file names
    """
    print(message)


print(sys.argv)

if len(sys.argv) == 1:
    main_help_message()