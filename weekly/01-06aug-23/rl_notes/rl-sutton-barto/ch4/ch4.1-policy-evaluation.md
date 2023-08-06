# 4.1 Policy Evaluation (Prediction)

Consider how to compute state-value function, $v_\pi$ for an arbitrary policy.

Değerlendirme yapmadan önce evre-değer fonksiyonun rastgele bir pi policysi için hesaplanmasını düşünelim.

Buna **************policy evaluation diyoruz. Ayrıca kimi yerde prediction problem olarak da geçiyor.**************

$v_\pi(s) = E_\pi[G_t|S_t = s]$

$v_\pi(s) = E_\pi[R_{t+1} + \gamma v_\pi(s_{t+1})| S_t = s ]$ (eq 4.3)

$\sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')]$ (eq 4.4)

If the environment’s dynamics are completely known, then the last equation above is a system of S linear equations in S unknowns.

Eğer ortam bilgilerine tamamen hakimsek denklem 4.4deki işlemler S adet lineer denklem ve S bilinmeyenli denklemler sınıfına düşer.

In principle, the solution is straightforward but a tedious computation. For our purposes, iterative solution methods are most suitable.

Prensipte işlemler kolay gibi görünse de oldukça maliyetlidir. Bu amaçla, iteratif çözüm yöntemlerini kullanmak daha uygundur.

Başta gelişigüzel bir policy ile gelişigüzel ilk evre-değerini belirleyelim. v_0. Ardından takip eden her süreç bir önceki süreçten Bellman denklemleriyle elde edilir.

$v_{k+1}(s) = E\pi[R_{t+1} + \gamma v_k(S_{t+1}) | S_t =s]$ 

$\sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r+\gamma v_k(s')]$ 

Açıkça görüldüğü gibi $v_k = v_\pi$ sabit bir noktadır bu iterasyon için ve Bellman denklemleriyle bu eşitliği sağlayabiliriz. ******************bu algoritmaya iterative policy evaluation adını veriyoruz.******************

Consider a sequence of approximate value functions v0, … vn each mapping S+ → R. The initial approximation, is chosen arbitrarily and each successive approximation is obtained with Bellman equation for v_pi as an update rule.

Bir sonraki approximationı üretebilmek için, iterative policy evaluation aynı işlemi her bir evreye uygular. Evre s in bir önceki değerini, s evresini takip eden s’ evrelerinin eski değerlerinden elde edilen yeni değer ve beklenen immediate reward ile (R_t+1) ile değiştirir. (denkleme bir kez daha bakıp v_k+1 ile v_k farkına bakmanız iyi olabilir). Yine 2. denklemden de anlaşılabileceği gibi bütün farklı transitionlar üzerinden k+1. adımdaki değer hesaplanıyor

We call this operation an ****expected update.****

Yine bu işlemin ismi de ********************************expected update******************************** olarak geçer.