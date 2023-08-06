# Markov Decision Processes - Part 3

MDP problemeleri bandit problemlerinde gördüğümüz evaluative feedbackin yanı sıra associative aspect de barındırır.

- ************************Evaluative Feedback Neydi************************
    
    Training bilgisini instruct etmek yerine evalüe etmek için kullanıyoruz.
    
    Aktif bir şekilde keşfetme ihtiyacını da buradan hissediyoruz. ( active exploration ). Bu şekilde gelen feedback, (purely evaluative - tamamen değerlendirici) aldığımız aksiyonun değerini bildirir ama en iyi ya da en kötü söylemez.
    

MDPler sıralı bir şekilde problem ele almada klasik yöntemlerden en önemlisidir. Sıralı şekilde karar aldığımız problemlerde şu anda alacağımız karar, sonraki bulunacağımız durumlara ve ödüllerin miktarına etki ediyor.

Bandit problemlerinde q*(a) yi her bir aksiyon için  estimate etmişken, MDPlerde q*(s,a)yi, içinde bulunduğumuz her bir farklı state için her bir farklı aksiyonun değerini ölçüyoruz. Ya da optimal aksiyonlar verildiğinde v*(s)i estimate ediyoruz.

v*(s) ve q*(s,a) statea bağımlı değerler, isabetli bir şekilde uzun zaman sonra sonuçlanacak olayların  şuan hesaplanmasına yardımcı oluyor. (accurately assigning creditis for long-term consequences)

[Chapter 3.1 Agent Environment Interface](Markov%20Decision%20Processes%20-%20Part%203%20e430c9c46fcf40fc9cb414d67ae42ce8/Chapter%203%201%20Agent%20Environment%20Interface%20bac8dbbd2eee431f8ef2ad5d54a58e8a.md)

[Chapter 3.2 - Goals and Rewards](Markov%20Decision%20Processes%20-%20Part%203%20e430c9c46fcf40fc9cb414d67ae42ce8/Chapter%203%202%20-%20Goals%20and%20Rewards%20cd269ad08f5f473495ef6d38fa82df83.md)

[Ch 3.3 Returns and Episodes](Markov%20Decision%20Processes%20-%20Part%203%20e430c9c46fcf40fc9cb414d67ae42ce8/Ch%203%203%20Returns%20and%20Episodes%2035d79cf155ec4001b4940fd4326ca143.md)

[Ch 3.5 Policies and Value Functions](Markov%20Decision%20Processes%20-%20Part%203%20e430c9c46fcf40fc9cb414d67ae42ce8/Ch%203%205%20Policies%20and%20Value%20Functions%207524363d44ed414bb0a39020c308319a.md)

[Chapter 3.6 Optimal Policies and Optimal Value Functions](Markov%20Decision%20Processes%20-%20Part%203%20e430c9c46fcf40fc9cb414d67ae42ce8/Chapter%203%206%20Optimal%20Policies%20and%20Optimal%20Value%20Fun%2061e67333a3744452affa5cff1a591828.md)