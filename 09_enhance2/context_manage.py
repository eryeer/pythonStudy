from contextlib import contextmanager


@contextmanager
def file(path, methd):
    f = open(path, methd)
    yield f
    f.close()


with file("./context_manage.py", "r") as f:
    read = f.read()
    print(read)
