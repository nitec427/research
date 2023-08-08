# 5.1 Monte Carlo Prediction

Consider first MC methods for learning the state-value function for a given policy. 

**Öncelikle MC metodlarından policy verildiğinde evre-değerlerini öğrenen yöntemleri düşünelim.**

$v_\pi$ , when $\pi$ is given

Recall that value of the state is its expected return.

**Bir evrenin değeri** $v_\pi$(s)**,  expected return ile açıklanıyordu.**

$V_\pi(s) = E[G_t | S_t = s]$

To estimate it from experience, simply average it over the first or every occurrences in the episode.

**Deneyimden kestirmenin en kolay yolu, s evresine yapılan ilk ziyaret için ya da her bir ziyaret için bir return değeri hesaplamak olur. Sonrasında bu değerleri ortalarız. Gözlem (sample) sayısı arttıkça kestirilen değer gerçek değere oldukça yaklaşır.**

Both first-visit MC and every-visit MC converges to the ideal value function when we sample infinitely many times.

**Black-jack örneği monte carloyu açıklamakta oldukça iyi bir yöntem.**

An important fact about MC methods is that the estimates for each state are ****independent.**** The estimate for one state does not build upon the estimate of any other state, as is the case in DP. ************Thus, we know that MC does not bootstrap.************

Monte Carlo yöntemlerinin bir diğer önemli yanı ise her evrenin birbirinden bağımsız olmasıdır. Örneğin ileride Temporal Difference Learningde öğreneceğimiz üzere evrelerin değeri, sonraki evrelerin değeri + bir zaman adımı sonrası ödülün toplamı değil, bütün bir deneyim sonrası elde edilen toplam ödüllerdir.