
#can be any number
page = 0

def setup():
    size(640, 480)
    
def draw():
#    global page
#    if mousePressed:
        #increases by 1 every time the frame is being pressed dont use
        #page += 1

    
    if page == 0:
        background(255)
        fill(0)
        ellipse(50, 50, 200, 200)
    elif page == 1:
        background(49, 79, 79)
    elif page == 2:
        background(60, 220, 190)
    elif page == 3:
        background(0)
        
def mousePressed():
#only advances once per click
    global page
    page += 1
    
    
    
    
