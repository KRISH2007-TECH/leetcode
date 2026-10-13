1class Solution {
2public:
3    int romanToInt(string s) {
4        int temp=0;
5        for (int i=0;i<s.length();i++)
6        {   
7              
8               if (s[i]=='I'&& s[i+1]=='V')
9               {
10                temp+=4;
11                i++;
12               }
13               else if (s[i]=='I'&& s[i+1]=='X')
14               {
15                temp+=9;
16                i++;
17               }
18                else if(s[i]=='X' && s[i+1]=='C')
19               {
20                temp+=90;
21                i++;
22               }
23               else if (s[i]=='C' && s[i+1]=='M')
24               {
25                temp+=900;
26                i++;
27                }
28                else if (s[i]=='C' && s[i+1]=='D')
29               {
30                temp+=400;
31                i++;
32                }
33                else if (s[i]=='I')
34               {
35                temp=temp+1;
36               }
37               else if(s[i]=='X' && s[i+1]=='L')
38               {
39                temp+=40;
40                i++;
41               }
42               else if (s[i]=='V')
43               {
44                temp+=5;
45               }
46               
47              
48               else if(s[i]=='X')
49               {
50                temp+=10;
51               }
52               else if (s[i]=='L')
53               {
54                temp+=50;
55               }
56                
57               else if (s[i]=='C')
58               {
59                temp+=100;
60                }
61                else if  (s[i]=='D')
62                {
63                    temp+=500;
64                }
65                else if (s[i]=='M')
66                {
67                    temp+=1000;
68                }
69        }
70            
71
72        return temp;
73}
74};