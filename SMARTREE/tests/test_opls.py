from ..smart_tree import bond_graph_to_smarts_dic

import mbuild as mb
import networkx as nx
import foyer

class Test_OPLS:
    def test_o_xylene(self):
        mol = mb.load('../opls_validation/o-xylene.mol2')
        smarts_dic = bond_graph_to_smarts_dic(BG = mol.bond_graph, depth=1)
    def test_14_butanediol(self):
        pass
    def test_cyclopentanone(self):
        pass
    def test_acetonitrile(self):
        pass
    def test_nitroethane(self):
        pass
    def test_12_dimethoxybenzene(self):
        pass
    def test_111_trifluoropropane(self):
        pass
    def test_methyloxirane(self):
        pass
    def test_13_dichloropropane(self):
        pass
    def test_pyrrolidine(self):
        pass
    def test_diethyl_malonate(self):
        pass
    def test_2_propenenitrile(self):
        pass
    def test_1_butanethiol(self):
        pass
    def test_2_propanethiol(self):
        pass
    def test_13_dioxolane(self):
        pass
    def test_ethylmethylsulfide(self):
        pass
    def test_2_hexanone(self):
        pass
    def test_112_trichloroethane(self):
        pass
    def test_1_octanol(self):
        pass
    def test_methyl_acetate(self):
        pass
    def test_dimethyl_disulfide(self):
        pass
    def test_acetophenone(self):
        pass
    def test_1_pentanol(self):
        pass
    def test_11_dichloroethane(self):
        pass
    def test_tert_butylamine(self):
        pass
    def test_2_aminoethanol(self):
        pass
    def test_2_heptanone(self):
        pass
    def test_methylnitroaniline(self):
        pass
    def test_propylene_carbonate(self):
        pass
    def test_dichloromethane(self):
        pass
    def test_pyridine(self):
        pass
    def test_pyrrole(self):
        pass
    def test_tetrahydrothiophene(self):
        pass
    def test_dibutyl_ether(self):
        pass
    def test_isopropylbenzene(self):
        pass
    def test_diisopropylamine(self):
        pass
    def test_fluorobenzene(self):
        pass
    def test_N_methylformamide(self):
        pass
    def test_thiophene(self):
        pass
    def test_246_trimethylpyridine(self):
        pass
    def test_dichlorofluoromethane(self):
        pass
    def test_acetone(self):
        pass
    def test_1_chlorobutane(self):
        pass
    def test_14_dichlorobutane(self):
        pass
    def test_formamide(self):
        pass
    def test_formic_acid(self):
        pass
    def test_benzyl_alcohol(self):
        pass
    def test_11_dichloroethene(self):
        pass
    def test_toluene(self):
        pass
    def test_chloride(self):
        pass
    def test_diethylene_glycol_dimethyl_ether(self):
        pass
    def test_acetamide(self):
        pass
    def test_quinoline(self):
        pass
    def test_1235_tetrafluorobenzene(self):
        pass
    def test_2_iodopropane(self):
        pass
    def test_2_methylpyridine(self):
        pass
    def test_morpholine(self):
        pass
    def test_t_butanol(self):
        pass
    def test_methyl_formate(self):
        pass
    def test_ethanethiol(self):
        pass
    def test_cyclohexane(self):
        pass
    def test_lithium(self):
        pass
    def test_dimethyldisulfide(self):
        pass
    def test_N_methylacetamide(self):
        pass
    def test_N_methylpyrrolidone(self):
        pass
    def test_1_butanol(self):
        pass
    def test_ethylene_carbonate(self):
        pass
    def test_3_methylphenol(self):
        pass
    def test_4_methylphenol(self):
        pass
    def test_sulfolane(self):
        pass
    def test_bromomethane(self):
        pass
    def test_methyl_methacrylate(self):
        pass
    def test_vinyl_acetate(self):
        pass
    def test_trifluoromethyl_benzene(self):
        pass
    def test_chloroethane(self):
        pass
    def test_2_methyl_2_butanol(self):
        pass
    def test_1_bromopropane(self):
        pass
    def test_gamma_butyrolactone(self):
        pass
    def test_1_cyclopropylpropane(self):
        pass
    def test_benzonitrile(self):
        pass
    def test_2_nitropropane(self):
        pass
    def test_triethyl_phosphate(self):
        pass
    def test_12_ethanedithiol(self):
        pass
    def test_2_methylphenol(self):
        pass
    def test_dimethyl_sulfide(self):
        pass
    def test_2_acetyloxyethyl_acetate(self):
        pass
    def test_12_dichloroethane(self):
        pass
    def test_methyltert_butylether(self):
        pass
    def test_4_methylpyridine(self):
        pass
    def test_styrene(self):
        pass
    def test_methyl_benzoate(self):
        pass
    def test_dimethoxymethane(self):
        pass
    def test_furan(self):
        pass
    def test_12_dibromopropane(self):
        pass
    def test_tbutanol(self):
        pass
    def test_pentanenitrile(self):
        pass
    def test_2_chloroethanol(self):
        pass
    def test_2_propylpyrrole(self):
        pass
    def test_methanol(self):
        pass
    def test_3_methylpyridine(self):
        pass
    def test_paraldehyde(self):
        pass
    def test_propyne(self):
        pass
    def test_nitrobenzene(self):
        pass
    def test_1_ethylpropylamine(self):
        pass
    def test_dimethylformamide(self):
        pass
    def test_dimethylsulfide(self):
        pass
    def test_24_dimethyl_3_pentanone(self):
        pass
    def test_isobutane(self):
        pass
    def test_diisopropyl_ether(self):
        pass
    def test_12_difluorobenzene(self):
        pass
    def test_1_nitropropane(self):
        pass
    def test_pyrimidine(self):
        pass
    def test_methanethiol(self):
        pass
    def test_ethyl_vinyl_ether(self):
        pass
    def test_nitromethane(self):
        pass
    def test_1_chloronaphthalene(self):
        pass
    def test_NN_dimethylformamide(self):
        pass
    def test_n_butylamine(self):
        pass
    def test_dimethyl_sulfoxide(self):
        pass
    def test_dibromomethane(self):
        pass
    def test_trichloromethane(self):
        pass
    def test_propane(self):
        pass
    def test_2_methyl_2_propanol(self):
        pass
    def test_12_ethanediamine(self):
        pass
    def test_1234_tetrafluorobenzene(self):
        pass
    def test_E_hex_2_ene(self):
        pass
    def test_benzene(self):
        pass
    def test_2_methoxypropane(self):
        pass
    def test_3_pentanol(self):
        pass
    def test_diethylene_glycol(self):
        pass
    def test_methane(self):
        pass
    def test_propionic_acid(self):
        pass
    def test_1_bromobutane(self):
        pass
    def test_12_dibromoethane(self):
        pass
    def test_124_trimethylbenzene(self):
        pass
    def test_ethanol(self):
        pass
    def test_ethyl_acetate(self):
        pass
    def test_propene(self):
        pass
    def test_2_chloroaniline(self):
        pass
    def test_dimethylether(self):
        pass
    def test_1122_tetrachloroethane(self):
        pass
    def test_phenol(self):
        pass
    def test_acetic_anhydride(self):
        pass
    def test_ethyl_propanoate(self):
        pass
    def test_propanethiol(self):
        pass
    def test_propylamine(self):
        pass
    def test_123_propanetriol(self):
        pass
    def test_cyclohexylamine(self):
        pass
    def test_diethylamine(self):
        pass
    def test_cyclohexanone(self):
        pass
    def test_chlorobenzene(self):
        pass
    def test_benzenethiol(self):
        pass
    def test_triethylamine(self):
        pass
    def test_isoquinoline(self):
        pass
    def test_propanenitrile(self):
        pass
    def test_pentachloroethane(self):
        pass
    def test_15_pentanediol(self):
        pass
    def test_diethyl_sulfide(self):
        pass
    def test_dibutylamine(self):
        pass
    def test_ethylbenzene(self):
        pass
    def test_NN_dimethylacetamide(self):
        pass
    def test_24_pentanedione(self):
        pass
    def test_tetrahydrofuran(self):
        pass
    def test_diphenyl_ether(self):
        pass
    def test_cyclopropyl_methyl_ketone(self):
        pass
    def test_benzaldehyde(self):
        pass
    def test_neopentane(self):
        pass
    def test_isopropylamine(self):
        pass
    def test_4_acetyloxybutyl_acetate(self):
        pass
    def test_biphenyl(self):
        pass
    def test_isopropanol(self):
        pass
    def test_formaldehyde(self):
        pass
    def test_diethyl_carbonate(self):
        pass
    def test_ethane(self):
        pass
    def test_13_difluorobenzene(self):
        pass
    def test_anisole(self):
        pass
    def test_methyl_salicylate(self):
        pass
    def test_acetate(self):
        pass
    def test_26_dimethyl_4_heptanone(self):
        pass
    def test_diethanolamine(self):
        pass
    def test_bromoethane(self):
        pass
    def test_dimethylcarbonate(self):
        pass