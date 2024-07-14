# Import the necessary libraries
from nada_dsl import *
import matplotlib.pyplot as plt

def nada_main():
    display_string = "NILLION X HHGOA"
    num_chars = len(display_string)
    
    # Define a party for each character in the string
    parties = [Party(name=f"Party{i+1}") for i in range(num_chars)]
    
    # Define secret inputs for character positions (x, y) and ASCII values
    outputs = []
    for i in range(num_chars):
        x_pos = SecretInteger(Input(name=f"x_pos_{i}", party=parties[i]))
        y_pos = SecretInteger(Input(name=f"y_pos_{i}", party=parties[i]))
        ascii_val = SecretInteger(Input(name=f"ascii_val_{i}", party=parties[i]))

        # Append outputs
        outputs.append(Output(x_pos, f"x_pos_output_{i}", parties[i]))
        outputs.append(Output(y_pos, f"y_pos_output_{i}", parties[i]))
        outputs.append(Output(ascii_val, f"ascii_val_output_{i}", parties[i]))
    
    return outputs

# Simulated NADA execution environment
def run_nada_program():
    display_string = "NILLION X HHGOA"
    num_chars = len(display_string)
    
    # Simulate positions and ASCII values for visualization
    positions = [(i, 0) for i in range(num_chars)]
    ascii_values = [ord(c) for c in display_string]
    
    return positions, ascii_values

# Running the NADA program to get positions and ASCII values
positions, ascii_values = run_nada_program()

# Visualization part using matplotlib

# Convert ASCII values to characters
characters = [chr(ascii_val) for ascii_val in ascii_values]

# Plotting the characters
fig, ax = plt.subplots()
for (x, y), char in zip(positions, characters):
    ax.text(x, y, char, fontsize=18, ha='center', va='center')

ax.set_xlim(-1, len(characters))
ax.set_ylim(-1, 1)
ax.axis('off')

# Save the plot to a file
plt.savefig("/content/nillion-python-starter/quickstart/client_code/nillion_x_hh_goa.png")

# Display the plot
plt.show()
