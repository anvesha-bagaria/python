abv'''
Created on 29-Sep-2017

@author: anvesha
'''

======================

We have had requests for a method to process the results of sending emails 
through PHPMailer. In this new release, we have implemented a callback
function that passes the results of each email sent (to, cc, and/or bcc). 
We have provided an example that echos the results back to the screen. The
callback function can be used for any purpose. With minor modifications, the
callback function can be used to create CSV logs, post results to databases,
etc.

Please review the test.php script for the example.

It's pretty straight forward.

Enjoy!
Andy
