class Node{
    int key;
    int val;
    Node next;
    Node(int key, int val){
        this.key=key;
        this.val=val;
        this.next=null;
    }
}
class MyHashMap {
    private Node map[];
    public MyHashMap() {
        map = new Node[100];
        for(int i=0;i< 100; i++){
            map[i] = new Node(-1,-1);
        }
    }    
    public void put(int key, int value) {
        int hash = hash(key);
        Node current = map[hash];
        while(current.next!=null){
            if(current.next.key == key){
                current.next.val=value;
                return;
            }
            current=current.next;
        }
        current.next = new Node(key,value);
    }
    
    public int get(int key) {
        int hash = hash(key);
        Node current = map[hash].next;
        while(current!=null){
            if(current.key == key)
                return current.val;
            current = current.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int hash = hash(key);
        Node current = map[hash];
        while(current.next!=null){
            if(current.next.key ==  key){
                current.next = current.next.next;
                return;
            }
            current=current.next;
        }
    }
    public int hash(int key){
        return key%100;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
