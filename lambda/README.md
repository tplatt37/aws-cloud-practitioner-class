# Simple Lambda Function

This is a simple Lambda function that downloads any text file from the internet and counts the number of words, lines, characters, etc.

# To create

1. Create a Lambda function "From scratch"
2. Choose Python 3.13 (or newer version)
3. Paste this code into the lambda_function.py file, replacing all existing code
4. Click "Deploy"


# To run

Go to the "Test" settings and create a Test event with this JSON:
```
{"url":"https://some/path/to/text.txt"}
```

NOTE: You must replace the URL (https://) with some valid text file availalbe on the Internet.