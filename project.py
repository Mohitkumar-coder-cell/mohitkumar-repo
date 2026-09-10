# import turtle
# import math
# import random

# screen = turtle.Screen()
# screen.bgcolor("#1a0514")
# screen.title("For You <3")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.penup()

# WORD = "kimminsu"
# FONT = ("Arial", 8, "bold")

# def draw_petal(base, base_angle, length, width, color, points=26):
#     t.color(color)
#     bx, by = base
#     cos_a, sin_a = math.cos(base_angle), math.sin(base_angle)
#     for i in range(points + 1):
#         theta = i * math.pi / points
#         out = length * math.sin(theta)
#         side = width * math.sin(theta) * math.cos(theta)
#         rx = out * cos_a - side * sin_a
#         ry = out * sin_a + side * cos_a
#         t.goto(bx + rx, by + ry)
#         t.write(WORD, align="center", font=FONT)
# def draw_leaf(base, angle_deg, length, width):
#     draw_petal(base, math.radians(angle_deg), length, width, "#2e8b57", points=22)

# rings = [
#     {"radius": 0, "count": 4, "length": 40, "width": 15, "color": "#ffe6f2", "offset": 45},
#     {"radius": 10, "count": 5, "length": 50, "width": 25, "color": "#ffb3d9", "offset": 0},
#     {"radius": 20, "count": 7, "length": 70, "width": 35, "color": "#ff66b2", "offset": 30},
#     {"radius": 30, "count": 9, "length": 90, "width": 45, "color": "#ff1493", "offset": 15},
#     {"radius": 40, "count": 12, "length": 110, "width": 55, "color": "#c71585", "offset": 0},
# ]
# t.goto(0, -30)
# t.setheading(260)
# t.pendown()

# t.color("#2e8b57")
# t.pensize(4)
# t.circle(250, 25)

# pos1, head1 = t.position(), t.heading()
# t.pensize(1)
# draw_leaf(base=pos1, angle_deg=160, length=50, width=25)
# t.penup()
# t.goto(pos1)
# t.setheading(head1)
# t.pendown()

# t.color("#2e8b57")
# t.pensize(4)
# t.circle(250, 20)

# pos2, head2 = t.position(), t.heading()
# t.pensize(1)
# draw_leaf(base=pos2, angle_deg=20, length=55, width=28)
# t.penup()
# t.goto(pos2)
# t.setheading(head2)
# t.pendown()

# t.color("#2e8b57")
# t.pensize(4)
# t.circle(250, 30)
# t.penup()
# t.pensize(1)
# for ring in rings:
#     for i in range(ring["count"]):
#         angle = (360 / ring["count"]) * i + ring["offset"]

#         base_x = ring["radius"] * math.cos(math.radians(angle))
#         base_y = ring["radius"] * math.sin(math.radians(angle))

#         draw_petal(
#             base=(base_x, base_y),
#             base_angle=math.radians(angle),
#             length=ring["length"],
#             width=ring["width"],
#             color=ring["color"]
#         )

# t.color("#ff99cc")
# for _ in range(12):
#     x = random.randint(-250, 250)
#     y = random.randint(-250, 250)
#     if math.hypot(x, y) > 130:
#         t.goto(x, y)
#         t.write("<3", align="center", font=("Courier", 10, "bold"))

# t.goto(0, -320)
# t.color("white")
# t.write("Click anywhere to close", align="center", font=("Arial", 10, "italic"))
# screen.exitonclick()

# import turtle

# p = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# p.pencolor('#7c909c')    # lowercase hex
# p.speed(10)
# colors = ('#9c3758', '#df8752', '#1a266b', '#156a14')

# for n in range(5):
#     p.pencolor(colors[n % 4])
#     for x in range(8):
#         p.pensize(2)
#         for i in range(2):
#             p.circle(80 + n*20, 90)
#             p.left(90)
#         p.left(45)

# p.hideturtle()
# s.mainloop()  

#ATM project

# balance = 10000
# pin = 1234

# print("===== WELCOME TO ATM =====")

# # PIN verification
# attempts = 3

# while attempts > 0:
#     user_pin = int(input("Enter your PIN: "))

#     if user_pin == pin:
#         print("PIN correct!")
#         break
#     else:
#         attempts = attempts - 1
#         print("Wrong PIN!")
#         print("Attempts left:", attempts)

# if attempts == 0:
#     print("Your card is blocked.")

# else:

#     # ATM Menu
#     while True:

#         print("\n===== ATM MENU =====")
#         print("1. Check Balance")
#         print("2. Withdraw Money")
#         print("3. Deposit Money")
#         print("4. Change PIN")
#         print("5. Exit")

#         choice = int(input("Enter your choice: "))

#         # Check Balance
#         if choice == 1:
#             print("Your balance is ₹", balance)

#         # Withdraw
#         elif choice == 2:
#             amount = int(input("Enter amount to withdraw: "))

#             if amount <= 0:
#                 print("Invalid amount!")

#             elif amount > balance:
#                 print("Insufficient balance!")

#             else:
#                 balance = balance - amount
#                 print("Please collect your cash.")
#                 print("Remaining balance: ₹", balance)

#         # Deposit
#         elif choice == 3:
#             amount = int(input("Enter amount to deposit: "))

#             if amount <= 0:
#                 print("Invalid amount!")

#             else:
#                 balance = balance + amount
#                 print("Money deposited successfully.")
#                 print("New balance: ₹", balance)

#         # Change PIN
#         elif choice == 4:
#             old_pin = int(input("Enter old PIN: "))

#             if old_pin == pin:
#                 new_pin = int(input("Enter new PIN: "))
#                 pin = new_pin
#                 print("PIN changed successfully!")

#             else:
#                 print("Wrong old PIN!")

#         # Exit
#         elif choice == 5:
#             print("Thank you for using ATM!")
#             break

#         else:
#             print("Invalid choice!")

