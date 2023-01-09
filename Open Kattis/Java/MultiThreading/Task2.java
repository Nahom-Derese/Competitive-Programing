package MultiThreading;

public class Task2 implements Runnable{
    public void run(){
        for (int i = 0; i < 10; i++) {
            System.out.println("THIS IS TASK TWO......");
        }
    }
}
