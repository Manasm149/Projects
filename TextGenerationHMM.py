import numpy as np

# Initialize the starting state based on the initial distribution pi
def initialize_pos(pi):
    r = np.random.random()  # Random float in [0, 1)
    cumulative_distribution = np.cumsum(pi)  # Cumulative sum of pi
    for q, probability in enumerate(cumulative_distribution):
        if r <= probability:
            return q  # Return first state where cumulative prob exceeds r

# Generate a sequence of text using a Hidden Markov Model
def textGen(pi, A, B, tl, dictionary):
    text = []
    current_state = initialize_pos(pi)  # Sample initial state based on pi
    for _ in range(tl):
        # Choose a word from the dictionary based on emission probabilities
        word = np.random.choice(dictionary, p=B[current_state])
        text.append(word)
        # Transition to the next state based on A
        next_state = np.random.choice(len(pi), p=A[current_state])
        current_state = next_state
    return text

# Reads the model parameters from user input
def main():
    # Read m = number of states, n = vocabulary size, tl = text length
    first_line = input().strip().split()
    m = int(first_line[0])  
    n = int(first_line[1])  
    tl = int(first_line[2]) 
    
    # Read initial state distribution pi
    pi = list(map(float, input().strip().split()))
    
    # Read transition probability matrix A (m x m)
    A = []
    for _ in range(m):
        row = list(map(float, input().strip().split()))
        A.append(row)
    
    # Read emission probability matrix B (m x n)
    B = []
    for _ in range(m):
        row = list(map(float, input().strip().split()))
        B.append(row)
        
    return m, n, tl, pi, A, B

if __name__ == "__main__":
    # Read parameters
    m, n, tl, pi, A, B = main()
    
    # Initialize the dictionary as a list of integers [0, 1, ..., n-1]
    dictionary = list(range(n))
    
    # Set seed for reproducibility
    np.random.seed(0)
    
    # Generate text using HMM
    text = textGen(pi, A, B, tl, dictionary)
    
    # Output the generated text
    for i in range(len(text)):
        print(text[i], end=" ")
