1class Solution {
2public:
3    char nextGreatestLetter(vector<char>& letters, char target) {
4        int i = 0, e = letters.size() - 1;
5        char ans = letters[0];  // default to first element for wrap-around
6
7        while (i <= e) {
8            int mid = i + (e - i) / 2;
9            if (letters[mid] > target) {
10                ans = letters[mid];
11                e = mid - 1;
12            } else {
13                i = mid + 1;
14            }
15        }
16
17        return ans;
18        }
19};