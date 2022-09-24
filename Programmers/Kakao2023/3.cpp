#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    long long answer = 0;

    for (int i = n - 1; i >= 0; i--)
    {
        if (deliveries[i] == 0 && pickups[i] == 0)
            continue;

        answer += i + i + 2;

        int pickCap = 0;
        int delCap = 0;

        for (int j = i; j >= 0; j--)
        {
            pickCap += pickups[j];
            if (pickCap > cap)
            {
                pickups[j] = pickCap - cap;
                break;
            }
            pickups[j] = 0;
        }

        for (int j = i; j >= 0; j--)
        {
            delCap += deliveries[j];
            if (delCap > cap)
            {
                deliveries[j] = delCap - cap;
                break;
            }
            deliveries[j] = 0;
        }

        if (pickups[i] > 0 || deliveries[i] > 0)
            i++;
    }
    return answer;
}
