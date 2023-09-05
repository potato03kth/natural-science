import turtle as t

t.shape("classic")
r = 20
for i in range(5):
    t.circle(r)
    r += 10
for i in range(5):
    r -= 10
    t.circle(-r, 360, 6)
t.done()

r = 20
