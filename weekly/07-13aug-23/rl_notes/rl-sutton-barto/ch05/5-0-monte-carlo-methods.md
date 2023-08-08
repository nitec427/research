# Monte Carlo Yöntemleri - Bölüm 5

MC methods only requires experience. (Just sample)

Sample and average these returns. 

Only on the completion of an episode are value estimates and policies changed. MC methods can thus be incremental episode-by-episode but not a step-by-step(online) approach.

Also there is a non-stationarity problem with Monte Carlo methods. Because the value of the current state depends on the value of the next states and in each iteration state values change, the problem becomes non-stationarity. However with general policy iteration theorem(idea) we can overcome it.

[5.1 Monte Carlo Prediction ](5-1-monte-carlo-prediction.md)

[5.2 Monte Carlo Estimation of Action Values](5-2-Monte%20Carlo%20Estimation%20of%20Action%20Values.md)

[5.3 Monte Carlo Control](5-3-Monte%20Carlo%20Control.md)

[5.4 Monte Carlo Without Exploring Starts](5.4-Monte%20Carlo%20Without%20Exploring%20Starts.md)

[5.5 Off-Policy Prediction via Importance Sampling](5.5-Off-Policy%20Prediction%20via%20Importance%20Sampling.md)