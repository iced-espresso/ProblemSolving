#include <string>
#include <vector>

using namespace std;
const int MAX_N = 102;
const int MAX_M = 102;
int map[MAX_M][MAX_N];
int r;
int c;

struct Point
{
    /* data */
    int x, y;
    Point(int x, int y)
    :x(x),y(y)
    {

    }
};

class Coordinator
{
private:
        int x_start, x_end, y_start, y_end;

public:
    Coordinator(int x1, int y1, int x2, int y2)
    :x_start(x1), y_start(y1), x_end(x2), y_end(y2)
    {  
    }
    Point GetPrev(int x, int y)
    {
        if(x == x_start && y > y_start) // 위쪽
            return Point(x, y-1);
        else if(y == y_end && x > x_start) // 오른쪽
            return Point(x-1,y);
        else if(x == x_end && y < y_end) // 밑쪽
            return Point(x,y+1);
        else if(y == y_start && x < x_end) // 왼쪽
            return Point(x+1,y);
        else
            return Point(0,0);
    }
};

void init(int _rows, int _cols)
{
    r = _rows;
    c = _cols;
    for(int x=1;x<=r;x++)
        for(int y=1;y<=c;y++)
        {
            map[x][y] = (x-1)*c + y;
        }
}


int rotateMap(int x1, int y1, int x2, int y2 )
{
    Coordinator myCoor(x1, y1, x2, y2);
    Point currPoint(x1,y1);
    
    int minVal = map[x1][y1];
    int tempVal = map[x1][y1];
    while (1)
    {
        Point prevPoint = myCoor.GetPrev(currPoint.x, currPoint.y);
        if(prevPoint.x == x1 && prevPoint.y == y1)
        {
            map[currPoint.x][currPoint.y] = tempVal;   
            break; 
        }
        map[currPoint.x][currPoint.y] = map[prevPoint.x][prevPoint.y];
        minVal = minVal > map[currPoint.x][currPoint.y] ? map[currPoint.x][currPoint.y] : minVal;
        currPoint = prevPoint;
    }
    return minVal;
}

vector<int> solution(int rows, int columns, vector<vector<int> > queries) {
    init(rows, columns);
    vector<int> answer;
    for(int idx=0;idx<queries.size();idx++)
    {
        int ret = rotateMap(queries[idx][0], queries[idx][1], queries[idx][2], queries[idx][3]);
        answer.push_back(ret);
    }
    return answer;
}


int main()
{
    vector<vector<int> > temp;
    vector<int> answ = solution(6,6, temp);
    return 0;
}