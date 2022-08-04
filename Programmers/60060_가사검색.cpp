#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Node
{
public:
    Node* nextNode[26];
    map<int, int> lenMap;
};

Node forwardRoot;
Node reverseRoot;

void updateTrie(string word)
{
    Node* node = &forwardRoot;
    for (int i = 0; i < word.size(); i++)
    {
        int c = word[i] - 'a';
        node->lenMap[word.size()-i] += 1;
        if (node->nextNode[c] == 0)
        {
            node->nextNode[c] = new Node();
            node = node->nextNode[c];
        }
        else
        {
            node = node->nextNode[c];
;       }
    }
}
void updateReverseTrie(string word)
{
    Node* node = &reverseRoot;
    for (int i = word.size()-1; i >= 0; i--)
    {
        int c = word[i] - 'a';
        node->lenMap[i+1] += 1;
        if (node->nextNode[c] == 0)
        {
            node->nextNode[c] = new Node();
            node = node->nextNode[c];
        }
        else
        {
            node = node->nextNode[c];
        }
    }
}

Node* findEndNode(string word)
{
    Node* node = &forwardRoot;
    for (int i = 0; i < word.size(); i++)
    {
        int c = word[i] - 'a';
        if (node->nextNode[c] != 0)
            node = node->nextNode[c];
        else
            return 0;
    }
    return node;
}


Node* findReverseEndNode(string word)
{
    Node* node = &reverseRoot;
    for (int i = word.size()-1; i >= 0; i--)
    {
        int c = word[i] - 'a';
        if (node->nextNode[c] != 0)
            node = node->nextNode[c];
        else
            return 0;
    }
    return node;
}


int getCount(string query)
{
    int i = query.find('?');
    Node* node;
    if (i == 0)
    {
        i = query.rfind('?');

        node = findReverseEndNode(query.substr(i + 1, query.size()));
    }
    else
    {
        node = findEndNode(query.substr(0, i));
    }
    if (node == 0)
        return 0;

    return node->lenMap[std::count(query.begin(), query.end(), '?')];
}
vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    for (int i = 0; i < words.size(); i++)
    {
        updateTrie(words[i]);
        updateReverseTrie(words[i]);
    }

    for (int i = 0; i < queries.size(); i++)
    {
        answer.push_back(getCount(queries[i]));
    }
    return answer;
}




int main()
{
    vector<string> words = { "frodo", "front", "frost", "frozen", "frame", "kakao" };
    solution(words, { "fro??", "????o", "fr???", "fro???", "pro?" });
    return 0;
}