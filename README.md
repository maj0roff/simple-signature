# simple-signature
A simple module to create and validate a request signature when communicating between the client and the server.
It helps to avoid manual requests from the user until they find the signature creation principle and your unique value.

It works like this:
A string with the beginning "<uniqueValue*>"
To this string we add their values from the arguments entered into the function.
And for example we get the following string "<uniqueValue*>user:maj0r pass:123 type:create-module".
At the end we again add <uniqueValue*> and get the following string "<uniqueValue*>user:maj0r pass:123 type:create-module<uniqueValue*>".
Now we translate all this into md5 hash and translate it into hex value.
