import time

# Loop to simulate progress updates
for i in range(10):
    # Print progress
    print(f"Progress: {i}/10", end='\r')
    # Simulate some processing time
    time.sleep(1)

print("\nTask complete!")