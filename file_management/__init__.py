"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

-> file is a container in computer storage devices used for storing data.
When we want to read from or write to a file, we need to open it first. When we are done,
it needs to be closed so that the resources that are tied with the file are freed.


r	Open a file for reading. (default)
w	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Open a file for exclusive creation. If the file already exists, the operation fails.
a	Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Open in text mode. (default)
b	Open in binary mode.
+	Open a file for updating (reading and writing)
"""