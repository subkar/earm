import pysb.macros as macros
from pysb import *

site_name = 'b'

def declare_monomers():
    Monomer('tBid', ['b'])
    Monomer('Bax', ['b', 'state'], {'state':['C', 'A']})
    Monomer('Bcl2', ['b'])
    Monomer('Bad', ['b'])
    Monomer('Pore')

def catalyze_one_step_reversible(enz, sub, prod, klist):
    kcat, krev = klist

    Rule('catalyze1',
         enz({site_name:None}) + sub({site_name:None}) >>
         enz({site_name:None}) + prod({site_name:None}),
         Parameter('catalyze1_kcat', kcat))

    Rule('catalyze1_rev',
         prod({site_name:None}) >> sub({site_name:None}),
         Parameter('cat1_rev_krev', krev))

def bind(a, b, klist):
    return macros.bind(a, site_name, b, site_name, klist)

def bind_table(table):
    return macros.bind_table(table, site_name, site_name)

def pore_assembly(monomer, size, pore, klist):
    #Rule
    pass

def displace_reversibly(target, lig1, lig2, klist):
    kf, kr = klist

    r = Rule('displacement',
         target({site_name:1}) % lig1({site_name:1}) + lig2({site_name:None}) <>
         target({site_name:1}) % lig2({site_name:1}) + lig1({site_name:None}),
         Parameter('displace_kf'), Parameter('displace_kr'))