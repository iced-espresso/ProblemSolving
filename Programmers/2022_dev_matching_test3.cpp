#include <string>
#include <vector>
#include <queue> 
using namespace std;

const int MAXN = 102;
int map[MAXN][MAXN];
int visit[MAXN][MAXN];
int sizeVisit[MAXN][MAXN];

struct Point
{
    int r;
    int c;
};

int N,M;

// map : 1->¹Ù´Ù, 0->¹°, 2->À°Áö
void flood()
{
    queue<Point> q;

    q.push(Point{ 1, 1 });

    int dr[] = { -1,1,0,0 };
    int dc[] = { 0,0,-1,1 };

    while (!q.empty())
    {
        Point curr = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int newr = curr.r + dr[i];
            int newc = curr.c + dc[i];

            if (newr > N || newr < 1 || newc > M || newc < 1)
                continue;

            if (visit[newr][newc]) continue;

            if (map[newr][newc] != 2)
            {
                map[newr][newc] = 1;
                visit[newr][newc] = 1;
                q.push(Point{ newr,newc });
            }
            
        }

    }

}


void init(vector<vector<int>> lands)
{
    for (int i = 1; i <= N; i++)
    {
        map[i][1] = 1;
    }
    for (int i = 1; i <= N; i++)
    {
        map[i][M] = 1;
    }

    for (int i = 1; i <= M; i++)
    {
        map[1][i] = 1;
    }
    for (int i = 1; i <= M; i++)
    {
        map[N][i] = 1;
    }

    for (int i = 0; i < lands.size(); i++)
    {
        map[lands[i][0]][lands[i][1]] = 2;
    }
}

int getSize(int r, int c)
{
    queue<Point> q;

    q.push(Point{ r, c });
    sizeVisit[r][c] = 1;

    int dr[] = { -1,1,0,0 };
    int dc[] = { 0,0,-1,1 };

    int size = 0;
    while (!q.empty())
    {
        Point curr = q.front();
        q.pop();
        size++;

        for (int i = 0; i < 4; i++)
        {
            int newr = curr.r + dr[i];
            int newc = curr.c + dc[i];

            if (newr > N || newr < 1 || newc > M || newc < 1)
                continue;

            if (sizeVisit[newr][newc]) continue;

            if (map[newr][newc] != 2)
            {
                map[newr][newc] = 1;
                sizeVisit[newr][newc] = 1;
                q.push(Point{ newr,newc });
            }

        }

    }
    return size;
}


vector<int> solution(int rows, int columns, vector<vector<int>> lands) {
    vector<int> answer;
    N = rows;
    M = columns;

    init(lands);
    flood();

    int maxSize = -1;
    int minSize = -1;
    for(int r=1;r<=N;r++)
        for (int c = 1; c <= M; c++)
        {
            if (!sizeVisit[r][c] && map[r][c] == 0)
            {
                int size = getSize(r, c);
                if (size > maxSize)
                    maxSize = size;

                if (minSize == -1)
                    minSize = size;

                if (size < minSize)
                    minSize = size;
            }
        }
    answer.push_back(minSize);
    answer.push_back(maxSize);
    return answer;
}

int main()
{
    solution(5, 7, { {2, 5}, {3, 3}, {3, 4}, {3, 5}, {4, 3} });

}