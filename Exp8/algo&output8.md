Experiment- 08

**Algorithm**



**1. re.match()**

**Algorithm:**



Step 1: Start

Step 2: Import re module

Step 3: Store a sentence in variable text

Step 4: Use re.match("python", text) to check match at the beginning

Step 5: If match is found → go to Step 6

Step 6: Print "Python"

Step 7: Else → go to Step 8

Step 8: Print "No match"

Step 9: End



&#x20;**2. re.search()**

**Algorithm:**



Step 1: Start

Step 2: Import re module

Step 3: Store sentence in text

Step 4: Use re.search("hot", text) to find word anywhere

Step 5: If found → go to Step 6

Step 6: Print "Yes, it's hot"

Step 7: Else → go to Step 8

Step 8: Print "Not found"

Step 9: End



&#x20;**3. re.findall()**

**Algorithm:**



Step 1: Start

Step 2: Import re module

Step 3: Store text containing numbers

Step 4: Use re.findall(r"\\d+", text) to extract numbers

Step 5: Store result in numbers list

Step 6: Print all numbers

Step 7: End





&#x20;**4. re.finditer()**

**Algorithm:**



Step 1: Start

Step 2: Import re module

Step 3: Store text with repeated words

Step 4: Use re.finditer("apple", text)

Step 5: Loop through each match

Step 6: For each match:

  - Print matched word using match.group()

  - Print starting position using match.start()

  - Print ending position using match.end()

Step 7: End loop

Step 8: End





&#x20;**5. re.split()**

**Algorithm:**



Step 1: Start

Step 2: Import re module

Step 3: Store text with multiple separators

Step 4: Use re.split("\[,;|]", text) to split

Step 5: Store result in languages list

Step 6: Print list of languages

Step 7: End





&#x20;**6. re.sub()**

**Algorithm:**



Step 1: Start

Step 2: Import re module

Step 3: Store text with phone number

Step 4: Use re.sub(r"\\d", "x", text)

Step 5: Replace all digits with "x"

Step 6: Store result in hidden

Step 7: Print modified text

Step 8: End



**OUTPUT**

**PS C:\\Users\\shwet\\python lab> \& C:\\Users\\shwet\\AppData\\Local\\Programs\\Python\\Python314\\python.exe "c:/Users/shwet/python lab/Exp8/Experiment-8.py"**

**No match**

**Yes, it's hot**

**All numbers: \['85', '90', '78', '92']**

**Found: apple**

**Start: 0 End: 5**

**Found: apple**

**Start: 13 End: 18**

**Languages: \['python', ' Java', ' c++ ', ' Javascript']**

**My phone number is xxxxxxxxxx**

