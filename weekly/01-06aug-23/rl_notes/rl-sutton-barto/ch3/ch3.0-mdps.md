# Markov Decision Processes - Part 3

MDP problemeleri bandit problemlerinde gördüğümüz evaluative feedbackin yanı sıra associative aspect de barındırır.

- ************************Evaluative Feedback Neydi************************
    
    Training bilgisini instruct etmek yerine evalüe etmek için kullanıyoruz.
    
    Aktif bir şekilde keşfetme ihtiyacını da buradan hissediyoruz. ( active exploration ). Bu şekilde gelen feedback, (purely evaluative - tamamen değerlendirici) aldığımız aksiyonun değerini bildirir ama en iyi ya da en kötü söylemez.
    

MDPler sıralı bir şekilde problem ele almada klasik yöntemlerden en önemlisidir. Sıralı şekilde karar aldığımız problemlerde şu anda alacağımız karar, sonraki bulunacağımız durumlara ve ödüllerin miktarına etki ediyor.

Bandit problemlerinde q*(a) yi her bir aksiyon için  estimate etmişken, MDPlerde q*(s,a)yi, içinde bulunduğumuz her bir farklı state için her bir farklı aksiyonun değerini ölçüyoruz. Ya da optimal aksiyonlar verildiğinde v*(s)i estimate ediyoruz.

v*(s) ve q*(s,a) statea bağımlı değerler, isabetli bir şekilde uzun zaman sonra sonuçlanacak olayların  şuan hesaplanmasına yardımcı oluyor. (accurately assigning creditis for long-term consequences)

[Chapter 3.1 Agent Environment Interface](ch3.1-agent-environment-interface.md)

[Chapter 3.2 - Goals and Rewards](ch3.2-goals-rewards.md)

[Ch 3.3 Returns and Episodes](ch3.3-returns-and-episodes.md)

[Ch 3.5 Policies and Value Functions](ch3.5-policies-and-value-functions.md)

[Chapter 3.6 Optimal Policies and Optimal Value Functions](ch3.6-optimal-policies-optimal-value-functions.md)
