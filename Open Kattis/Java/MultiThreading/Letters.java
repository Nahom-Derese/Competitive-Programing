public class Letters extends Thread {
    private String name;
    public static Object lock = new Object();

    public Letters(String name) {
        this.name = name;
    }

    synchronized public void write() {
        
        for (int i = 0; i < 1000; i++) {
            System.out.print(name);
    }
    }

    public void run(){
        synchronized(lock){
        write();
        }
    }

    public static void main(String[] args) {
        new Letters("X").start();
        new Letters("Y").start();
    }

}
