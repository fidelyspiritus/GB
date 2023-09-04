

public class LinkedList {
    public Node head;

    /**
    * Узел связного списка
    */
    public class Node{

        /**
        * Ссылка на следующий узел
        */
        public Node next;
        /**
        * Значение узла
        */
        public T value;

    }

    // Метод для добавления элемента в связный список
    public void addFirst(T value){
        Node node = new Node();
        node.value = value;
        if (head != null){
            node.next = head;
        }
        head = node;
    }

    // Метод для разворота связного списка
    public void reverseList() {
        Node prev = null;
        Node current = head;
        Node next = null;

        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

}
