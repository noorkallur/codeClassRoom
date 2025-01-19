# using recursion skip the letter a from the string and print the restt of the string
def skipAcharacter(str):
    if len(str) == 0:
        return ""
    if str[0] == 'a':
        return skipAcharacter(str[1:])
    else:
        return str[0] +  skipAcharacter(str[1:])
    
str = "abbaccda"
print(skipAcharacter(str))
        
        
# // C++ code for the same 
# #include <iostream>

# void charAremoval(char* str, char* res, int& index)
# {
#     if(*str == '\0'){
#         res[index] = '\0';
#         return;
#     }
#     if(*str == 'a')
#     {
#         charAremoval(str+ 1, res, index);
#     }
#     else{
#         res[index] = *str;
#         index++;
#         charAremoval(str+ 1, res, index);
#     }
# }

# int main() {
#     // Write C++ code here
#     char arr[] = "abccad";
#     char res[] =  "";
#     int index = 0;
#     charAremoval(arr, res, index);
#     std::cout<< res<<std::endl;
#     return 0;
# }