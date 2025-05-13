Challenge 1 
Use  the  Variable  Explorer,  observe  the  difference  between  basic  Python  operator  (+)  and 
OpenCV function (cv2.add). What is the main difference between the two? 
 
 
When  the  basic  Python  operator  is  used,  the  final  output  is  analogous  to applying  a  modulo 
function after addition. For example, 160 + 100 will result in a final output of 4 (260 modulo 
256). This is different from the OpenCV function, where the pixel values are capped at 255.  
 
It  is  important  to  note that  the  values  are  limited by  the  data  type  (uint8).  In  this  case,  the 
values can only range from 0-255, and the basic Python operators and the OpenCV functions 
will have to work around this. Which method to use is really depends on the type of output you 
are looking for.  
 
However,  it  is  not  always  feasible  to  deal  with  such  a  small  range.  Most  of  the  time,  it  is 
necessary  to  have  an  array  that  could  store  values  much  larger  than  255.  The  purpose  is  to 
ensure that the values  will not be  altered or truncated during the processing. To resolve this 
issue,  we  can  either  change  the  data  type  of  an  existing  array  or  specify  the  data  type  when 
creating a new array. 
 
But if the values are beyond the range of 0-255 after the processing, we might have a problem 
in  showing  the  output,  because  normally  a  proper  image  (for  display  purpose)  should  only 
have values range from 0-255. Therefore, we will have to scale the values back to the range of 
0-255 when it is necessary to display the output.  
 
An  example  that  demonstrates  how  to  perform scaling after adding “cameraman.bmp”  to 
“boat.bmp” is shown below. 


**Answer:**

*   **Python `+` operator (with NumPy arrays):** Performs **modulo arithmetic**.
    *   For `uint8` data, this means the result of an operation like `value1 + value2` is effectively `(value1 + value2) % 256`.
*   **OpenCV `cv2.add()` function:** Performs **saturation arithmetic**.
    *   For `uint8` data, results are clipped to the range [0, 255].
        *   If `value1 + value2 > 255`, the result is `255`.
        *   If `value1 + value2 < 0` (though less common with addition of positive pixel values), the result would be `0`.