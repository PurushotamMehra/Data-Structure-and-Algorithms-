#include <vector>
#include <iostream>
#include <algorithm>

double findMaxAverage(std::vector<int>& nums, int k) {
    double sum = 0;
    for(int i = 0; i < k; i++)
        sum += nums[i];
    double ans = sum;

    for(int i = k; i < nums.size(); i++) {
        sum += nums[i] - nums[i - k];
        ans = std::max(ans, sum);
    }

    return ans / k;
}

int main() {
    std::vector<int> nums = {1,12,-5,-6,50,3};
    int k = 4;
    std::cout << findMaxAverage(nums, k) << std::endl;
    return 0;
}