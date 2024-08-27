best_time = 0
goal_time = 60
held_times = []

try:
    while True:
        time = int(input("How long did you hold your breath? "))

        if time <= 0:
            break

        held_times.append(time)

        if time > best_time:
            best_time = time
            print(f"A personal best! {time} seconds is your best time.")

        if time >= goal_time:
            if time != best_time:  # Ensure the personal best message is not repeated
                print(f"A personal best! {time} seconds is your best time.")
            print("You reached your goal!!!")
            break

except ValueError:
    print("Recording ended")

if held_times:
    print("Your results are:")
    for t in sorted(held_times, reverse=True):
        print(f"{t} seconds")
else:
    print("Sorry, you have not entered any valid times.")
