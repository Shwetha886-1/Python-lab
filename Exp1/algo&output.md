Experiment-01 

Data type and operators 



**ALGORITHM - Verification of Algebraic and Bitwise Identities**



STEP1: Start the program.



STEP2: Initialize variables



Assign values:

a = 208

b = 600



STEP3: Display heading



Print the message "In Equation assignment operator".



STEP4: Verify algebraic identities



Print the Boolean result (True or False) for each identity.



STEP5: Display heading



Print "In bitwise operation".



STEP6: Verify bitwise identities



Check whether a | b = (a ^ b) + (a \& b).



Check whether a ^ (a \& b) = (a | b) ^ b.



Check whether b ^ (a \& b) = (a | b) ^ a.



Check whether (a \& b) ^ (a | b) = a ^ b.



STEP7: Check additional bitwise relations



Verify (a+b) = (a|b) + (a\&b).



Verify a+b = (a^b) + 2\*(a\&b).



STEP8: Display heading



Print "In Subtraction".



STEP9: Verify subtraction identities



Check a-b = (a^(a\&b)) - ((a|b)^a).



Check a-b = ((a|b)^b) - ((a|b)^a).



Check a-b = (a^(a\&b)) - (b^(a\&b)).



Check a-b = ((a|b)^b) - (b^(a\&b)).



STEP10: Print results



Display the Boolean results of all comparisons.



STEP11: Stop the program.



***OUTPUT:***

True

True

True

True

True



In bitwise operation

True

True

True

True



True

True



In Subtraction

True

True

True

True

