#include <vector>
#include <map>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int visit[100][100];
int M, N;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
void init(int m, int n)
{
    M = m;
    N = n;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            visit[i][j] = 0;
}

int search(int i, int j, vector<vector<int>>& picture)
{
    if (visit[i][j])
    {
        return 0;
    }
    if (picture[i][j] == 0)
    {
        visit[i][j] = 1;
        return 0;
    }

    visit[i][j] = 1;

    int sum = 1;
    for (int idx = 0; idx < 4; idx++)
    {
        int newi = i + dx[idx];
        int newj = j + dy[idx];

        if (newi >= M || newi < 0 || newj >= N || newj < 0)
            continue;
        if (picture[i][j] == picture[newi][newj])
        {
            sum += search(newi, newj, picture);
        }
    }

    return sum;
}

vector<int> solution(int m, int n, vector<vector<int>> picture)
{

    init(m, n);
    int number_of_area = 0;
    int max_size_of_one_area = 0;

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
        {
            int ret = search(i, j, picture);
            if (ret != 0)
            {
                number_of_area++;
                if (ret > max_size_of_one_area)
                    max_size_of_one_area = ret;
            }
        }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;

    return answer;
}
