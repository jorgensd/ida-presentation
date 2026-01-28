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
2. Convert into mesh (`gmsh mesh_geo`)
   a. Press `Mesh->3D`
   b. Press `Mesh->Refine by splitting`
   c. Press `Mesh->Optimize 3D (NetGen)`
   d. Press `Mesh->Set order 2`
   e. Press `Mesh->Save`
3. Optionally look at surfaces (`Tools->Visibility`/`ctrl+shift+v`)
   a. Select individual physical or elementary surfaces/volumes
