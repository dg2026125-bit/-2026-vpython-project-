Web VPython 3.2
cube1 = box(texture = "https://i.postimg.cc/xdxwBNXK/samgagpeullaseukeu.png")
cube0 = sphere(pos = vec(0.3,-0.4,0.5),size = vec(0.1,0.1,0.1))

def on_click(evt) : 
    if mag(cube0.pos - evt.pos) < 1 :
        cube1.color = color.red
    
scene.bind('click', on_click)
