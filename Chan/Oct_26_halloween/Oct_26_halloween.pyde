# sky: dark blue faded to black pic
# moon: yellowy white circle with texture
# clouds: 2 layers back layer 1 shade darker
# witch on broom: black sillouette (flies faster for 1 sec when click)
# grass: dark green rectangle
# house: base square, windows rectangle (cracked, closed lights, scratching arm fade form black to figure), roof
# open gate
# bench
# ghost sitting on bench
# cat: on pillars of gate
# trick or treaters: ghost, witch, officer (drop candy when click)

x = 0

def setup(): 
    size(640, 480)
    
# sky
background

# moon

# clouds 1st layer
def draw():
    
    global x
    
    if x >= 640:
        x = 0     
    x += 2
    
    noStroke()
    ellipse(x, height/10, 20, 20)
    ellipse(x+10, height/10, 20, 20)
    ellipse(x+20, height/10, 20, 20)
    ellipse(x+5, height/10+5, 20, 20)
    ellipse(x+15, height/10+5, 20, 20)
    
    ellipse(x+40, height/10+5, 20, 20)
    
# witch sillouette

# clouds 2nd layer

# grass

#
