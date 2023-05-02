# class FileStream:

#     def __init__(self, path, mode) -> None:
#         self.path = path
#         self.mode = mode

#     def __enter__(self):
#         self.filestream = open(self.path, self.mode)
#         return self.filestream

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.filestream.close()

# with FileStream("another.txt","w") as f:
#     f.write("Some Text")

from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with filestream("somefile.txt","w") as f:
    f.write("Some Text in a File")
