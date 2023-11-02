var {
    int p;
    private BoolArray rd_bits;
    Trace tr;
}

relation {
    prog(p, rd_bits, tr);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | compare(p, ??(3));
    boolean RHS -> Now(PT);
    BoolArray PT -> Eventually(PNT) | Globally(PNT);
    BoolArray PNT -> eqx(tr, ??(1));
}


example {
    int -> ??(3);
    boolean -> ??;
    BoolArray -> randomBoolArray();
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

generator void randomBoolArray(ref BoolArray ba){
    ba = new BoolArray();
    ba.elements[0] = ??(1);
    ba.elements[1] = ??(1);
    ba.elements[2] = ??(1);
    ba.elements[3] = ??(1);
    ba.elements[4] = ??(1);
    ba.elements[5] = ??(1);
    ba.elements[6] = ??(1);
    ba.elements[7] = ??(1);
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

void Now(BoolArray seq, ref boolean ret)
{
    ret = seq.elements[0];
}

void eqx(Trace tr, int x, ref BoolArray ret) {
    boolean[8] elements;
    for(int i=0;i<8;i++) 
        elements[i] = (tr.events[i].x == x);   
    ret = new BoolArray(elements = elements);    
}


void prog(int p, BoolArray rd_bits, ref Trace tr) {
    for(int i=0;i<p;i++)
        tr.events[i].x = 0;
    tr.events[p].x = 1;
    for(int i=p+1;i<8;i++)
        tr.events[i].x = rd_bits.elements[i];// not truly non-deterministic
}