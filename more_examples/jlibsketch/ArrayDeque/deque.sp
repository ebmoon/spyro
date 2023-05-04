struct DequeNode {
    int val;
    DequeNode prev;
    DequeNode next;
}

struct ArrayDeque {
    DequeNode head;
    DequeNode tail;
    int size;
}

void size(ArrayDeque q, ref int ret) {
    ret = q.size;
}

void isEmpty(ArrayDeque q, ref boolean ret) {
    ret = (q.size == 0);
}

void copy(ArrayDeque q, ref ArrayDeque ret) {
    ret = new ArrayDeque(head=null, tail=null, size=q.size);

    DequeNode prev = null;
    DequeNode curr = q.head;
    while(curr != null) {
        DequeNode n = new DequeNode(val=curr.val, prev=prev, next=null);
        if (prev != null) {
            prev.next = n;
        }
        curr = curr.next;
        prev = n;
    }

    ret.tail = prev;
}

void add(ArrayDeque q, int e, ref ArrayDeque ret) {
    copy(q, ret);   // To make each Deque immutable
    
    DequeNode n = new DequeNode(val=e, prev=null, next=null);
    
    if (q.size == 0) {
        ret.head = n;
    } else {
        n.prev = q.tail;
        ret.tail.next = n;
    }

    ret.tail = n;
    ret.size = q.size + 1;
}

void remove(ArrayDeque q, ref boolean err, ref ArrayDeque ret) {
    copy(q, ret);   // To make each Deque immutable

    DequeNode head = ret.head;
    if (head != null) {
        DequeNode next = head.next;
        if (next != null) {
            next.prev = null;
        }
        head = next;
        if (ret.size == 1) {
            ret.tail = null;
        }
        ret.size = ret.size - 1;
        err = false;
    } else {
        err = true;
    }
}

void peek(ArrayDeque q, ref boolean err, ref int ret) {
    if (q.size == 0) {
        err = true;
        ret = -1;
    } else {
        err = false;
        ret = q.head.val;
    }
}

void peekLast(ArrayDeque q, ref boolean err, ref int ret) {
    if (q.size == 0) {
        err = true;
        ret = -1;
    } else {
        err = false;
        ret = q.tail.val;
    }
}