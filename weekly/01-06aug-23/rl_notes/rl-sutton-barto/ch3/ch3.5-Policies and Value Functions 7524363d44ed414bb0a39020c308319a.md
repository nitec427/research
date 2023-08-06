# Ch 3.5 Policies and Value Functions

Neredeyse bütün RL algoritmaları değer fonksiyonu dediğimiz fonksiyonları yakınsama problemini ilgilendirir.

Bu fonksiyonlar ya evrelerin ya da evre-aksiyon çiftlerinin ne kadar iyi olduğunu incelerler.

**************Buradaki ne kadar iyi olduğu kavramı, expected return ile açıklanır.**************

Agentın beklediği reward , alacağı aksiyona göre şekillenmektedir. 

Dolayısıyla, değer fonksiyonları tanımlanırken belirli bir şekilde aksiyon almayı göz önüne alır, bu belirli şekle policy (plan) ismini veririz.

Matematiksel anlamda, **************policy,************** statelerden olası aksiyonların selçilmesini sağlayan olasılık dağılımıdır.

RL methods specify how the agent’s policy is changed as a result of its experience.

**Aksiyonların elimizdeki policy altında seçilip seçilemeyeceğine dair olasılıkları kullanıyorsun.**

Ardından her bir next_state, reward çiftinin olasılığını bakıp dört elemanlı olasılık dağılımını kullanarak istediğin değeri buluyorsun.

****************Örnek 3.11:**************** If current state is S_t, and actions are selected according to policy pi, what is the expectation of R_(t+1) in terms of policy and four-argument probability distribution.

$E_\pi[R_{t+1} | S_t] = \sum_a \pi(a|s) \sum_{s',r} p(s',r | s,a) [r]$

$v_\pi = E_\pi[G_t | S_t = s] = E_\pi[\sum_k \gamma^kR_{t+k+1} | S_t = s]$ 

Değer fonksiyonunu evreler üzerinden yukarıdaki gibi tanımlayabileceğimiz gibi, aksiyon-evre çiftlerinin değerini de yine aşağıdaki eşitlikle verebiliriz.

$q_\pi(s,a) = E_\pi[G_t | S_t = s, A_t = a] = E_\pi[\sum_k \gamma^kR_{t+k+1} | S_t = s, A_t = a]$

Şimdi evre değer fonksiyonun, aksiyon-evre değer fonksiyonu ve policy üzerinden nasıl tanımlanabileceğini düşünelim. Evre değer fonksiyonunda hesaplanan değer içerisinde bulunduğumuz evrede olası olan bütün aksiyonların bize döndürdüğü returnlerin toplamıdır. Dolayısıyla herhangi bir policy pi altında aşağıdaki gibi bir eşitlik verebiliriz

$v_\pi = \sum_a \pi(a|s)q_\pi(a,s)$

Peki şimdi aksiyon-evre değer fonksiyonunu, sadece evre değer fonksiyonu 4-elemanlı olasılık dağılımı cinsinden nasıl yazabileceğimizi düşünelim. 

$q_\pi(s,a) = \sum_{s'} p(s', r|s,a) [r + \gamma v_\pi(s)]$

İki değer fonksiyonu da deneyimden hesaplanabilir. Yeteri kadar deney yapıldığında (idealde sonsuza dek), agent verilen planı takip ettiğinde ve her aksiyon-evre ve evre değeri için ortalama tuttuğunda bu ortalama değer fonksiyonlarından gelecek değere eşittir.

Çünkü her bir aksiyon ve evre idealde sonsuz kere değerlendirilecektir. ********Bu yöntemler sonra bahsedileceği gibi Monte Carlo yöntemleridir, they involve many random samples of actual returns.********

- Bellman Equation for $v_\pi$
    
    Yukarıdaki denklemleri takip edecek şekilde Bellman denklemini aşağıdaki formüllerle tanımlayabiliriz.
    
    $v_\pi(s) = E[ G_t | S_t = s ]$
    
    $v_\pi(s) = E[ R_{t+1} + \gamma G_{t+1} | S_t = s ]$
    
    $v_\pi(s) = E[\sum_a \pi(a|s) \sum_{s'}p(s',r | s,a) ][r+\gamma E_\pi[G_{t+1} | S_{t+1}]$ **************Bellman Equation**************
    
- [ ]  Sena hocanın işini yap. , Görselleştir → çok kez olanları temizle → 20 yeni etiket yaps