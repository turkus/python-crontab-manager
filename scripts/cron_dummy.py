import os


def create_dummy():
    os.system("touch %s/dummy.txt" % os.path.dirname(__file__))


if __name__ == "__main__":
    create_dummy()
