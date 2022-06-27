#include <string>
#include <vector>
#include <queue>

using namespace std;
const int MAXR = 5;
const int MAXC = 5;
class Point
{
public:
    int r;
    int c;
    int dis;
    Point(int r, int c, int dis) : r(r), c(c), dis(dis)
    {

    }
};


int visit[MAXR][MAXC];

void initVisit()
{
    for (int r = 0; r < MAXR; r++)
        for (int c = 0; c < MAXC; c++)
            visit[r][c] = 0;
}

bool checkClosePerson(vector<string>& room, int r, int c)
{
    initVisit();
    const int dr[] = { -1,1,0,0 };
    const int dc[] = { 0,0,-1,1 };
    queue<Point> q;
    q.push(Point(r, c, 0));

    while (!q.empty())
    {
        Point temp = q.front();
        q.pop();

        visit[temp.r][temp.c] = 1;

        for (int i = 0; i < 4; i++)
        {
            int newr = temp.r + dr[i];
            int newc = temp.c + dc[i];
            int newDis = temp.dis + 1;

            if (newr < 0 || newr >= MAXR || newc < 0 || newc >= MAXC)
                continue;

            if (visit[newr][newc] == 1) continue;
            if (newDis > 2) continue;
            if (room[newr][newc] == 'P')
                return true;

            if (room[newr][newc] == 'O' )
                q.push(Point(newr, newc, newDis));


        }

    }
    return false;
}


int getSolutionByRoom(vector<string>& room)
{
    for (int r = 0; r < MAXR; r++)
    {
        for (int c = 0; c < MAXC; c++)
        {
            if (room[r][c] == 'P' && checkClosePerson(room, r, c))
            {
                return 0;
            }
        }
    }
    return 1;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    for (auto room : places)
    {
        answer.push_back(getSolutionByRoom(room));
    }
    return answer;
}


vector<vector<string>> input = { {"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"}, {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"} };


int main()
{
    solution(input);
    return 0;
}