from mayavi import mlab
import numpy as np

# Criar uma esfera para representar o cérebro
theta, phi = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Adicionar a esfera à cena
mlab.mesh(x, y, z, color=(0.7, 0.7, 1), opacity=0.7)

# Adicionar uma coroa ao redor do cérebro para representar a atividade cerebral
mlab.points3d(0, 0, 0, scale_factor=1.2, color=(1, 1, 0), resolution=50)

# Configurar a visualização
mlab.view(azimuth=45, elevation=45, distance=150)

# Exibir a cena
mlab.show()