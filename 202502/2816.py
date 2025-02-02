target_channel = ["KBS1", "KBS2"]


def button_function_a(current_channel):
    global button

    if channel[0] == "KBS1":
        return

    else:
        if channel[current_channel] == "KBS1":
            button += "4"
            channel[current_channel], channel[current_channel - 1] = channel[current_channel - 1],  channel[current_channel]
            button_function_a(current_channel - 1)

        else:
            button += "1"
            button_function_a(current_channel + 1)


def button_function_b(current_channel):
    global button

    if channel[1] == "KBS2":
        return

    else:
        if channel[current_channel] == "KBS2":
            button += "4"
            channel[current_channel], channel[current_channel - 1] = channel[current_channel - 1],  channel[current_channel]
            button_function_b(current_channel - 1)

        else:
            button += "1"
            button_function_b(current_channel + 1)


N = int(input())
channel = []
button = ""

for _ in range(N):
    channel.append(input())

button_function_a(0)
button_function_b(0)

print(button)