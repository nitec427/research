# Chapter 3.6 Optimal Policies and Optimal Value Functions

Solving RL, means, roughly finding a policy that achieves a lot of reward in the long run.

Value functions define partial ordering over policies.

A policy is better than policy_2 if its expected return is higher than or equal to  policy_2 for all the states.

Iow pi ≥ pi’ < = > v_pi ≥ v_pi’

There is at least one policy that is better than or equal to all other policies. This is an **optimal policy**.

Although there may be more than one, we denote all the policies by pi*. 

Optimal policies also share the same optimal action-volue function denoted by q*.