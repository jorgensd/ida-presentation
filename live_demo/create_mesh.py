import gmsh

gmsh.initialize()
gmsh.merge("part_less_fillets.step")
gmsh.model.addPhysicalGroup(2, tags=[14], tag=58, name="fixed")
gmsh.model.addPhysicalGroup(2, tags=[15,16], tag=59, name="traction")
gmsh.model.addPhysicalGroup(3, tags=[1], tag=1, name="Tool")

gmsh.model.mesh.generate(3)
gmsh.model.mesh.refine()
gmsh.model.mesh.optimize("Netgen")
gmsh.model.mesh.setOrder(2)
gmsh.write("mesh.msh")

gmsh.fltk.run()
