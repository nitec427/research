# Dynamic Programming - Bölüm 4

Collection of algorithms that can be used compute optimal policies given a perfect model of the environment as a MDP.

Classical DP algorithms are of limited utility, because they assume perfect model of the env, and the cost but they are still important theoretically. 

The key idea of DP and RL generally, is the use of value functions to organize and structure the search for good policies.  

We can easily obtain optimal policies once we have found optimal value functions v* or q* which satisfy the Bellman equations.

$v_*(s) = max_aE[R_{t+1} + \gamma v_*(S_{t+1}]$

DP algorithms are obtained by turning Bellman equations into assignments.

[Chapter 4.1 Policy Evaluation (Prediction)](ch4.1-policy-evaluation.md)

[Chapter 4.2 Policy Improvement](ch4.2-policy-improvement.md)

[Chapter 4.3 Policy Iteration](ch4.3-policy-iteration.md)

Chapter sonu sorularını çöz policy iterationda

[Chapter 4.4 Value Iteration](ch4.4-value-iteration.md)

[Chapter 4.5 Asenkron Dynamic Programming](ch4.5-async-dp.md)

[Chapter 4.7 Efficiency of Dynamic Programming](ch4.7-efficiency-of-dp.md)