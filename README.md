This scripts work with **Sockets** and **Python**
for sending files and get it on server side via async mode.

For use this scripts you need have file
**buffer.py** on each side

File **async_server.py** get files and host-name as hash type.
Because for me host names has symbols what can't be used with decoding files.
That's why I send it as hash type.
Anyway maybe you don't need this option and IP will be enouth for you.
In **worker** func you can add any work logic for using this files, and get anoter before end.

File **client.py** get files as argument and send it to server side.
If you need, you can send many files in one time, just add more arguments to variable **files**

File **run_init.sh** make init process for **async_server.py**
and run in automatic with your server

Hope it will help you!