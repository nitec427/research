# Chapter 4.2 Policy Improvement

Değer fonksiyonlarını policyler için hesaplamamızın nedeni daha iyi policyler elde etmektir. Örneğin gelişigüzel bir policy belirleyip değer fonksiyonunu yazdık.

The reason for computing value functions is to help find better policies.

Imagine we have determined value function for an arbitrary policy.

For some state s, we’d like to know whether to change the policy to deterministically choose an action $a \neq \pi(s)$

Herhangi bir state s için, deterministic bir şekilde aksiyon alabilmek için policyi değiştirip değiştirmemeye karar vermeyi merak ediyoruz.

Elimizdeki state ve policy den $v_\pi (s)$ in ne kadar iyi olduğunu biliyoruz, peki policyi değiştirdiğimizde yeni sonucun daha iyi olup olmadığını nasıl anlarız. 

Bunu bilmenin bir yolu evre s’teyken aksiyon a’yı seçip, elimizdeki policyi kullanmaktır. Böyle yaptığımızda aşağıdaki değeri elde ederiz

$q_\pi(s|a) = E[R_{t+1} + \gamma v_\pi(S_{t+1}|S_t =s, A_t=a)$

Burada önemli kriter, seçilen aksiyonun v_pi(s)den büyük ya da küçük olduğunu bulmak . Eğer büyükse, bu a aksiyonu s evresinde almanın optimal sonuca sebep olduğunu gösterir ve a’yı seçen policyi kullanmamız gerektiğini söyler. Böylece evre s’e geldiğimizde her zaman a aksiyonunu seçeriz. 

Bu teoremin doğruluğunu ******************************************************************************************************policy improvement theorem olarak adlandırabiliriz.******************************************************************************************************

Let pi and pi’ be any pair of deterministic policies.

$q_\pi(s, \pi'(s)) >= v_\pi(s)$

Yukarıdaki denklem sağlandığında pi’ planı elimizdeki plandan daha iyidir ve o takip edilmelidir. Bu her bir state için sağlandığında optimal policyi elde etmiş oluruz. Bütün statelera bunu uyguladığımızda optimal policy şartı aşağıda verildiği gibi olur.

$v_{\pi'}(s) >= v_\pi$ 

It must obtain greater or equal expected return from all states.