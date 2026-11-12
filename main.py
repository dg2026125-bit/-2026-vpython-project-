Web VPython 3.2
import random
cube1 = box(texture = "https://i.postimg.cc/xdxwBNXK/samgagpeullaseukeu.png")
cube0 = sphere(pos = vec(0.3,-0.4,0.5),size = vec(0.1,0.1,0.1))
colors = [color.red, color.blue, color.green]
b = sphere(size = vec(0.05,0.05,0.05), pos = vec(0,0.4,0.5))
def on_click(evt) : 
    if mag(cube0.pos - evt.pos) < 1 :
        cube1.color = random.choice(colors)
        for i in range(6) :
            rate(5)
            b.pos.y += 0.1
            b.pos.x += random.uniform(-0.15, 0.1)
            b.opacity = b.opacity  - 0.15
            
               
    
scene.bind('click', on_click)
