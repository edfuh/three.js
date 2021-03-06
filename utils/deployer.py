import sys
import os

# MERGER

rev = 11;

files = [];
files.append('Three.js');
files.append('core/Color.js');
files.append('core/Vector2.js');
files.append('core/Vector3.js');
files.append('core/Vector4.js');
files.append('core/Rectangle.js');
files.append('core/Matrix4.js');
files.append('core/Vertex.js');
files.append('core/Face3.js');
files.append('core/Face4.js');
files.append('core/Geometry.js');
files.append('cameras/Camera.js');
files.append('objects/Object3D.js');
files.append('objects/Line.js');
files.append('objects/Mesh.js');
files.append('objects/Particle.js');
files.append('materials/BitmapUVMappingMaterial.js');
files.append('materials/ColorFillMaterial.js');
files.append('materials/ColorStrokeMaterial.js');
files.append('materials/FaceColorFillMaterial.js');
files.append('materials/FaceColorStrokeMaterial.js');
files.append('scenes/Scene.js');
files.append('renderers/Renderer.js');
files.append('renderers/CanvasRenderer.js');
files.append('renderers/SVGRenderer.js');
files.append('renderers/renderables/RenderableFace3.js');
files.append('renderers/renderables/RenderableFace4.js');
files.append('renderers/renderables/RenderableParticle.js');
files.append('renderers/renderables/RenderableLine.js');

string = '';

for item in files:
	src_file = open('../src/' + item,'r');
	string += src_file.read() + "\n";

dep_file = open('temp.js','w');
dep_file.write(string);
dep_file.close();


# YUICOMPRESSOR

os.system("java -jar yuicompressor-2.4.2.jar temp.js -o ../build/three.js --charset utf-8 -v");


# HEADER

output = '../build/three.js';
string = "// three.js r" + str(rev) + " - http://github.com/mrdoob/three.js\n";

src_file = open(output,'r');
string += src_file.read();

dep_file = open(output,'w');
dep_file.write(string);
dep_file.close();
