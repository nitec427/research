# Chapter 3.1 Agent Environment Interface

Sonlu MDPlerde sahip olabileceğimiz A→ aksiyon kümesi, S ve R kümeleri de sabit sayıda elemana sahip olur.

- State neidir
    
    Some representation of the environment
    
    Agentın içinde bulunduğu ortam hakkında bilgileri taşıyan bir kavramdır.
    

Her bir zaman dilimi t de agent S_t (anlık statei alır), ve buna dayanarak bir A_t seçimi yapar. A_t elemanı A(s) kümesinin içindedir. Yani şu anki statede alabileceğimiz aksiyonlardan bir tanesidir.

Bir zaman dilimi sonra, yani t+1 de aldığımız aksiyona göre R_t+1 dediğimiz bir reward (ödül) environment tarafından bize verilir ve kendimizi S_t+1 da buluruz

MDP ve agent böylece trajector dediğimiz ve sırasıyla giden bir etkileşim için girerler.

$p(s', r| s, a) = Pr(S_t = s', R_t = r | S_{t-1}=s, A_{t-1}$

Finite mdpler için yukarıdaki gibi bir olasılık denklemi yazabiliriz. Burada görülebileceği gibi her bir olası state (s’) ve oradan gelecek ödül r, bir önceki state ve orada alınan aksiyonlara bağlıdır.

MDPnin dinamiği olasılık dağılımından gelir.

p: S X R X S X A 

Peki state neden sadece bir önceki state ve orada alınan aksiyona bağlı. MDPleri kurgularken kısıtlamayı statea koyuyoruz. State kendisinden önce gelen bütün önceki statelerin de bir nevi bilgisini içeriyor diyebiliriz. Ama David Silverin olayını düşün o kadar da komplike değil. Eğer state önceki statelere bağlı değilse ******************************Markovian propertyi sağlıyor diyebiliriz.******************************

******************This is best viewed a restriction not on the decision process, but on the state.****************** 

Yukarıda (3.1) ile verilen denklemi kullanarak farklı eşitlikler elde edebiliriz.

Bunlardan ilki state-transition probability denklemi

$p(s' | s,a) = prob(s_t = s' | s_{t-1}, a_{t-1} = a)$

Ayrıca beklenen ödülü (reward) stateler ve aksiyonlar üzerinden expectation olarak da yazabiliriz.

$r(s,a) = E[ R_t | S_{t-1} = s, A_{t-1} = a] = \sum_{r\in R} r \sum_{s'\in S}p(s', r|s,a)$

Genel anlamda neyin agent neyin environment içerisinde kalacağını kestirmek kolay değil, daha önce yapay zeka derslerinde gördüğün gibi. Sutton ve Barto’da ise genel kural agentın arbitrary bir şekilde değiştiremediği her şey agentın dışında kalır diyebiliriz.  

Pratikte, the agent-environment boundary, agentla çevre arasındaki çizgi, stateler, aksiyonlar ve onlara bağlı ödüller belirlendikten sonra belli olur. Böylelikle spesifik olarak karar verme görevimiz (decision making task) belirlemiş oluruz.