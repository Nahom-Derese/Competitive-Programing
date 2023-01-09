package MultiThreading;

import MultiThreading.main.Balance;

public class Task1 implements Runnable {
    Balance balance;

    Task1(Balance t){
        balance = t;
    }

    public synchronized void run(){

        synchronized(t2){
            t2.wait();
            System.out.println("Your Balance is : -" + balance.b);
        }
    }
}

