# Value Iteration

Policy iterationın büyük problemlerinden bir tanesi her adımda policy evaluation yapılmasıydı, çünkü policy evaluation içinde de birden fazla kere evreler işleniyordu.

Eğer policy değerlendirmesi iteratif bir şekilde yapılırsa, v_pi a yaklaşmak sonsuz kere denemyle elde edilir. Peki ******işlemin sonuna kadar beklemeli miyiz, yoksa bir yerde durmalı mıyız.******

Gridworld örneğinde de görülebileceği gibi 3 adımda yapılabilecek convergence en az 20 adım daha sürüyor. Dolayısıyla bunun daha kolay bir yolu olmalı.

Evet, bir şekilde policy iterationı yakınsama garantisini bozmadan kısaltabiliriz.

Özel bir duruma örnek olarak ilk değerlendirme aşamasındaki sweepten sonra bir daha hiç yapmamak (one update of each state)

Bu algoritmaya da **************value iterasyonu diyoruz.**************

Policy improvement ile truncated policy evaluation karışımı bir denklemle bulunabilir.

$v_{k+1}(s) = max_a E[R_{t+1} + \gamma v_k(s_{t+1}) ]$