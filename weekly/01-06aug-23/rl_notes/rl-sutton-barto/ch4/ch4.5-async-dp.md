# Asenkron Dynamic Programming

DP algoritmalarının en kötü yanı bütün stateler üzerinden her aşamada geçmemiz gerektiğidir. Sweep of the state set.

Eğer state set çok büyükse işlemler aşırı uzun süre alır.

Asenkron DP yöntemleri in-place iteratif DP yöntemleridir ve sistematik şekilde state sweep yapmazlar. Evreleri güncellerken herhangi bir sıraya önem göstermez, ve ondaki state durumu neyse onu kullanır. Bazı evrelerin durumu birkaç kez güncellenmişken, bazıları daha hiç güncellenmemiş olabilir.

Doğru bir şekilde yakınsaması için, async algoritma bütün evreleri güncellemek zorundadır, herhangi bir evreyi atlama gibi bir lüksü yoktur. Evrelerin seçiminde büyük bir esneklik sağlar.