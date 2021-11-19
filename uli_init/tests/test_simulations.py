from uli_init import simulate
from base_test import BaseTest

import pytest


class TestSimulate(BaseTest):

    def test_bad_inputs(self, peek_system):
        simulation = simulate.Simulation(
                peek_system,
                tau_p=0.1,
                dt=0.0001,
                mode="cpu"
                )
        # Only 1 of shrink params given
        with pytest.raises(ValueError):
            simulation.quench(
                kT=2,
                n_steps=1e3,
                shrink_kT=5,
                shrink_steps=None,
                shrink_period=None,
            )
        # Pressure and walls quench
        with pytest.raises(ValueError):
            simulation.quench(
                kT=2,
                pressure=0.1,
                n_steps=1e3,
                shrink_kT=None,
                shrink_steps=None,
                shrink_period=None,
                wall_axis=[1, 0, 0],
            )
        # Pressure and walls anneal
        with pytest.raises(ValueError):
            simulation.anneal(
                kT_init=2,
                kT_final=1,
                step_sequence = [1e3, 1e3],
                pressure=0.1,
                shrink_kT=None,
                shrink_steps=None,
                shrink_period=None,
                wall_axis=[1, 0 , 0],
            )
        with pytest.raises(ValueError):
            sim = simulate.Simulation(
                    system="path-to-file.gsd",
                    auto_scale=True,
                    ref_values=None
                )

    def test_quench_no_shrink(self, peek_system):
        simulation = simulate.Simulation(
                peek_system,
                tau_p=0.1,
                dt=0.0001,
                mode="cpu"
                )
        simulation.quench(
            kT=2,
            pressure=0.1,
            n_steps=1e3,
            shrink_kT=None,
            shrink_steps=None,
            shrink_period=None,
        )

    def test_anneal_no_shrink(self, peek_system):
        simulation = simulate.Simulation(peek_system, dt=0.0001, mode="cpu")
        simulation.anneal(
            kT_init=4,
            kT_final=2,
            step_sequence=[1e3, 1e3],
            shrink_kT=None,
            shrink_steps=None,
            shrink_period=None,
        )

    def test_quench_npt(self, peek_system):
        simulation = simulate.Simulation(
                peek_system,
                tau_p=0.1,
                dt=0.0001,
                mode="cpu"
                )
        simulation.quench(
            kT=2,
            pressure=0.1,
            n_steps=1e3,
            shrink_kT=8,
            shrink_steps=1e3,
            shrink_period=1,
        )

    def test_quench(self, peek_system):
        simulation = simulate.Simulation(peek_system, dt=0.0001, mode="cpu")
        simulation.quench(
            kT=2,
            n_steps=1e3,
            shrink_kT=8,
            shrink_steps=1e3,
            shrink_period=1,
        )

    def test_anneal_npt(self, pekk_system):
        simulation = simulate.Simulation(
                pekk_system,
                dt=0.0001,
                tau_p=0.1,
                mode="cpu"
                )
        simulation.anneal(
            kT_init=4,
            kT_final=2,
            pressure=0.1,
            step_sequence=[1e3, 1e3],
            shrink_kT=8,
            shrink_steps=1e3,
            shrink_period=1,
        )

    def test_anneal(self, pekk_system):
        simulation = simulate.Simulation(pekk_system, dt=0.0001, mode="cpu")
        simulation.anneal(
            kT_init=4,
            kT_final=2,
            step_sequence=[1e3, 1e3],
            shrink_kT=8,
            shrink_steps=1e3,
            shrink_period=1,
        )

    def test_quench_noH(self, pekk_system_noH):
        simulation = simulate.Simulation(pekk_system_noH, dt=0.001, mode="cpu")
        simulation.quench(
            kT=2,
            n_steps=1e3,
            shrink_kT=8,
            shrink_steps=1e3,
            shrink_period=1,
        )

    def test_anneal_noH(self, peek_system_noH):
        simulation = simulate.Simulation(peek_system_noH, dt=0.001, mode="cpu")
        simulation.anneal(
            kT_init=4,
            kT_final=2,
            step_sequence=[1e3, 1e3, 1e3],
            shrink_kT=8,
            shrink_steps=1e3,
            shrink_period=1,
        )

    def test_walls_quench(self, peek_system_noH):
        simulation = simulate.Simulation(peek_system_noH, dt=0.001, mode="cpu")
        simulation.quench(
            kT=2,
            n_steps=1e3,
            shrink_kT=6,
            shrink_steps=1e3,
            shrink_period=5,
            wall_axis=[1,0,0],
        )

    def test_walls_anneal(self, peek_system_noH):
        simulation = simulate.Simulation(peek_system_noH, dt=0.001, mode="cpu")
        simulation.anneal(
            kT_init=4,
            kT_final=2,
            step_sequence=[1e3, 1e3],
            shrink_kT=6,
            shrink_steps=1e3,
            shrink_period=5,
            wall_axis=[1,0,0],
        )

    def test_slabs_quench(self, test_slab):
        simulation = simulate.Simulation(test_slab, dt=0.0001, mode="cpu")
        simulation.quench(kT=2, n_steps=1e3, wall_axis=[1,0,0])

    def test_slabs_anneal(self, test_slab):
        simulation = simulate.Simulation(test_slab, dt=0.0001, mode="cpu")
        simulation.anneal(
            kT_init=4, kT_final=2, step_sequence=[1e3, 1e3, 1e3], wall_axis=[1,0,0]
        )

    def test_tensile_sim(self, test_slab):
        simulation = simulate.Simulation(test_slab, dt=0.00001, mode="cpu")
        simulation.tensile(kT=2.0, strain=0.25, n_steps=1e3, expand_period=10)

