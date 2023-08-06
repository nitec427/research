# 4.7 Efficiency of Dynamic Programming

DP algoritmaları çok büyük problemlerde pratik olmayabilir, ancak diğer MDP çözme yöntemleriyle kıyaslandığında, oldukça efficient olduklarını görebiliriz.

Birkaç teknik detayı göz ardında bırakırsak, DPnin en iyi policyi bulmak için  worst-time karışıklığı evrelerin ve aksiyonların kümesinin polinomik ifadesidir.

DP yöntemleri toplam seçilebilecek policy sayısı $k^n$ olsa bile polinomik bir zaman aralığında en iyi policyi bulabilir.

Bu açıdan bakıldığında diğer yöntemlerden (direct search over policy space) exponansiyel anlamda daha hızlıdır.

Lineer programming yöntemleri de yakınsama olarak oldukça hızlıdır, ancak problemin boyutu büyüdükçe pratik olmayan bir hale gelirler ve DP burada öne geçer. Büyük boyutlu problemler için ancak DP uygundur.