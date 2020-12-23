import pytest
from uli_init import simulate

class BaseTest:

    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()

    @pytest.fixture
    def peek_system(self):
        peek_sys = simulate.System(molecule='PEEK',
                                    para_weight=0.50,
                                    density=1.2,
                                    n_compounds = [3],
                                    polymer_lengths = [3],
                                    forcefield = 'gaff',
                                    remove_hydrogens = False)
        return peek_sys

    @pytest.fixture
    def pekk_system(self):
        pekk_sys = simulate.System(molecule='PEKK',
                                    para_weight=0.50,
                                    density=1.2,
                                    n_compounds = [3],
                                    polymer_lengths = [3],
                                    forcefield = 'gaff',
                                    remove_hydrogens = False)
        return pekk_sys

    @pytest.fixture
    def peek_system_noH(self):
        peek_sys = simulate.System(molecule='PEEK',
                                    para_weight=0.50,
                                    density=1.2,
                                    n_compounds = [3],
                                    polymer_lengths = [3],
                                    forcefield = 'gaff',
                                    remove_hydrogens = True)
        return peek_sys

    @pytest.fixture
    def pekk_system_noH(self):
        pekk_sys = simulate.System(molecule='PEKK',
                                    para_weight=0.50,
                                    density=1.2,
                                    n_compounds = [3],
                                    polymer_lengths = [3],
                                    forcefield = 'gaff',
                                    remove_hydrogens = True)
        return pekk_sys
