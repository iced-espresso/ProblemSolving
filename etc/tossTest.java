import java.util.*;

class tossTest{
    static public void main(String args[]){
        new Solution().solution(2, true, new int[]{1,1,2,2});
    }
}


class RoundRonbiner{
    private int n;
    private int maxN;

    public RoundRonbiner(int maxN){
        n = 1;
        this.maxN = maxN;
    }

    public int getNext(){
        int temp = n;
        n = (n==maxN) ? 1 : n+1;
        return temp;
    }
}

interface RoadBalancer{
    public int getServer(int req);
}

class StickyRoadBalancer implements RoadBalancer{
    private RoundRonbiner roundRonbinerServer;
    private HashMap<Integer, Integer> reqToServer;
    public StickyRoadBalancer(int servers){
        reqToServer = new HashMap<>();
        roundRonbinerServer = new RoundRonbiner(servers);
    }

    @Override
    public int getServer(int req){
        if (!reqToServer.containsKey(req)){
            reqToServer.put(req, roundRonbinerServer.getNext());
        }

        return reqToServer.get(req);
    }
}

class NonStickyRoadBalancer implements RoadBalancer{
    RoundRonbiner roundRonbinerServer;

    public NonStickyRoadBalancer(int servers){
        roundRonbinerServer = new RoundRonbiner(servers);
    }

    public int getServer(int req){
        return roundRonbinerServer.getNext();
    }
}

class Solution {


    public int[][] solution(int servers, boolean sticky, int[] requests) {

        ArrayList[] list = new ArrayList[servers];

        for(int i=0;i<servers;i++)
            list[i] = new ArrayList();

        RoadBalancer roadBalancer;
        if(sticky)
            roadBalancer = new StickyRoadBalancer(servers);
        else
            roadBalancer = new NonStickyRoadBalancer(servers);

        StickyRoadBalancer stickyRoadBalancer;

        for(int req:requests){
            int server = roadBalancer.getServer(req);
            list[server-1].add(req);
        }

        int[][] answer = new int[servers][];
        for(int i=0;i<servers;i++)
            answer[i] = list[i].stream().mapToInt(x->(int)x).toArray();

        return answer;
    }
}