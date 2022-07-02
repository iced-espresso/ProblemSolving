#include <string>
#include <vector>

using namespace std;

enum UNIT
{
    EMPTY_SPACE = -1,
    SHEEP = 0,
    WOLF = 1,
};

class Node
{
public:
    Node* left = NULL;
    Node* right = NULL;
    Node* parent = NULL;
    UNIT unit;
    void AddChild(Node* child)
    {
        if (left == NULL)
            left = child;
        else if (right == NULL)
            right = child;
    }
    void SetParent(Node* p)
    {
        this->parent = p;
    }
};

void dfs(Node* curr, Node* prev, int sheepNum, int wolfNum);
Node node[18];
int maxSheep = 0;

void dfsChild(Node* curr, Node* prev, int sheepNum, int wolfNum)
{
    if (curr->left != NULL && curr->left != prev)
        dfs(curr->left, curr, sheepNum, wolfNum);

    if (curr->right != NULL && curr->right != prev)
        dfs(curr->right, curr, sheepNum, wolfNum);
}

void dfs(Node* curr, Node* prev, int sheepNum, int wolfNum)
{
    UNIT tempCh = curr->unit;
    curr->unit = EMPTY_SPACE;

    if(tempCh == WOLF)
    {
        wolfNum++; 
        if (wolfNum >= sheepNum)
        {
            curr->unit = tempCh;
            return;
        }
    }
    else if (tempCh == SHEEP)
    {
        sheepNum++;
        if (sheepNum > maxSheep) maxSheep = sheepNum;

        if (curr->parent != NULL)
            dfs(curr->parent, curr, sheepNum, wolfNum);
    }
    else if (tempCh == EMPTY_SPACE)
    {
        if (curr->parent != NULL && curr->parent != prev)
            dfs(curr->parent, curr, sheepNum, wolfNum);

    }

    if (curr->left != NULL && curr->left != prev)
        dfs(curr->left, curr, sheepNum, wolfNum);

    if (curr->right != NULL && curr->right != prev)
        dfs(curr->right, curr, sheepNum, wolfNum);
    curr->unit = tempCh;

}

void init(vector<int> info, vector<vector<int>> edges)
{
    maxSheep = 0;
    for (int i = 0; i < info.size(); i++)
    {
        node[i].unit = (UNIT)info[i];
    }

    for (int i = 0; i < edges.size(); i++)
    {
        Node* parent = &node[edges[i][0]];
        Node* child = &node[edges[i][1]];
        parent->AddChild(child);
        child->SetParent(parent);
    }
}

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer = 0;
    init(info, edges);
    dfs(&node[0], NULL, 0, 0);
    return maxSheep;
}

int main()
{
    solution({0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1}, {{0, 1}, {1, 2}, {1, 4}, {0, 8}, {8, 7}, {9, 10}, {9, 11}, {4, 3}, {6, 5}, {4, 6}, {8, 9}} );
    solution({ 0,1,0,1,1,0,1,0,0,1,0 }, { {0,1},{0,2},{1,3},{1,4},{2,5},{2,6},{3,7},{4,8},{6,9},{9,10} });
}