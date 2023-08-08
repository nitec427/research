# 5.2 Monte Carlo Estimation of Action Values

If a model is not available, it is useful to estimate ******************action values (the values of state-action pairs)****************** rather than state values.

**Eğer elimizde bir model yoksa, aksiyon-değerlerini tahmin etmek evre-değerlerini tahmin etmekten daha faydalıdır.**

With a model, just state values are sufficient to determine a policy, simply look ahead one step and choose whichever action leads to best reward and next state.

**Bir model ile, sadece evre-değerleri policyi belirlemede yeterli olur. Bir adım ileriye bakarsın ve hangi aksiyon en iyi ödül ve sonraki evreyi veriyorsa onu seçersin.**

Without a model, state values alone are not sufficient. You must explicitly estimate the value of each action to make values useful in suggesting a policy.

**Ancak bir model olmadan, evre-değerleri tek başına yeterli değildir. Bariz bir şekilde aksiyon değerlerini tahmin ederek onları policy bulmada kullanman gerekir.**

Thus, one of the primary goals in MC is to estimate optimal action-values, q*.

**Bu yüzden Monte Carlo yöntemlerinin temel hedeflerden biri de optimal aksiyon-değerlerini bulan fonksiyonu kestirmektir.**

To do this, we first consider the policy evaluation problem for action values.

Policy evaluation problem for action values is to estimate $q_\pi(s,a)$, expected return when starting at s, and taking action a, thereafter following policy pi.

**Aksiyon-değerlerini değerlendirme problemi $q_\pi(s,a)$ i kestirmekten geçer, yani s evresinde ve a aksiyonu alındığında beklenen toplam ödülün hesaplanmasıdır.**

The MC methods are the same for state-values presented previously. (MC-first-visit, every-visit)

**Monte Carlo yöntemleri evre-değerini kestiren MC yöntemlerle aynı.**

Every-visit MC method estimates the value of s,a pair as the average of returns that have followed all the visits to it.

**Her-ziyaret MC yöntemi, s,a çiftinin değerini kestirirken çifte yapılan bütün ziyaretlerin bir ortalamasını alır.**

First-visit MC averages the return following the first time in each episode that the state was visited and action was selected. 

The only complication is s,a pairs may never be visited. Because $\pi$ is deterministic, each time we are in state s, we always follow the same action.

**Ancak bazı evrelerde bazı aksiyonlar alınmayabilir, çünkü belirli bir policyi takip ediyoruz. Bu yüzden exploration yapmamız da lazım.** 

**Bunu yapabilmek için exploring starts yöntemiyle, herhangi bir s,a çiftinin başlama olasılığını non-zero değerler veriyoruz ve sonsuzda yine her bir evre-aksiyon çiftinin değerini kestirmiş oluyoruz.**

**Maintaining exploration problem olarak da biliniyor bu problem.** 

We must assure continual exploration. One way to do this is by specifying that the episodes start in a state-action pair have non-zero probabilities. However this 

The assumption of ES is sometimes useful, but you can’t rely on it in general, particularly when learning directly from actual interaction with an environment. Instead, there methods assuring that all state-action pairs are encountered with a non-zero probability of selecting action in all states.