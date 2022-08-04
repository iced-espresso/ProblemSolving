import java.lang.reflect.Array;
import java.util.*;

public class LeetCode_729_MyCalendar {
    public static void main(String args[]){
        MyCalendar myCalendar = new MyCalendar();
        System.out.println(myCalendar.book(10, 20)); // return True
        System.out.println(myCalendar.book(15, 25)); // return False, It can not be booked because time 15 is already booked by another event.
        System.out.println(myCalendar.book(20, 30)); // return True, The event can be booked, as the first event takes every time less than 20, but

    }
}

class MyCalendar {
    private List<int[]> list;
    public MyCalendar() {
        list = new ArrayList<>();
    }

    public boolean book(int start, int end) {
        for(int[] node:list){
            if(start < node[1] && end > node[0])
                return false;
        }

        list.add(new int[]{start,end});
        return true;
    }
}
