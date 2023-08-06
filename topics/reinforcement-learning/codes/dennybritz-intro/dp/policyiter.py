import numpy as np
import pprint
from gridworld import GridworldEnv


pp = pprint.PrettyPrinter(indent=2)
env = GridworldEnv()

def policy_eval(policy, env: GridworldEnv , discount_factor = 1.0 , theta = 1e-6):
    """
    Evaluate a policy given an environment and a full description
    """
    # start with random value function
    values = np.zeros(env.number_of_states)
    counter = 0
    while True:
        delta = 0
        counter += 1
        print("counter", counter)
        for state in range(env.number_of_states):
            value = 0
            for action, action_prob in enumerate(policy[state]):
                for prob, next_state, reward, done in env.P[state][action]:
                    value += action_prob * prob * (reward + discount_factor * values[next_state])
            delta = max(delta, np.abs(value - values[state]))
            values[state] = value
        if delta < theta:
            break
    return np.array(values)
        
    
def policy_improvement(env, policy_eval_function=policy_eval,  discount_factor=1.0):
    def one_step_lookahead(state, V):
        actions = np.zeros(env.nA)
        for a in range(env.nA):
            for prob, next_state, reward, done in env.P[state][a]:
                actions[a] += prob * (reward + discount_factor * V[next_state])
        return actions
    policy = np.ones([env.nS, env.nA]) / env.nA
    while True:
        print("policy",policy)
        V = policy_eval_function(policy, env, discount_factor)
        policy_stable = True
        
        for state in range(env.nS):
            chosen_action = np.argmax(policy[state])
            
            action_values = one_step_lookahead(state, V)
            best_action = np.argmax(action_values)
            
            if chosen_action != best_action:
                policy_stable = False
            policy[state] = np.eye(env.nA)[best_action]
        if policy_stable:
            return policy, V
        
policy, V = policy_improvement(env)
print("Policy Probability Distribution:")
print(policy)
print("")

print("Reshaped Grid Policy (0=up, 1=right, 2=down, 3=left):")
print(np.reshape(np.argmax(policy, axis=1), env.shape))
print("")

print("Value Function:")
print(V)
print("")

print("Reshaped Grid Value Function:")
print(V.reshape(env.shape))
print("")

expected_v = np.array([ 0, -1, -2, -3, -1, -2, -3, -2, -2, -3, -2, -1, -3, -2, -1,  0])
print(np.testing.assert_array_almost_equal(V, expected_v, decimal=2))