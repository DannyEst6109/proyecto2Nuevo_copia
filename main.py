from gl import Raytracer, V3
from obj import *
from figures import *

width = 400
height = 400

Tvidrio_trans = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)
gold = Material(diffuse = (1, 0.8, 0 ),spec = 32, matType = REFLECTIVE)
madera = Material(diffuse = (0.6,0.2,0.2), spec = 64)

Respejo = Material(spec = 128, matType = REFLECTIVE)
Tagua = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
Rzafiro = Material(diffuse = (0.46,0.45,0.65), spec = 64, ior = 1.33, matType = REFLECTIVE)
Piedra = Material(diffuse = (0.4,0.4,0.4), spec = 64)
Tesmeralda = Material(diffuse = (0,0.61,0.44), spec = 64, ior = 1.33, matType = TRANSPARENT)
Tdiamante = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)
Trojo = Material(diffuse= (0.60, 0.06, 0.12), spec = 64, ior = 1.33, matType= TRANSPARENT)
Ocuarzo = Material(diffuse=(0.97, 0.79, 0.84), spec= 64, ior = 1.33, matType= OPAQUE)
lava = Material(texture = Texture('lava.bmp'))

rtx = Raytracer(width,height)
rtx.envmap = EnvMap("envmap_playa.bmp")

rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(-2, 5, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(-3, 0, 0), intensity = 0.5))

rtx.scene.append( Sphere(V3(-0.8,2,-4), 0.2, Tdiamante) )
rtx.scene.append( Sphere(V3(0.8,2,-4), 0.2, Tdiamante) )
rtx.scene.append( Sphere(V3(0,2,-8), 0.5, lava ))
rtx.scene.append( Sphere(V3(-3,-3,-4), 0.2, Tdiamante) )
rtx.scene.append( Sphere(V3(3,-3,-4), 0.2, Tvidrio_trans) )
rtx.scene.append( Sphere(V3(-2,-2,-4), 0.2, madera ) )
rtx.scene.append( Sphere(V3(2,-2,-4), 0.2, Tagua) )
rtx.scene.append( Sphere(V3(-1,-1,-4), 0.2, Piedra) )

rtx.scene.append( AABB(V3(0,-4,-8), V3(6,1,6), gold) )
rtx.scene.append( AABB(V3(0,-3,-8), V3(5,1,5), Ocuarzo) )
rtx.scene.append( AABB(V3(0,-2,-8), V3(4,2,4), Trojo) )
rtx.scene.append( AABB(V3(0,-1,-8), V3(3,1.5,2), Respejo) )
rtx.scene.append( AABB(V3(0,0,-8), V3(2,1.2,3), Tesmeralda) )

rtx.glRender()
rtx.glFinish('finalx.bmp')