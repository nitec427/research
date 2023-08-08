# 5.3 Monte Carlo Control

Consider how MC estimation can be used in control, to approximate optimal policies.

**Şimdiyse, Monte Carlo kestirme yöntemlerinin kontrolde nasıl kullanılabileceğini, yani optimal policyleri nasıl bulacağına bakalım.**

In GPI one maintains both an approximate policy and approximate value functions. 

**Genel policy (politika, yöntem) iterasyonunda hem yaklaşık politikayı hem de yaklaşık değer fonksiyonunu kestirmeye çalışıyoruz.**

You repeatedly alter some value function more closely to the actual value function for the current policy.

**Sırasıyla birbirlerinin değerlerini güncelliyoruz, ve birbirilerine hedef oluyorlar.**

And the policy is repeatedly improved w.r.t to the current value function.

These two kinds of work against each other and creates a moving target for the other, but together they cause both policy and value function to approach optimality.

******First Trial******

Assume you have experimented unlimited number of times and used exploring starts idea.

************Policy Evaluation:************

Episodes are experienced with approximate action-value function approaching to the true function asymptotically.

Under the constraints above $q_{\pi_k}$ can be computed with MC methods for any $\pi_k$.

******************Politika (Policy) Değerlendirmesi:******************

Episodeler üzerinden her bir aksiyonun değerini kestiriyorsun. Ardından bu aksiyon değerlerini politika iyileştirme adımında kullanacaksın.

****************************Policy Improvement Phase:****************************

PI is done by making the policy greedy w.r.t to the current value function. In this case we have **********************************action-value function********************************** , and so no model is needed to construct greedy policy. For any action-value function q, corresponding greedy policy deterministically choose an action with maximal action-value.

**Politika iyileştirmesi için her bir evrede en iyi değeri veren aksiyonu seçiyoruz. Bunu seçerken elimizde politika değerlendirme aşamasından gelen yeni değerler mevcut ve onları kullanıyoruz. Böylelikle optimal politikayı elde edebiliyoruz.**

$\pi(s) = argmax_aq(s,a)$

PI then can be done by constructing each $\pi_{k+1}$, as the greedy policy with respect to $q_{\pi_{k}}$.

Here is the mathematical formulation of policy improvement. 

Let’s start in state s and follow policy  $\pi_{k+1}$

$q_{\pi_{k}}(s, \pi_{k+1}(s)) = q_{\pi_{k}}(s, argmax_a \pi_{k}(s,a)$ 

= $max_a q_{\pi_{k}}(s,a)$

≥ $q_{\pi_{k}}(s,\pi_{k}(s)$ ≥ $v_{\pi_{k}}$(s)