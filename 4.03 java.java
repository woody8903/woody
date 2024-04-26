class Connetion {
    private static Connection _inst = null;
    private int count = 0;
    public static Connetion get () {
        if(_inst == null) {
            _inst == null) {
                _inst = new Connection();
                return _inst;
            }
            return _inst;
        }
        public void count() { count ++; }
        public int getCount() {return count; }
    }

    public class Test {
        public static void main(String[] args) {
            Connection connl = Connection.get();
            connl.count();
            Connection conm2 = Connection.get();
            conn2.count();
            connection conn3 = Connection.get();
            conn3count();
            System.out(print(connnl, getgount))
        }
    }
}