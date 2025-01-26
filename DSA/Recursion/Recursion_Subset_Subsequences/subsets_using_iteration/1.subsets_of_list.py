def subsets(nums):
    # [] 1
    # [] 1, 2, 12
    # [] 1, 2, 12, 3, 13, 23, 123
    res = [[]]
    for num in nums:
        res = res + [item + [num] for item in res]
    return res
nums=[1, 2, 3]
print(subsets(nums))

# this is cpp code for the same  
#include <iostream>
#include <vector>
# std::vector<std::vector<int>> subsets(const std::vector<int>& nums) {
#     std::vector<std::vector<int>> res = {{}};
#     for (int num : nums) {
#         int n = res.size();
#         for (int i = 0; i < n; ++i) {
#             std::vector<int> subset = res[i];
#             subset.push_back(num);
#             res.push_back(subset);
#         }
#     }
#     return res;
# }

# int main() {
#     std::vector<int> nums = {1, 2, 3};
#     std::vector<std::vector<int>> result = subsets(nums);

#     std::cout << "Subsets:" << std::endl;
#     for (const auto& subset : result) {
#         std::cout << "[";
#         for (size_t i = 0; i < subset.size(); ++i) {
#             std::cout << subset[i];
#             if (i < subset.size() - 1) {
#                 std::cout << ", ";
#             }
#         }
#         std::cout << "]" << std::endl;
#     }

#     return 0;
# }