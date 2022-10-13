#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int nums;
    cin >> nums;
    int minRemoveal = nums;
    int removeal, height, j;
    vector<int>heights;
    for(int i=0;i<nums;i++)
    {
        cin >> height;
        heights.push_back(height);
    }
    vector<int>left(nums);
    vector<int>right(nums);

    for(int i=0;i<nums;i++)
    {
        j = nums-i-1;
        left[i] = 1;
        for(int ii=0;ii<i;ii++)
        {
            if(heights[i]>heights[ii])
            {
                left[i]= max(left[i], left[ii]+1);
            }
        }
        right[j] = 1;
        for(int jj=nums-1;jj>j;jj--)
        {
           if(heights[j]>heights[jj])
           {
               right[j] = max(right[j], right[jj]+1);
           }
        }

    }
    for(int i=0;i<nums;i++)
    {
        removeal = nums-(left[i]+right[i]-1);
        minRemoveal = min(removeal, minRemoveal);
    }
    cout<<minRemoveal;
    return 0;
}
