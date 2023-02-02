#!/usr/bin/env python3
"""
Importable and runnable geovista example.

Notes
-----
.. versionadded:: 0.1.0

"""

import geovista as gv
from geovista.pantry import hexahedron
import geovista.theme  # noqa: F401


def main() -> None:
    """
    This example demonstrates how to create a mesh from 2-D latitude and longitude
    unstructured cell points. The resulting mesh contains 6-sided (hexagonal)
    cells.

    The data is synthetically generated and targets the mesh faces/cells.

    Note that, Natural Earth coastlines are also rendered.

    """
    # load the sample data
    sample = hexahedron()

    # create the mesh from the sample data
    mesh = gv.Transform.from_unstructured(sample.lons, sample.lats, data=sample.data)

    # provide mesh diagnostics via logging
    gv.logger.info("%s", mesh)

    # plot the mesh
    plotter = gv.GeoPlotter()
    sargs = dict(title=f"{sample.name} / {sample.units}", shadow=True)
    plotter.add_mesh(mesh, scalar_bar_args=sargs)
    plotter.add_coastlines()
    plotter.add_axes()
    plotter.add_text(
        "DYNAMICO Hexahedron (10m Coastlines)",
        position="upper_left",
        font_size=10,
        shadow=True,
    )
    plotter.show()


if __name__ == "__main__":
    main()
