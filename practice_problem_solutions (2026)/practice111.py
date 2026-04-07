# Bouncing Balls

def bouncing_ball(h, bounce, window):
    if h <= 0 or (bounce <= 0 or bounce >= 1) or window >= h:
        return -1
    
    seen = 1
    while h > 0:
        bounce_height = h * bounce
        if bounce_height > window:
            seen += 2
            h = bounce_height
        else:
            break
    return seen

print(bouncing_ball(3, 0.66, 1.5))  # 3
print(bouncing_ball(2, 0.5, 1))     # 1