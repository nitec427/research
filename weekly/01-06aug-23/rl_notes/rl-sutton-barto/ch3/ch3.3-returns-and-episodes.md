# Ch 3.3 Returns and Episodes

Amacımız uzun bir long runda T adım sonrasında elde edeceğimiz beklenen toplam rewardı maksimize etmektir. ****************************************************************************************Bunu literatürde return olarak tanımlamışlar.****************************************************************************************

En basit anlamında return, T adım içerisinde elde edilen toplam reward miktarıdır.

$G_t = R_{t+1} + R_{t+2},... + R_T$

Bu tarz bir tanımlama T adımının final adım olduğunu düşündüğümüzde işimize çokça yarayacaktır. Böylelikle agent-environment etkileşimini farklı episodelara bölebiliriz. Her bir episode terminal state dediğimiz bir statede son bulur.

**************************state = evre oldukça güzel duruyor., episode = serüven, parça**************************

Serüvenli tasklarda, terminal olmayan evrelerin oluşturduğu kümeye S, terminal kümeler dahil edilidğinde oluşan kümeye ise, $S^+$ diyoruz.

Yukarıda verilen ****************return tanımı discount factorü**************** içine katmadığı için eksik kalmaktadır. Discount denilen bir parametre ile agentın açgözlü bir şekilde en yakın zaman dilimindeki en büyük değerleri almasını sağlayabiliriz, ancak bunu yaparka sonraki adımlarda agenta sıkıntı da yaratabiliriz.

$G_t = R_{t+1} + \gamma R_{t+1} +  \gamma^2 R_{t+2} + ... = \sum_{k=0} \gamma^k R_{t+k+1}$

discount oranı sayesinde ileride karşılacağımız rewardların şu andaki time stepine etkisini ölçebiliyoruz.

Eğer discount değeri 1den küçük ve reward değerlerinden herhangi biri sonsuz olmuyorsa bu toplam bir süre sonra sabit bir sayıya yaklaşır.

Bir zaman adımı ve onu takip eden adımların arasında döngüsel ve ****************************************************çok çok önemli bir ilişki vardır.****************************************************

$G_t = R_{t+1} + \gamma(R_{t+2} + \gamma R_{t+3} + ...) = R_{t+1} + \gamma G_{t+1}$

Bu return denklemi terminal state, where G_T = 0 olduğunda bile sağlanabikiyor.

Return sonsuza kadar süren seri toplamı olsa da eğer discount değeri birden küçükse return şu hali alır.

$G_t = \sum_{k=0}^\infty \gamma^k = \frac{1}{1-\gamma}$