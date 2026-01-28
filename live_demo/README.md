# Instructions

To run example as script:

```bash
xhost +local:host
docker run -ti --network=host -e DISPLAY=$DISPLAY -e LIBGL_ALWAYS_SOFTWARE=1 -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/root/shared -w /root/shared --rm --shm-size=512m  --entrypoint=/bin/bash ghcr.io/fenics/dolfinx/lab:stable
```

To run as jupyter notebook:

```bash
docker run -ti --network=host -e pyvista_jupyter_backend=html -v $(pwd):/root/shared -w /root/shared --rm --shm-size=512m  ghcr.io/fenics/dolfinx/lab:stable
```

## Converting script to notebook

Run

```bash
python3 -m pip install jupytext
python3 -m jupytext script.py --to ipynb
```

# Meshing pipeline

1. Look at step file (`gmsh part_less_fillets.step`)
2. Convert into mesh (`gmsh mesh.geo`)
   - Press `Mesh->3D`
   - Press `Mesh->Refine by splitting`
   - Press `Mesh->Optimize 3D (NetGen)`
   - Press `Mesh->Set order 2`
   - Press `Mesh->Save`
3. Optionally look at surfaces (`Tools->Visibility`/`ctrl+shift+v`)
   - Select individual physical or elementary surfaces/volumes




# Other material models
## Mooney-Rivlin
Assumptions: (Cauchy stress in terms of strain invariants and deformation tensors)
https://en.wikipedia.org/wiki/Mooney%E2%80%93Rivlin_solid
https://en.wikipedia.org/wiki/Finite_strain_theory#Deformation_gradient_tensor

```python
uh = dolfinx.fem.Function(V)
I = ufl.Identity(len(uh))
F = I + ufl.grad(uh)
B = F * F.T # Left Cauchy Green
J = ufl.det(F)
# Invariants
I1 = ufl.tr(B) # lmbda_i**2

# lmbda_1**2*lmbda_2**2+lmbda_2**2*lmbda_2**3+lmbda_1**3*lmbda_1**2
I2 = 1/2 * (ufl.tr(B)**2 - ufl.tr(B*B)) 
I1b = (J **(-2/3)) * I1
I2b = (J **(-4/3)) * I2
W = C1 * (I1b - 3) + C2 * (I2b - 3)
```