# using recursion skip a substring from the string and print the rest of the string
def skipSubstring(str, subStr):
    if len(str) == 0:
        return ""
    if str[0:len(subStr)] == subStr:
        return skipSubstring(str[len(subStr):], subStr)
    else:
        return str[0] +  skipSubstring(str[1:],subStr)
    
str = "abbappleccda"
print(skipSubstring(str, "apple"))

#  // C++ code for the same 
# #include <iostream>
# #include <cstring>
# void charAremoval(char* str, char* res, int& index)
# {
#     if(*str == '\0'){
#         res[index] = '\0';
#         return;
#     }
#     if(strncmp(str, "apple", 5) == 0)
#     {
#         charAremoval(str+ 5, res, index);
#     }
#     else{
#         res[index] = *str;
#         index++;
#         charAremoval(str+ 1, res, index);
#     }
# }

# int main() {
#     // Write C++ code here
#     char arr[] = "abcapplecad";
#     char res[] =  "";
#     int index = 0;
#     charAremoval(arr, res, index);
#     std::cout<< res<<std::endl;
#     return 0;
# }