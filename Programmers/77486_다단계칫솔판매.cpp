#include <string>
#include <vector>
#include <string>
#include <vector>
#include <map>

using namespace std;

class Person
{
    Person* parent;
    int money;
public:
    Person(Person* parent) : parent(parent)
    {
        money = 0;
    }
    int GetMoney() { return money; }
    void DistributeMoney(int profitMoney)
    {
        if (parent == NULL)
        {
            money += profitMoney;
            return;
        }

        int parenProfit = profitMoney * 0.1;
        int myProfit = profitMoney - parenProfit;
        money += myProfit;
        if (parenProfit > 0 && parent != NULL)
        {
            parent->DistributeMoney(parenProfit);
        } 
    }
};

map<string, Person*> personMap;

void makeTree(vector<string> enroll, vector<string> referral)
{
    personMap["-"] = new Person(NULL);
    for (int i=0;i<enroll.size();i++)
        personMap[enroll[i]] = new Person(personMap[referral[i]]);
}

void calMoney(vector<string> seller, vector<int> amount)
{
    for (int i = 0; i < seller.size(); i++)
        personMap[seller[i]]->DistributeMoney(amount[i]*100);
}

vector<int> getResult(vector<string> enroll)
{
    vector<int> result;
    for (int i = 0; i < enroll.size(); i++)
        result.push_back(personMap[enroll[i]]->GetMoney());
    return result;
}

void deleteTree()
{
    map<string, Person*>::iterator iter;
    for (iter = personMap.begin(); iter != personMap.end(); iter++)
    {
        delete iter->second;
    }
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    makeTree(enroll, referral);
    calMoney(seller, amount);
    vector<int> answer = getResult(enroll);
    deleteTree();
    return answer;
}

int main()
{
    vector<string> enroll = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
    vector<string> referral = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
    vector<string> seller = {"young", "john", "tod", "emily", "mary"};
    vector<int> amount = {12, 4, 2, 5, 10};
    vector<int> result = solution(enroll, referral, seller, amount);
    return 0;
}