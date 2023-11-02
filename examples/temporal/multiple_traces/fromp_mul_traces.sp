var {
    int p1;
    Trace tr1;
    int p2;
    Trace tr2;
}

relation {
    prog(p1, tr1);
    prog(p2, tr2);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | compare(p1, ??(3)) | compare(p2, ??(3)) | compare(p1, p2);
    boolean RHS -> Now(PT);
    BoolArray PT -> Eventually(PNT) | Globally(PNT) | Until(PNT, PNT);
    BoolArray PNT -> eqx(tr1, ??(1)) | eqx(tr2, ??(1));
}


example {
    int -> ??(3);
    boolean -> ??;
    Trace -> randomTrace();
}

struct BoolArray{
    boolean[8] elements;
}

struct Event{
    boolean x;
}

struct Trace{
    Event[8] events;
}

generator void randomTrace(ref Trace tr){
    tr = new Trace();
    tr.events[0] = new Event(x = ??(1));
    tr.events[1] = new Event(x = ??(1));
    tr.events[2] = new Event(x = ??(1));
    tr.events[3] = new Event(x = ??(1));
    tr.events[4] = new Event(x = ??(1));
    tr.events[5] = new Event(x = ??(1));
    tr.events[6] = new Event(x = ??(1));
    tr.events[7] = new Event(x = ??(1));
}

void Eventually(BoolArray seq, ref BoolArray ret) {
    boolean[8] elements;
    elements[7] = seq.elements[7];
    for(int i=6;i>=0;i--) {
        elements[i] = elements[i+1] || seq.elements[i];
    }
    ret = new BoolArray(elements = elements);
}

void Globally(BoolArray seq, ref BoolArray ret) {
    boolean[8] elements;
    elements[7] = seq.elements[7];
    for(int i=6;i>=0;i--) {
        elements[i] = elements[i+1] && seq.elements[i];
    }
    ret = new BoolArray(elements = elements);
}

void Until(BoolArray seq1, BoolArray seq2, ref BoolArray ret) {
    boolean[8] elements;
    int last = -1;
    for(int i = 0; i < 8; i++)
        if(seq2.elements[i] == 1)
        {
            boolean hold1 = 1; 
            elements[i] = 1;
            for(int j = i - 1; j > last; j--)
            {
                hold1 = hold1 && seq1.elements[j];
                elements[j] = hold1;
            }
            last = i;
        }
    
    for(int j = 7; j > last; j--)
        elements[j] = 0;
    ret = new BoolArray(elements = elements);
}

void Now(BoolArray seq, ref boolean ret)
{
    ret = seq.elements[0];
}

// void map(fun f, Trace tr, ref BoolArray ret) {
//     boolean[8] elements;
//   for(int i=0;i<8;i++) 
//        elements[i] = f(tr.events[i].x);   
//    ret = new BoolArray(elements = elements);    
// }

void eqx(Trace tr, int x, ref BoolArray ret) {
    boolean[8] elements;
    for(int i=0;i<8;i++) 
        elements[i] = (tr.events[i].x == x);   
    ret = new BoolArray(elements = elements);    
}


void prog(int p, ref Trace tr) {
    for(int i=0;i<p;i++)
        tr.events[i].x = 0;
    tr.events[p].x = 1;
    for(int i=p+1;i<8;i++)
        tr.events[i].x = 1;// not truly non-deterministic
}