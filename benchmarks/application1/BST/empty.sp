//@Description Binary tree

var {
    tree_node empty_out;
}

relation {
    bst_empty(empty_out);
}

generator {
    boolean AP -> compare(S, S + ??(1))
                | tree_equal(T, T) | !tree_equal(T, T)
                | is_empty(T) | !is_empty(T);
    int S -> tree_size(T) | 0;
    tree_node T -> empty_out;
}

example {
    int -> ??(2) | -1 * ??(2) ;
    tree_node(4) -> bst_empty() | bst_insert(tree_node, int);
}