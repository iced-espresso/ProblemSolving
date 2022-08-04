import java.util.Arrays;

public class Programmers67256 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] numbers = {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2};
        sol.solution(numbers, "left");

    }
}

enum HandType {
    LEFT, RIGHT
}

class Hand {
    class Position {
        int r, c;

        public Position(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public int getDistnace(Position pos) {
            return Math.abs(pos.r - this.r) + Math.abs(pos.c - this.c);
        }
    }

    Position pos;
    HandType handType;
    private static final int[] leftNumbers = {1, 4, 7};
    private static final int[] rightNumbers = {3, 6, 9};
    private int[] myRegionNumbers;

    private Position numToPos(int num) {
        if (num == 0) {
            num = 11;
        }
        return new Position((num - 1) / 3, (num - 1) % 3);
    }

    public Hand(HandType handType) {
        this.handType = handType;
        if (handType == HandType.LEFT) {
            pos = new Position(3, 0);
            myRegionNumbers = leftNumbers;
        } else if (handType == HandType.RIGHT) {
            pos = new Position(3, 2);
            myRegionNumbers = rightNumbers;
        }
    }

    @Override
    public String toString() {
        if (handType == HandType.LEFT) {
            return "L";
        } else {
            return "R";
        }
    }

    public void moveTo(int number) {
        this.pos = numToPos(number);
    }

    public boolean isMyRegion(int num) {
        return Arrays.stream(myRegionNumbers).anyMatch(x -> x == num);
    }

    public int getDistance(int num) {
        Position pos = numToPos(num);
        return pos.getDistnace(this.pos);
    }
}

class User {
    Hand leftHand = new Hand(HandType.LEFT);
    Hand rightHand = new Hand(HandType.RIGHT);
    Hand priorityHand;

    private Hand findCloseHand(int number) {
        int leftDistance = leftHand.getDistance(number);
        int rightDistance = rightHand.getDistance(number);
        Hand hand;
        if (leftDistance < rightDistance) {
            hand = leftHand;
        } else if (leftDistance > rightDistance) {
            hand = rightHand;
        } else {
            hand = priorityHand;
        }
        return hand;
    }

    private Hand getMoverHand(int number) {
        if (leftHand.isMyRegion(number)) {
            return leftHand;
        } else if (rightHand.isMyRegion(number)) {
            return rightHand;
        } else {
            return findCloseHand(number);
        }
    }

    public User(String hand) {
        priorityHand = hand.equals("left") ? leftHand : rightHand;
    }

    public String moveTo(int number) {
        Hand moverHand = getMoverHand(number);
        moverHand.moveTo(number);
        return moverHand.toString();
    }
}

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        User user = new User(hand);
        for (int number : numbers) {
            answer += user.moveTo(number);
        }
        return answer;
    }
}