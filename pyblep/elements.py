"""
Conventions:
    class in CamelCase
    fields in lower_case
    units should use SI besides energy in [eV], charge in [e]
"""

from .element import Element


class Drift(Element):
    """Drift in expanded form"""
    _description = [
        ("length", "m", "Length of the drift"),
    ]


class DriftExact(Drift):
    """Drift in exact form"""


class Multipole(Element):
    _description = [
        ('knl', 'm^-n', "Normalized integrated strength of normal components"),
        ('ksl', 'm^-n', "Normalized integrated strength of skew components"),
        ('hxl', 'rad', "Rotation angle of the reference trajectory in the horizzontal plane"),
        ('hyl', 'rad', "Rotation angle of the reference trajectory in the vertical plane"),
        ('length', 'm', "Length of the orginating thick multipole"),
    ]


class Cavity(Element):
    _description = [
        ('voltage', 'V', "Integrated energy change"),
        ('frequency', 'Hz', "Frequency of the cavity"),
        ('lag', 'degree', "Delay in the cavity sin(lag - w tau)"),
    ]


class XYShift(Element):
    _description = [
        ('dx', 'm', 'Horizontal shift'),
        ('dy', 'm', 'Vertical shift')
    ]


class SRotation(Element):
    _description = [
        ('angle', '', 'Rotation angle'),
    ]


class Line(Element):
    _description = [
        ('elements', '', 'Line elements'),
        ('element_names', '', 'Element names'),
    ]


class BeamBeam4D(Element):
    """Interaction with a transverse-Gaussian strong beam (4D modelling)."""
    _description = [
        ('charge', 'e', 'Charge of the interacting distribution (strong beam)'),
        ('sigma_x', 'm', 'Horizontal size of the strong beam (r.m.s.)'),
        ('sigma_y', 'm', 'Vertical size of the strong beam (r.m.s.)'),
        ('beta_r', '', 'Relativistic beta of the stron beam'),
        ('x_bb', 'm', 'H. position of the strong beam w.r.t. the reference trajectory'),
        ('y_bb', 'm', 'V. position of the strong beam w.r.t. the reference trajectory'),
        ('d_px', '', 'H. kick subtracted after the interaction.'),
        ('d_py', '', 'V. kick subtracted after the interaction.')
    ]


class BeamBeam6D(Element):
    """Interaction with a transverse-Gaussian strong beam (6D modelling).

    http://cds.cern.ch/record/2306400
    """
    _description = [
        ('phi', 'rad', 'Crossing angle (>0 weak beam increases x in the direction motion)'),
        ('alpha', 'rad', 'Crossing plane tilt angle (>0 x tends to y)'),
        ('x_bb_co', 'm', 'H. position of the strong beam w.r.t. the closed orbit'),
        ('y_bb_co', 'm', 'V. position of the strong beam w.r.t. the closed orbit'),
        ('charge_slices', 'qe', 'Charge of the interacting slices (strong beam)'),
        ('zeta_slices', 'm',
         'Longitudinal position of the interacting slices (>0 head of the strong).'),
        ('sigma_11', 'm^2', 'Sigma_11 element of the sigma matrix of the strong beam'),
        ('sigma_12', 'm', 'Sigma_12 element of the sigma matrix of the strong beam'),
        ('sigma_13', 'm^2', 'Sigma_13 element of the sigma matrix of the strong beam'),
        ('sigma_14', 'm', 'Sigma_14 element of the sigma matrix of the strong beam'),
        ('sigma_22', '', 'Sigma_22 element of the sigma matrix of the strong beam'),
        ('sigma_23', 'm', 'Sigma_23 element of the sigma matrix of the strong beam'),
        ('sigma_24', '', 'Sigma_24 element of the sigma matrix of the strong beam'),
        ('sigma_33', 'm^2', 'Sigma_33 element of the sigma matrix of the strong beam'),
        ('sigma_34', 'm', 'Sigma_34 element of the sigma matrix of the strong beam'),
        ('sigma_44', '', 'Sigma_44 element of the sigma matrix of the strong beam'),
        ('x_co', 'm', 'x coordinate the closed orbit (weak beam).'),
        ('px_co', '', 'px coordinate the closed orbit (weak beam).'),
        ('y_co', 'm', 'y coordinate the closed orbit (weaek beam).'),
        ('py_co', '', 'py coordinate the closed orbit (weaek beam).'),
        ('zeta_co', 'm', 'zeta coordinate the closed orbit (weaek beam).'),
        ('delta_co', '', 'delta coordinate the closed orbit (weaek beam).'),
        ('d_x', 'm', 'Quantity subtracted from x after the interaction.'),
        ('d_px', '', 'Quantity subtracted from px after the interaction.'),
        ('d_y', 'm', 'Quantity subtracted from y after the interaction.'),
        ('d_py', '', 'Quantity subtracted from py after the interaction.'),
        ('d_zeta', 'm', 'Quantity subtracted from sigma after the interaction.'),
        ('d_delta', '', 'Quantity subtracted from delta after the interaction.')
    ]


class Particle(Element):
    _description = [
        ('mass0', 'eV', 'Reference mass'),
        ('p0c', 'eV', 'Reference momentum'),
        ('beta0', '', 'Reference relativistic beta'),
        ('charge0', 'e', 'Reference charge'),
        ('x', 'm', 'Horizzontal position'),
        ('px', '', 'Horizzontal normalized momentum Px/P0 mass0/mass'),
        ('y', 'm', 'Vertical position'),
        ('py', '', 'Vertical normalized momentum Py/P0 mass0/mass'),
        ('zeta', 'm', 'Compensated longitudinal delay z= beta / beta0 s - beta c t'),
        ('delta', '', 'Cinematic deviation betagamma / beta0gamma0 - 1'),
        ('rpp', '', 'ratio beta0gamma0/betagamma'),
        ('rvv', '', 'ratio beta/beta0'),
        ('rmass', '', 'ratio mass'),
        ('rcharge', '', 'q/q0'),
        ('chi', '', 'q/q0 mass0/mass'),
        ('partid', '', 'Indentification'),
        ('islost', '', 'Negative if particle is invalid or lost')
    ]
