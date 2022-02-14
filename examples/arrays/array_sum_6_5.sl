(set-logic LIA)
(synth-fun findSum ( (y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) )Int ((Start Int ( 0 1 2 3 4 5 6 y1 y2 y3 y4 y5 y6 z (+ Start Start) (let ((z Int Start)) Start)  (ite BoolExpr Start Start))) (BoolExpr Bool ((< Start Start) (<= Start Start) (> Start Start) (>= Start Start)))))
(declare-var x1 Int)
(declare-var x2 Int)
(declare-var x3 Int)
(declare-var x4 Int)
(declare-var x5 Int)
(declare-var x6 Int)
(constraint (=> (> (+ x1 x2) 5) (= (findSum x1 x2 x3 x4 x5 x6 ) (+ x1 x2))))
(constraint (=> (and (<= (+ x1 x2) 5) (> (+ x2 x3) 5)) (= (findSum x1 x2 x3 x4 x5 x6 ) (+ x2 x3))))
(constraint (=> (and (and (<= (+ x1 x2) 5) (<= (+ x2 x3) 5)) (> (+ x3 x4) 5)) (= (findSum x1 x2 x3 x4 x5 x6 ) (+ x3 x4))))
(constraint (=> (and (and (<= (+ x1 x2) 5) (and (<= (+ x2 x3) 5) (<= (+ x3 x4) 5))) (> (+ x4 x5) 5)) (= (findSum x1 x2 x3 x4 x5 x6 ) (+ x4 x5))))
(constraint (=> (and (and (<= (+ x1 x2) 5) (and (<= (+ x2 x3) 5) (and (<= (+ x3 x4) 5) (<= (+ x4 x5) 5)))) (> (+ x5 x6) 5)) (= (findSum x1 x2 x3 x4 x5 x6 ) (+ x5 x6))))
(constraint (=> (and (<= (+ x1 x2) 5) (and (<= (+ x2 x3) 5) (and (<= (+ x3 x4) 5) (and (<= (+ x4 x5) 5) (<= (+ x5 x6) 5))))) (= (findSum x1 x2 x3 x4 x5 x6 ) 0)))
(check-synth)
