"""
Standard definitions of parameters and their default values.
"""
import glob 
import numpy as np
import os

#  /* **********************   Model parameters   ************************** */


#-- WD
defs  = [dict(qualifier="name" ,description="Common name of the binary",    repr="%s",cast_type=str,value="mybinary",frame=["wd"],alias=['phoebe_name'],context='root'),
         dict(qualifier="model",description="Morphological constraints",    repr="%s",choices=["X-ray binary",
                                                                                                 "Unconstrained binary system",
                                                                                                 "Overcontact binary of the W UMa type",
                                                                                                 "Detached binary",
                                                                                                 "Overcontact binary not in thermal contact",
                                                                                                 "Semi-detached binary, primary star fills Roche lobe",
                                                                                                 "Semi-detached binary, secondary star fills Roche lobe",
                                                                                                 "Double contact binary"],
                                                                                                 cast_type='indexf',value="Unconstrained binary system",
                                                                                                 frame=["wd"],alias=['mode'],context='root')]                                                                                                 

#  /* **********************   System parameters   ************************* */

#-- WD
defs += [dict(qualifier="hjd0",  description="Origin of time",                            repr= "%f", llim=-1E10, ulim=  1E10, step= 0.0001, adjust=False, cast_type=float, unit='HJD',  value= 55124.89703,frame=["wd"],alias=['T0','phoebe_hjd0'],context='root'),
         dict(qualifier="period",description="Orbital period",                            repr= "%f", llim=  0.0, ulim=  1E10, step= 0.0001, adjust=False, cast_type=float, unit='d',    value= 22.1891087 ,frame=["wd"],alias=['p','phoebe_period'],context='root'),
         dict(qualifier="dpdt",  description="First time derivative of period",           repr= "%f", llim= -1.0, ulim=   1.0, step=   1E-6, adjust=False, cast_type=float, unit='d/d',  value= 0.0        ,frame=["wd"],alias=['phoebe_dpdt'],context='root'),
         dict(qualifier="pshift",description="Phase shift",                               repr= "%f",     llim= -0.5, ulim=   0.5, step=   0.01, adjust=False, cast_type=float,              value= 0.0776     ,frame=["wd"],alias=['phoebe_pshift'],context='root'),
         dict(qualifier="sma",   description="Semi-major axis",                           repr= "%f",     llim=  0.0, ulim=  1E10, step=   0.01, adjust=False, cast_type=float, unit='Rsol', value=11.0104     ,frame=["wd"],alias=['a','phoebe_sma'],context=['root'],prior=dict(distribution='uniform',lower=0,upper=1e10)),
         dict(qualifier="rm",    description="Mass ratio (secondary over primary)",       repr= "%f",     llim=  0.0, ulim=  1E10, step=   0.01, adjust=False, cast_type=float,              value=0.89747     ,frame=["wd"],alias=['q','phoebe_rm'],context='root'),
         dict(qualifier="incl",  description="Inclination angle",                               repr= "%f",     llim=  0.0, ulim= 180.0, step=   0.01, adjust=False, cast_type=float, unit='deg',  value=87.866      ,frame=["wd"],alias=['i','phoebe_incl'],context=['root'],prior=dict(distribution='uniform',lower=0,upper=180)),
         dict(qualifier="vga",   description="Center-of-mass velocity",                   repr= "%f",     llim= -1E3, ulim=   1E3, step=    1.0, adjust=False, cast_type=float, unit='km/s', value= 0.0        ,frame=["wd"],alias=['gamma','phoebe_vga'],context='root'),
         dict(qualifier='ecc'  , description='Eccentricity'                             , repr= '%f',     llim=  0.0, ulim=   0.99,step=   0.01, adjust=False, cast_type=float,              value=0.28319     ,frame=["wd"],alias=['e','phoebe_ecc'],context='root'),
         dict(qualifier='omega', description='Initial argument of periastron for star 1', repr= '%f',     llim=  0.0, ulim=   6.28,step=   0.01, adjust=False, cast_type=float, unit='rad',  value=5.696919    ,frame=["wd"],alias=['perr0'],context='root'),
         dict(qualifier='domegadt',description='First time derivative of periastron'    , repr='%f',      llim=  0.0, ulim=    1.0,step=   0.01, adjust=False, cast_type=float, unit='rad/s',value=0,           frame=["wd"],alias=['dperdt'],context='root')]

#  /* ********************   Component parameters   ************************ */

defs += [dict(qualifier='f1',    description="Primary star synchronicity parameter"      ,repr='%f',llim=  0.0, ulim=   10.0,step=   0.01, adjust=False,cast_type=float,value=1.,frame=["wd"],alias=['phoebe_f1'],context='root'), 
         dict(qualifier='f2',    description="Secondary star synchronicity parameter"    ,repr='%f',llim=  0.0, ulim=   10.0,step=   0.01, adjust=False,cast_type=float,value=1.,frame=["wd"],alias=['phoebe_f2'],context='root'), 
         dict(qualifier='teff1', description="Primary star effective temperature"        ,repr='%f',llim=  0.2 ,ulim=      5,step=   0.01, adjust=False,cast_type=float,value=0.8105,unit='10000K',frame=["wd"],alias=[],context='root'),
         dict(qualifier='teff2', description="Secondary star effective temperature"      ,repr='%f',llim=  0.2 ,ulim=      5,step=   0.01, adjust=False,cast_type=float,value=0.7299,unit='10000K',frame=["wd"],alias=[],context='root'),
         dict(qualifier='pot1',  description="Primary star surface potential"            ,repr='%f',llim=  0.0, ulim=  100.0,step=   0.01, adjust=False,cast_type=float,value=7.34050,frame=["wd"],alias=['phoebe_pot1'],context='root'),
         dict(qualifier='pot2',  description="Secondary star surface potential"          ,repr='%f',llim=  0.0, ulim=  100.0,step=   0.01, adjust=False,cast_type=float,value=7.58697,frame=["wd"],alias=['phoebe_pot2'],context='root'),
         dict(qualifier='met1',  description="Primary star metallicity"                  ,repr='%f',llim=  0.0, ulim=    1.0,step=   0.01, adjust=False,cast_type=float,value=0.0,frame=["wd"],alias=['phoebe_met1'],context='root'),
         dict(qualifier='met2',  description="Secondary star metallicity"                ,repr='%f',llim=  0.0, ulim=    1.0,step=   0.01, adjust=False,cast_type=float,value=0.0,frame=["wd"],alias=['phoebe_met2'],context='root'),
         dict(qualifier='alb1',  description="Primary star surface albedo"               ,repr='%f',llim=  0.0, ulim=    1.5,step=   0.01, adjust=False,cast_type=float,value=1.0,frame=["wd"],alias=['phoebe_alb1'],context='root'),
         dict(qualifier='alb2',  description="Secondary star surface albedo"             ,repr='%f',llim=  0.0, ulim=    1.5,step=   0.01, adjust=False,cast_type=float,value=0.864,frame=["wd"],alias=['phoebe_alb2'],context='root'),
         dict(qualifier='grb1',  description="Primary star gravity brightening"          ,repr='%f',llim=  0.0, ulim=    1.5,step=   0.01, adjust=False,cast_type=float,value=0.964,frame=["wd"],alias=['phoebe_grb1','gr1'],context='root'),
         dict(qualifier='grb2',  description="Secondary star gravity brightening"        ,repr='%f',llim=  0.0, ulim=    1.5,step=   0.01, adjust=False,cast_type=float,value=0.809,frame=["wd"],alias=['phoebe_grb2','gr2'],context='root')]

#  /* ****************   Light/RV curve dependent parameters   ************ */

defs += [dict(qualifier='filter',description='Filter name',choices=['STROMGREN.U','stromgren.v','stromgren.b','stromgren.y',
                                                                    'johnson.U','johnson.B','JOHNSON.V','johnson.R','johnson.I','johnson.J','johnson.K','johnson.L','johnson.M','johnson.N',
                                                                    'bessell.RC','bessell.IC',
                                                                    'kallrath.230','kallrath.250','kallrath.270','kallrath.290','kallrath.310','kallrath.330',
                                                                    'tycho.B','tycho.V','hipparcos.hp','COROT.EXO','COROT.SIS','JOHNSON.H',
                                                                    'GENEVA.U','GENEVA.B','GENEVA.B1','GENEVA.B2','GENEVA.V','GENEVA.V1','GENEVA.G',
                                                                    'KEPLER.V','SDSS.U'],repr='%s',cast_type='indexf',value='johnson.V',frame=["wd"],context='lc',alias=['phoebe_lc_filter']),
         dict(qualifier="indep_type",    description="Independent modeling variable",repr="%s",choices=['time (hjd)','phase'],cast_type='indexf',value="phase",frame=["wd"],alias=['jdphs','phoebe_lc_indep'],context='lc'),
         dict(qualifier="indep",         description="Time/phase template or time/phase observations",repr="%s",cast_type=np.array,value=np.arange(0,1.005,0.01),frame=["wd"],context='lc'),
         dict(qualifier="ld_model", description="Limb darkening model",                      choices=['linear','logarithmic','square root law'],repr= "%s",cast_type='indexf',value="logarithmic",frame=["wd"],alias=['ld','phoebe_ld_model'],context='root'),
         dict(qualifier="ld_xbol1", description="Primary star bolometric LD coefficient x",  repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.512,frame=["wd"],alias=['phoebe_ld_xbol1'],context='root'),
         dict(qualifier="ld_ybol1", description="Primary star bolometric LD coefficient y",  repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.0,frame=["wd"],alias=['phoebe_ld_ybol1'],context='root'),
         dict(qualifier="ld_xbol2", description="Secondary star bolometric LD coefficient x",repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.549,frame=["wd"],alias=['phoebe_ld_xbol2'],context='root'),
         dict(qualifier="ld_ybol2", description="Secondary star bolometric LD coefficient y",repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.0,frame=["wd"],alias=['phoebe_ld_ybol2'],context='root'),
         dict(qualifier="ld_lcx1",  description="Primary star passband LD coefficient x",    repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.467,frame=["wd",'jktebop'],alias=['x1a','phoebe_ld_lcx1'],context='lc'),
         dict(qualifier="ld_lcx2",  description="Secondary star passband LD coefficient x",  repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.502,frame=["wd",'jktebop'],alias=['x2a','phoebe_ld_lcx2'],context='lc'),
         dict(qualifier="ld_lcy1",  description="Primary star passband LD coefficient y",    repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.0,frame=["wd",'jktebop'],alias=['y1a','phoebe_ld_lcy1'],context='lc'),
         dict(qualifier="ld_lcy2",  description="Secondary star passband LD coefficient y",  repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.0,frame=["wd",'jktebop'],alias=['y2a','phoebe_ld_lcy2'],context='lc'),
         dict(qualifier="ld_rvx1",  description="Primary RV passband LD coefficient x",      repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.5,frame=["wd"],context='rv'),
         dict(qualifier="ld_rvx2",  description="Secondary RV passband LD coefficient x",    repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.5,frame=["wd"],context='rv'),
         dict(qualifier="ld_rvy1",  description="Primary RV passband LD coefficient y",      repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.5,frame=["wd"],context='rv'),
         dict(qualifier="ld_rvy2",  description="Secondary RV passband LD coefficient y",    repr= "%f",llim=-10.0, ulim=10.0,step= 0.01,cast_type=float,value=0.5,frame=["wd"],context='rv'),
         dict(qualifier="hla" ,     description="LC primary passband luminosity"  ,repr='%f',cast_type=float,llim=0,ulim=1e10,step=0.01,value=8.11061,frame=["wd"],alias=['phoebe_hla'],context='lc'),
         dict(qualifier="cla" ,     description="LC secondary passband luminosity",repr='%f',cast_type=float,llim=0,ulim=1e10,step=0.01,value=4.43580,frame=["wd"],alias=['phoebe_cla'],context='lc'),
         dict(qualifier="opsf",     description="Opacity frequency function",      repr="%f",cast_type=float,llim=0.0,ulim=1E10,step=0.01,value=0.0,frame=["wd"],alias=['phoebe_opsf'],context='lc'),
         dict(qualifier="el3",      description="Third light contribution",repr="%f",cast_type=float,llim=0.0,ulim=1E10,step=0.01,value=0.0,frame=["wd"],alias=['phoebe_el3'],context='lc'),
         dict(qualifier='el3_units',description="Units of third light",choices=['total light','percentage'],repr='%s',cast_type='indexf',value='total light',frame=["wd"],alias=['l3perc','phoebe_el3_units'],context='lc'),
         dict(qualifier='phnorm',   description='Phase of normalisation',repr='%8.6f',cast_type=float,value=0.25,frame=["wd"],context='lc'),
         dict(qualifier='jdstrt',   description='Start Julian date',    repr='%14.6f',cast_type=float,value=0,frame=["wd"],context='lc'),
         dict(qualifier='jdend',    description='End Julian date',      repr='%14.6f',cast_type=float,value=1.0,frame=["wd"],context='lc'),
         dict(qualifier='jdinc',    description='Increment Julian date',repr='%14.6f',cast_type=float,value=0.1,frame=["wd"],context='lc'),
         dict(qualifier='phstrt',   description='Start Phase'          ,repr='%8.6f',cast_type=float,value=0,frame=["wd"],context='lc'),
         dict(qualifier='phend',    description='End phase',            repr='%8.6f',cast_type=float,value=1,frame=["wd"],context='lc'),
         dict(qualifier='phinc',    description='Increment phase',      repr='%8.6f',cast_type=float,value=0.01,frame="wd",context='lc'),
         #dict(qualifier='data',     description='Filename containing the data',cast_type='filename2data',value=None,frame=['main',"wd"],context='lc'),
         ]

#  /* *********   Values specifically for Wilson-Devinney   **************** */

defs += [dict(qualifier='mpage', description="Output type of the WD code", choices=['lightcurve','rvcurve','lineprofile','starradii','image'],repr="%s",cast_type='indexf',value='lightcurve',frame=["wd"],context='root'),
         dict(qualifier='mref',  description="Reflection treatment",       choices=['simple','detailed'],                                     repr="%s",cast_type='indexf',value='simple',frame=["wd"],context='root'),
         dict(qualifier='nref',  description='Number of reflections',      repr='%d',cast_type=int,value=2,frame=["wd"],alias=['phoebe_reffect_reflections'],context='root'),
         dict(qualifier='icor1', description='Turn on prox and ecl fx on prim RV',  repr='%d',cast_type=int,value=True,frame=["wd"],alias=['phoebe_proximity_rv1_switch'],context='root'),
         dict(qualifier='icor2', description='Turn on prox and ecl fx on secn RV',repr='%d',cast_type=int,value=True,frame=["wd"],alias=['phoebe_proximity_rv2_switch'],context='root'),
         dict(qualifier='stdev', description='Synthetic noise standard deviation',repr='%f',cast_type=float,value=0,frame=["wd"],context='root'),
         dict(qualifier='noise', description='Noise scaling',              choices=['proportional','square root','independent'],repr='%s',cast_type='indexf',value='independent',frame=["wd"],context='root'),
         dict(qualifier='seed',  description='Seed for random generator', repr='%f',cast_type=float,value=100000001.,frame=["wd"],alias=['phoebe_synscatter_seed'],context='root'),
         dict(qualifier='ipb',   description='Compute second stars Luminosity'                ,repr='%s',cast_type=int,value=False,frame=["wd"],context='root'),
         dict(qualifier='ifat1', description='Atmosphere approximation primary'               ,repr='%s',choices=['blackbody','kurucz'],cast_type='index',value='kurucz',frame=["wd"],alias=['phoebe_atm1_switch'],context='root'),
         dict(qualifier='ifat2', description='Atmosphere approximation secondary'             ,repr='%s',choices=['blackbody','kurucz'],cast_type='index',value='kurucz',frame=["wd"],alias=['phoebe_atm2_switch'],context='root'),
         dict(qualifier='n1',    description='Grid size primary'                              ,repr='%d',cast_type=int,value=70,frame=["wd"],alias=['phoebe_grid_finesize1'],context='root'),
         dict(qualifier='n2',    description='Grid size secondary'                            ,repr='%d',cast_type=int,value=70,frame=["wd"],alias=['phoebe_grid_finesize2'],context='root'),
         dict(qualifier='the',   description='Semi-duration of primary eclipse in phase units',repr='%f',cast_type=float,value=0,frame=["wd"],context='root'),
         dict(qualifier='vunit', description='Unit of radial velocity (km/s)',repr='%f',cast_type=float,value=1.,frame=["wd"],context='rv'),
         dict(qualifier='mzero',  description='Zeropoint mag (vert shift of lc)',repr='%f',cast_type=float,value=0,frame=["wd"],context='root'),
         dict(qualifier='factor', description='Zeropoint flux (vert shift of lc)',repr='%f',cast_type=float,value=1.,frame=["wd"],context='root'),
         dict(qualifier='wla',    description='Reference wavelength (in microns)',repr='%f',cast_type=float,value=0.59200,frame=["wd"],context='root'),
         dict(qualifier='atmtab', description='Atmosphere table',                        repr='%s', cast_type=str, value='phoebe_atmcof.dat',      frame=["wd"],context='root'),
         dict(qualifier='plttab', description='Planck table',                            repr='%s', cast_type=str, value='phoebe_atmcofplanck.dat',frame=["wd"],context='root')
         ]

#  /* *********************   SPOT PARAMETERS      ************************* */

defs += [dict(qualifier='ifsmv1', description='Spots on star 1 co-rotate with the star', repr='%s', cast_type=int,   value=0,     frame=["wd"],alias=['phoebe_spots_corotate1'],context='root'),
         dict(qualifier='ifsmv2', description='Spots on star 2 co-rotate with the star', repr='%s', cast_type=int,   value=0,     frame=["wd"],alias=['phoebe_spots_corotate2'],context='root'),
         dict(qualifier='xlat1',  description='Primary spots latitudes'                , repr='%s', cast_type='list',value=[300.],frame=["wd"],alias=['wd_spots_lat1'],context='root'),
         dict(qualifier='xlong1', description='Primary spots longitudes'               , repr='%s', cast_type='list',value=[0.],  frame=["wd"],alias=['wd_spots_long1'],context='root'),
         dict(qualifier='radsp1', description='Primary spots radii'                    , repr='%s', cast_type='list',value=[1.],  frame=["wd"],alias=['wd_spots_rad1'],context='root'),
         dict(qualifier='tempsp1',description='Primary spots temperatures'             , repr='%s', cast_type='list',value=[1.],  frame=["wd"],alias=['wd_spots_temp1'],context='root'),
         dict(qualifier='xlat2',  description='Secondary spots latitudes'              , repr='%s', cast_type='list',value=[300.],frame=["wd"],alias=['wd_spots_lat2'],context='root'),
         dict(qualifier='xlong2', description='Secondary spots longitudes'             , repr='%s', cast_type='list',value=[0.],  frame=["wd"],alias=['wd_spots_long2'],context='root'),
         dict(qualifier='radsp2', description='Secondary spots radii'                  , repr='%s', cast_type='list',value=[1.],  frame=["wd"],alias=['wd_spots_rad2'],context='root'),
         dict(qualifier='tempsp2',description='Secondary spots temperatures'           , repr='%s', cast_type='list',value=[1.],  frame=["wd"],alias=['wd_spots_temp2'],context='root'),
         ]
                  

# /* **********************   Values specifically for spheres *************** */

defs +=[dict(qualifier='teff', description="Effective temperature"        ,repr='%.0f',llim=  0,ulim=  1e20,step=   100., adjust=False,cast_type=float,value=5777.,unit='K',frame=["phoebe"],alias=[],context='star'),
        dict(qualifier='radius', description='Radius',repr='%f', cast_type=float,   value=1., unit='Rsol', adjust=False,frame=["phoebe"],context='star'),
        dict(qualifier='mass', description='Stellar mass',repr='%g',cast_type=float,value=1., unit='Msol', adjust=False,frame=["phoebe"],context='star'),
        dict(qualifier='atm',    description='Atmosphere model',repr='%s',cast_type=str,value='blackbody',frame=["phoebe"],context=['lcdep','rvdep','ifdep','spdep']),
        dict(qualifier='atm',    description='Bolometric Atmosphere model',repr='%s',cast_type=str,value='blackbody',frame=["phoebe"],context=['star','component','accretion_disk']),
        dict(qualifier='rotperiod', description='Polar rotation period',repr='%f',cast_type=float,value=22.,adjust=False,frame=["phoebe"],unit='d',context='star'),
        dict(qualifier='diffrot', description='(Eq - Polar) rotation period (<0 is solar-like)',repr='%f',cast_type=float,value=0.,adjust=False,frame=["phoebe"],unit='d',context='star'),
        dict(qualifier='gravb',  description='Bolometric gravity brightening',repr='%f',cast_type=float,value=1.,llim=0,ulim=1.,step=0.05,adjust=False,alias=['grb'],frame=["phoebe"],context='star'),
        dict(qualifier='gravblaw',description='Gravity brightening law',repr='%s',cast_type='choose',choices=['zeipel','espinosa'],value='zeipel',frame=['phoebe'],context='star'),
        dict(qualifier='incl',   description='Inclination angle',unit='deg',repr='%f',llim=0,ulim=180,step=0.01,adjust=False,cast_type=float,value=90.,frame=["phoebe"],context='star'),
        dict(qualifier='long',   description='Orientation on the sky', repr='%f',llim=  0.0, ulim=   360,step=   0.01, adjust=False, cast_type=float, unit='deg',  value=0.,frame=["phoebe"],context='star'),
        dict(qualifier='distance',description='Distance to the star',repr='%f',cast_type=float,value=10.,adjust=False,unit='pc',frame=['phoebe'],context='star'),
        dict(qualifier='shape', description='Shape of surface',repr='%s',cast_type='choose',choices=['equipot','sphere'],value='equipot',frame=["phoebe"],context='star'),
        ]

#  /* ********************* PHOEBE ********************************* */
#   BINARY CONTEXT
defs += [dict(qualifier='dpdt',   description='Period change',unit='s/yr',repr='%f',llim=-10,ulim=10,step=1e-5,adjust=False,cast_type=float,value=0,frame=["phoebe"],context='orbit'),
         dict(qualifier='dperdt', description='Periastron change',unit='deg/yr',repr='%f',llim=-10,ulim=10,step=1e-5,adjust=False,cast_type=float,value=0,frame=["phoebe"],context='orbit'),
         dict(qualifier='ecc',    description='Eccentricity',repr='%f',llim=0,ulim=1.,step=0.01,adjust=False,cast_type=float,value=0.,frame=["phoebe"],context='orbit'),
         dict(qualifier='t0',     description='Zeropoint date',unit='JD',repr='%f',llim=0,ulim=2e10,step=0.001,adjust=False,cast_type=float,value=0.,alias=['hjd0'],frame=["phoebe"],context='orbit'),
         dict(qualifier='incl',   description='Inclination angle',unit='deg',repr='%f',llim=0,ulim=180,step=0.01,adjust=False,cast_type=float,value=90.,frame=["phoebe"],context='orbit'),
         dict(qualifier='label',  description='Name of the system',repr='%s',cast_type=str,value='',frame=["phoebe","wd"],context=['orbit','root']),
         dict(qualifier='period', description='Period of the system',repr='%f',unit='d',llim=0,ulim=1e6,step=0.01,adjust=False,cast_type=float,value=10.,frame=["phoebe"],context='orbit'),
         dict(qualifier='per0',   description='Periastron',repr='%f',unit='deg',llim=0,ulim=360,step=0.01,adjust=False,cast_type=float,value=90.,frame=["phoebe"],context='orbit'),
         dict(qualifier='phshift',description='Phase shift',repr='%f',llim=-1,ulim=+1,step=0.001,adjust=False,cast_type=float,value=0,frame=["phoebe"],context='orbit'),
         dict(qualifier='q',      description='Mass ratio',repr='%f',llim=0,ulim=1e6,step=0.0001,adjust=False,cast_type=float,value=1.,alias=['rm'],frame=["phoebe"],context='orbit'),
         dict(qualifier='vgamma', description='Systemic velocity',repr='%f',llim=-1e6,ulim=1e6,step=0.1,adjust=False,cast_type=float,value=0.,unit='km/s',alias=['vga'],frame=["phoebe"],context='orbit'),
         dict(qualifier='sma',    description='Semi major axis',unit='Rsol',repr='%f',llim=0,ulim=1e10,step=0.0001,adjust=False,value=0.1,cast_type=float,frame=["phoebe"],context='orbit'),
         dict(qualifier='long_an',   description='Longitude of ascending node', repr='%f',llim=  0.0, ulim=   360,step=   0.01, adjust=False, cast_type=float, unit='deg',  value=0.,frame=["phoebe"],context='orbit'),
         dict(qualifier='c1label', description='ParameterSet connected to the primary component',repr='%s',value=None,frame=["phoebe"],context='orbit'),
         dict(qualifier='c2label', description='ParameterSet connected to the secondary component',repr='%s',value=None,frame=["phoebe"],context='orbit'),
         ]

#    BODY CONTEXT
defs += [dict(qualifier='alb',    description='Bolometric albedo (alb heating, 1-alb reflected)',          repr='%f',cast_type=float,value=1.,llim=0,ulim=1,step=0.05,adjust=False,frame=["phoebe"],context=['component','star','accretion_disk']),
         dict(qualifier='redist',description='Global redist par (1-redist) local heating, redist global heating',          repr='%f',cast_type=float,value=0.,llim=0,ulim=1,step=0.05,adjust=False,frame=["phoebe"],context=['component','star','accretion_disk']),
         dict(qualifier='syncpar',description='Synchronicity parameter',repr='%f',cast_type=float,value=1.,llim=0,ulim=50.,step=0.01,adjust=False,alias=['f'],frame=["phoebe"],context='component'),
         dict(qualifier='gravb',  description='Bolometric gravity brightening',repr='%f',cast_type=float,value=1.0,llim=0,ulim=1,step=0.05,adjust=False,alias=['grb'],frame=["phoebe"],context='component'),
         dict(qualifier='pot',    description="Roche potential value",repr='%f',cast_type=float,value=4.75,llim=0,ulim=1e10,step=0.01,adjust=False,frame=["phoebe"],context='component'),
         dict(qualifier='teff',   description='Mean effective temperature',repr='%.0f',cast_type=float,unit='K',value=10000.,llim=0.,ulim=1e20,step=1,adjust=False,frame=["phoebe"],context='component'),         
         dict(qualifier='distance',description='Distance to the binary system',repr='%f',cast_type=float,value=10.,unit='pc',frame=['phoebe'],context='orbit'),
         dict(qualifier='irradiator',description='Treat body as irradiator of other objects',repr='%s',cast_type='make_bool',value=False,frame=['phoebe'],context=['component','star','accretion_disk']),
         dict(qualifier='abun',description='Metallicity',repr='%f',cast_type=float,value=0.,frame=['phoebe'],context=['component','star']),
         dict(qualifier='label',  description='Name of the body',repr='%s',cast_type=str,value='',frame=["phoebe"],context=['component','star','accretion_disk']),
        ]

#    INTERSTELLAR REDDENING
defs += [dict(qualifier='law',       description='Interstellar reddening law',repr='%s',cast_type='choose',choices=['chiar2006','fitzpatrick1999','fitzpatrick2004','donnel1994','cardelli1989','seaton1979'],value='fitzpatrick2004',frame=["phoebe"],context=['reddening:interstellar']),
         dict(qualifier='extinction',description='Passband extinction',repr='%f',cast_type=float,value=0,adjust=False,frame=["phoebe"],context=['reddening:interstellar']),
         dict(qualifier='bandpass',  description='Reference bandpass for extinction parameter',repr='%s',cast_type=str,value='JOHNSON.V',frame=["phoebe"],context=['reddening:interstellar']),
         dict(qualifier='Rv',        description='Total-to-selective extinction',repr='%f',cast_type=float,value=3.1,adjust=False,frame=["phoebe"],context=['reddening:interstellar']),
        ]

#    CIRCULAR SPOT CONTEXT
defs += [dict(qualifier='long',      description='Spot longitude at T0',           repr='%f',cast_type=float,value= 0.,unit='deg',llim=0,ulim=360.,step=1.0,adjust=False,frame=["phoebe"],context='circ_spot'),
         dict(qualifier='colat',     description='Spot colatitude at T0 (CHECK!)',            repr='%f',cast_type=float,value=90.,unit='deg',llim=0,ulim=180.,step=1.0,adjust=False,frame=["phoebe"],context='circ_spot'),
         dict(qualifier='angrad',    description='Spot angular radius',unit='deg',repr='%f',cast_type=float,value=5.,llim=0,ulim=90.,step=.01,adjust=False,frame=["phoebe"],context='circ_spot'),
         dict(qualifier='teffratio', description='Relative temperature difference in spot',repr='%f',cast_type=float,value=0.9,llim=0,ulim=10,step=0.05,adjust=False,frame=["phoebe"],context='circ_spot'),
         dict(qualifier='abunratio', description='Relative log(abundance) difference in spot',repr='%f',cast_type=float,value=0.0,llim=-5,ulim=5,step=0.01,adjust=False,frame=["phoebe"],context='circ_spot'),
         dict(qualifier='subdiv_num',description="Number of times to subdivide spot",repr='%d',cast_type=int,value=3,adjust=False,frame=['phoebe'],context='circ_spot'),
         dict(qualifier='t0',        description="Spot time zeropoint",repr='%f',cast_type=float,unit='JD',value=0.,adjust=False,frame=['phoebe'],context='circ_spot'),
        ]        

defs += [dict(qualifier='delta',    description='Stepsize for mesh generation via marching method',repr='%f',cast_type=float,value=0.2,frame=['phoebe'],context=['mesh:marching']),
         dict(qualifier='maxpoints',description='Maximum number of triangles for marching method',repr='%d',cast_type=int,value=20000,frame=['phoebe'],context=['mesh:marching']),
         dict(qualifier='gridsize', description='Number of meshpoints for WD style discretization',repr='%d',cast_type=int,value=90,frame=['phoebe'],context=['mesh:wd']),
         dict(qualifier='alg', description='Select type of algorithm',repr='%s',cast_type='choose',choices=['c','python'],value='python',frame=['phoebe'],context=['mesh:marching']),
         #dict(qualifier='style',    description='Discretization style',repr='%s',cast_type='choose',choices=['marching','cmarching','wd'],value='marching',frame=['phoebe'],context=['mesh'])
         ]        
        
#    DATA contexts
defs += [dict(qualifier='ld_func', description='Limb darkening model',repr='%s',cast_type='choose',choices=['uniform','linear','logarithmic', 'quadratic', 'square root','claret'],value='uniform',frame=["phoebe"],context=['lcdep','rvdep']),
         dict(qualifier='ld_func', description='Bolometric limb darkening model',repr='%s',cast_type='choose',choices=['uniform','linear','logarithmic', 'square root','claret'],value='uniform',frame=["phoebe"],context=['component','star']),
         dict(qualifier='ld_coeffs',       description='Limb darkening coefficients',repr='%s',value=[1.],cast_type='return_string_or_list',frame=["phoebe"],context=['lcdep']),
         dict(qualifier='ld_coeffs',       description='Bolometric limb darkening coefficients',repr='%s',value=[1.],cast_type='return_string_or_list',frame=["phoebe"],context=['component','star','accretion_disk']),
         dict(qualifier='passband', description='Photometric passband',repr='%s',cast_type='make_upper',value='JOHNSON.V',frame=["phoebe"],context='lcdep'),
         dict(qualifier='pblum',    description='Passband luminosity',repr='%f',cast_type=float,value=4.*np.pi,adjust=False,frame=["phoebe"],context=['lcdep','spdep','ifdep']),
         dict(qualifier='l3',       description='Third light',repr='%f',cast_type=float,value=0.,adjust=False,frame=["phoebe"],context=['lcdep','spdep','ifdep']),
         dict(qualifier='alb',      description='Passband albedo (1-Bond), alb=1 is no reflection',          repr='%f',cast_type=float,value=1.,llim=0,ulim=1,step=0.05,adjust=False,frame=["phoebe"],context=['lcdep','rvdep','ifdep','spdep']),
         dict(qualifier='method',   description='Method for calculation of total intensity',repr='%s',cast_type='choose',choices=['analytical','numerical'],value='numerical',frame=["phoebe"],context='lcdep'),
         dict(qualifier='label',    description='Name of the observable',repr='%s',cast_type=str,value='',frame=["phoebe","wd"],context=['lc','rv','puls','circ_orbit']),
         dict(qualifier='ref',      description='Name of the observable',repr='%s',cast_type=str,value='',frame=["phoebe"],context=['lcdep','rvdep','ifdep','spdep']),
         dict(qualifier='beaming',  description='Take photometric doppler shifts into account',repr='%s',value=False,cast_type='make_bool',frame=['phoebe'],context=['lcdep','ifdep','spdep']),
         dict(qualifier='time',     description='Timepoint LC',repr='%s',value=[],frame=["phoebe"],context='lcsyn'),
         dict(qualifier='flux',   description='Calculated flux',repr='%s',value=[],unit='erg/s/cm2',frame=["phoebe"],context='lcsyn'),
         dict(qualifier='filename', description='Name of the file containing the data',repr='%s',cast_type=str,value='',adjust=False,frame=['phoebe'],context=['lcobs','spobs','rvobs','ifobs','lcsyn','ifsyn','rvsyn','spsyn','ifobs','ifsyn']),
         dict(qualifier='ref',    description='Name of the data structure',repr='%s',cast_type=str,value='',frame=["phoebe"],context=['lcobs','rvobs','spobs','ifobs','psdep','lcsyn','spsyn','rvsyn','ifsyn']),
         dict(qualifier='time',     description='Timepoints of the data',repr='%s',cast_type=np.array,value=[],unit='JD',frame=['phoebe'],context=['lcobs','spobs','rvobs','ifobs']),
         dict(qualifier='flux',   description='Observed signal',repr='%s',cast_type=np.array,value=[],unit='erg/s/cm2/AA',frame=["phoebe"],context='lcobs'),
         dict(qualifier='sigma',  description='Data sigma',repr='%s',cast_type=np.array,value=[],unit='erg/s/cm2/AA',frame=['phoebe'],context=['lcobs','rvobs','lcsyn','rvsyn']),
         dict(qualifier='flag',    description='Signal flag',repr='%s',cast_type=np.array,value=[],frame=["phoebe"],context=['lcobs','rvobs']),
         dict(qualifier='weight',    description='Signal weight',repr='%s',cast_type=np.array,value=[],frame=["phoebe"],context=['lcobs','rvobs']),
         dict(qualifier='fittransfo',    description='Transform variable in fit',repr='%s',cast_type=str,value='linear',frame=["phoebe"],context=['lcobs']),
         dict(qualifier='columns',  description='Data columns',repr='%s',value=['time','flux','sigma','flag','weights'],frame=["phoebe"],context=['lcobs']),
         dict(qualifier='columns',  description='Data columns',repr='%s',value=['time','flux','sigma'],frame=["phoebe"],context=['lcsyn']),
         dict(qualifier='columns',  description='Data columns',repr='%s',value=['time','rv','sigma'],frame=["phoebe"],context=['rvobs']),
         dict(qualifier='rv',   description='Radial velocities',repr='%s',cast_type=np.array,value=[],frame=["phoebe"],context='rvobs'),
         dict(qualifier='rv',   description='Radial velocities',repr='%s',value=[],unit='Rsol/d',frame=["phoebe"],context='rvsyn'),
         dict(qualifier='columns',  description='Data columns',repr='%s',value=['time','rv'],frame=["phoebe"],context=['rvsyn']),
         dict(qualifier='columns',  description='Data columns',repr='%s',value=['wavelength','time','flux','continuum'],unit='nm',cast_type='return_list_of_strings',frame=["phoebe"],context=['spobs','spsyn']),
        ]

defs += [dict(qualifier='wavelength',description='Wavelengths of calculated spectrum',repr='%s',value=[],unit='nm',frame=["phoebe"],context='spobs'),
         dict(qualifier='continuum',  description='Continuum intensity of the spectrum',repr='%s',value=[],frame=["phoebe"],context='spobs'),
         dict(qualifier='flux',  description='Flux of the spectrum',repr='%s',value=[],frame=["phoebe"],context='spobs'),
         dict(qualifier='sigma',  description='Noise in the spectrum',repr='%s',value=[],frame=["phoebe"],context='spobs'),
         dict(qualifier='l3',       description='Third light',repr='%f',cast_type=float,value=0.,adjust=False,frame=["phoebe"],context=['lcobs','spobs','ifobs']),
         dict(qualifier='pblum',    description='Passband luminosity',repr='%f',cast_type=float,value=1.0,adjust=False,frame=["phoebe"],context=['lcobs','spobs','ifobs']),
         dict(qualifier='statweight',    description='Statistical weight in overall fitting',repr='%f',cast_type=float,value=1.0,adjust=False,frame=["phoebe"],context=['lcobs','spobs','ifobs']),
         ]        

        
defs += [dict(qualifier='ld_coeffs',description='Limb darkening coefficients',repr='%s',cast_type='return_string_or_list',value=[1.],frame=["phoebe"],context='rvdep'),
         dict(qualifier='passband', description='Photometric passband',repr='%s',value='JOHNSON.V',cast_type='make_upper',frame=["phoebe"],context='rvdep'),
         dict(qualifier='method',   description='Method for calculation of total intensity',repr='%s',cast_type='choose',choices=['analytical','numerical'],value='numerical',frame=["phoebe"],context='rvdep'),
         dict(qualifier='time',     description='Timepoint',repr='%s',value=[],frame=["phoebe"],context=['rvsyn','pssyn']),
        ]        

defs += [dict(qualifier='ld_func', description='Limb darkening model',repr='%s',cast_type=str,value='uniform',frame=["phoebe"],context='spdep'),
         dict(qualifier='ld_coeffs',description='Limb darkening coefficients',repr='%s',cast_type='return_string_or_list',value=[1.],frame=["phoebe"],context='spdep'),
         dict(qualifier='passband', description='Photometric passband',repr='%s',value='JOHNSON.V',cast_type='make_upper',frame=["phoebe"],context='spdep'),
         dict(qualifier='method',   description='Method for calculation of spectrum',repr='%s',cast_type='choose',choices=['analytical','numerical'],value='numerical',frame=["phoebe"],context='spdep'),
         dict(qualifier='clambda',   description='Central wavelength',repr='%s',unit='nm',cast_type=float,value=457.2,frame=["phoebe"],context='spdep'),
         dict(qualifier='max_velo', description='Maximum velocity in wavelength array',repr='%s',unit='km/s',cast_type=float,value=350,frame=["phoebe"],context='spdep'),
         dict(qualifier='R',        description='Resolving power lambda/Dlambda (or c/Deltav)',repr='%s',cast_type=float,value=400000.,frame=["phoebe"],context='spdep'),
         dict(qualifier='profile',  description='Line profile source (gridname or "gauss")',repr='%s',cast_type=str,value='gauss',frame=["phoebe"],context='spdep'),
         dict(qualifier='time',     description='Timepoint',repr='%s',value=[],frame=["phoebe"],context='spsyn'),
         dict(qualifier='wavelength',description='Wavelengths of calculated spectrum',repr='%s',value=[],unit='nm',frame=["phoebe"],context='spsyn'),
         dict(qualifier='flux',      description='Intensity of calculated spectrum',repr='%s',value=[],unit='erg/s/cm2',frame=["phoebe"],context='spsyn'),
         dict(qualifier='continuum', description='Continuum of calculated spectrum',repr='%s',value=[],unit='erg/s/cm2',frame=["phoebe"],context='spsyn'),
        ]

defs += [dict(qualifier='ld_func',   description='Limb darkening model',repr='%s',cast_type=str,value='uniform',frame=["phoebe"],context='ifdep'),
         dict(qualifier='ld_coeffs',         description='Limb darkening coefficients',repr='%s',cast_type='return_string_or_list',value=[1.],frame=["phoebe"],context='ifdep'),
         dict(qualifier='passband',   description='Photometric passband',repr='%s',cast_type='make_upper',value='JOHNSON.V',frame=["phoebe"],context='ifdep'),
         #dict(qualifier='baseline',   description='Length of the baseline',repr='%f',value=0.,unit='m',frame=["phoebe"],context=['ifobs','ifsyn']),
         #dict(qualifier='posangle',   description='Position angle of the baseline',repr='%f',value=0.,unit='deg',frame=["phoebe"],context=['ifobs','ifsyn']),
         #dict(qualifier='freq',  description='Cyclic frequency',repr='%s',value=[],unit='cy/arcsec',frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='ucoord',   description='U-coord',repr='%f',value=[],unit='m',frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='vcoord',   description='V-coords',repr='%f',value=[],unit='m',frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='vis', description='Visibility',repr='%s',value=[],frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='sigma_vis', description='Error on visibility',repr='%s',value=[],frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='phase',   description='Phase of visibility',repr='%s',value=[],frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='sigma_phase',   description='Error on phase of visibility',repr='%s',value=[],frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='columns',  description='Data columns',repr='%s',value=['time','baseline','posangle','vis','phase'],unit='nm',cast_type='return_list_of_strings',frame=["phoebe"],context=['ifobs','ifsyn']),
         dict(qualifier='time',     description='Timepoint',repr='%s',value=[],frame=["phoebe"],context='ifsyn'),
        ]

defs += [dict(qualifier='coordinates',description="Location of geometrical barycenter",cast_type=np.array,repr='%s',value=[0.,0.,0.],unit='Rsol',frame=["phoebe"],context=['point_source']),
         dict(qualifier='photocenter',description="Location of passband photocenter",cast_type=np.array,repr='%s',value=[0.,0.,0.],unit='Rsol',frame=["phoebe"],context=['point_source']),
         dict(qualifier='velocity',   description="Velocity of the body",repr='%s',cast_type=np.array,value=[0.,0.,0.],unit='km/s',frame=["phoebe"],context=['point_source']),
         dict(qualifier='distance',   description="Distance to the body",repr='%s',cast_type=float,value=0,unit='pc',frame=["phoebe"],context=['point_source']),
         dict(qualifier='radius',     description='Mean radius',repr='%s',value=0.,unit='Rsol',frame=["phoebe"],context=['point_source']),
         dict(qualifier='mass',       description="Mass of the body as a point source",repr='%s',value=0.,unit='Msol',frame=["phoebe"],context=['point_source']),
         dict(qualifier='teff',       description="passband mean temperature",repr='%s',value=0.,unit='K',frame=["phoebe"],context=['point_source']),
         dict(qualifier='surfgrav', description="passband mean surface gravity",repr='%s',value=0.,unit='[cm/s2]',frame=["phoebe"],context=['point_source']),
         dict(qualifier='intensity', description="passband mean intensity",repr='%s',value=0.,unit='erg/s/cm2',frame=["phoebe"],context=['point_source']),
        ]
        
defs += [dict(qualifier='coordinates',description="Location of the body's geometrical barycenter",repr='%s',value=[],unit='Rsol',frame=["phoebe"],context=['psdep']),
         dict(qualifier='photocenter',description="Location of the body's passband photocenter",repr='%s',value=[],unit='Rsol',frame=["phoebe"],context=['psdep']),
         dict(qualifier='velocity',   description="Velocity of the body",repr='%s',value=[],unit='Rsol/d',frame=["phoebe"],context=['psdep']),
         dict(qualifier='mass',       description="Mass of the body as a point source",repr='%s',value=[],unit='Msol',frame=["phoebe"],context=['psdep']),
         dict(qualifier='teff',       description="passband mean temperature",repr='%s',value=[],unit='K',frame=["phoebe"],context=['psdep']),
         dict(qualifier='surfgrav', description="passband mean surface gravity",repr='%s',value=[],unit='m/s2',frame=["phoebe"],context=['psdep']),
         dict(qualifier='intensity', description="passband mean intensity",repr='%s',value=[],unit='erg/s/cm2',frame=["phoebe"],context=['psdep']),
        ]

#    PULSATION contexts
defs += [dict(qualifier='freq',     description='Pulsation frequency',repr='%f',cast_type=float,value=1.,unit='cy/d',frame=["phoebe"],context='puls'),
         dict(qualifier='phase',    description='Pulsation phase',repr='%f',cast_type=float,value=0.,unit='cy',frame=["phoebe"],context='puls'),
         dict(qualifier='ampl',     description='Pulsation amplitude (fractional radius)',repr='%f',cast_type=float,value=0.01,frame=["phoebe"],context='puls'),
         dict(qualifier='l',        description='Degree of the mode',repr='%d',cast_type=int,value=3,frame=["phoebe"],context='puls'),
         dict(qualifier='m',        description='Azimuthal order of the mode',repr='%d',cast_type=int,value=2,frame=["phoebe"],context='puls'),
         dict(qualifier='k',        description='Horizontal/vertical displacement',repr='%f',cast_type=float,value=0.001,frame=["phoebe"],context='puls'),
         dict(qualifier='ledoux_coeff',description='Ledoux Cln',repr='%f',cast_type=float,value=0.,frame=['phoebe'],context='puls'),
         dict(qualifier='deltateff',description='Temperature perturbation',repr='%s',cast_type=complex,value=0.025+0j,frame=["phoebe"],context='puls'),
         dict(qualifier='deltagrav',description='Gravity perturbation',repr='%s',cast_type=complex,value=0.00001+0j,frame=["phoebe"],context='puls'),
         dict(qualifier='incl',     description='Angle between rotation and pulsation axis',unit='deg',repr='%f',llim=0,ulim=360,step=0.01,adjust=False,cast_type=float,value=0.,frame=["phoebe"],context='puls'),
         dict(qualifier='trad_coeffs',  description='B vector for traditional approximation',repr='%s',cast_type=np.array,value=[],frame=['phoebe'],context='puls'),
         dict(qualifier='scheme',   description='Type of approximation for description of pulsations',repr='%s',cast_type='choose',choices=['nonrotating','coriolis','traditional approximation'],value='nonrotating',frame=["phoebe"],context='puls'),
        ]

#    MAGNETIC FIELD contexts

defs += [dict(qualifier='Bpolar',     description='Polar magnetic field strength',repr='%f',cast_type=float,value=1.,unit='G',frame=["phoebe"],context='magnetic_field'),
         dict(qualifier='beta',       description='Magnetic field angle wrt rotation axis',repr='%f',cast_type=float,value=0.,unit='deg',frame=["phoebe"],context='magnetic_field'),
        ]

#    Accretion disk contexts        
defs += [dict(qualifier='dmdt',     description='Mass transfer rate',repr='%f',cast_type=float,value=1e-4,unit='Msol/yr',frame=["phoebe"],context='accretion_disk'),
         dict(qualifier='mass',     description='Host star mass',repr='%f',cast_type=float,value=1.,unit='Msol',frame=["phoebe"],context='accretion_disk'),
         dict(qualifier='rin',      description='Inner radius of disk',repr='%f',cast_type=float,value=1.,unit='Rsol',frame=["phoebe"],context='accretion_disk'),
         dict(qualifier='rout',     description='Outer radius of disk',repr='%f',cast_type=float,value=20.,unit='Rsol',frame=["phoebe"],context='accretion_disk'),
         dict(qualifier='height',   description='height of disk',repr='%f',cast_type=float,value=1e-2,unit='Rsol',frame=["phoebe"],context='accretion_disk'),
         dict(qualifier='b',        description='Host star rotation parameter',repr='%f',cast_type=float,value=1.,llim=0,ulim=1,frame=["phoebe"],context='accretion_disk'),
         dict(qualifier='distance', description='Distance to the disk',repr='%f',cast_type=float,value=10.,adjust=False,unit='pc',frame=['phoebe'],context='accretion_disk'),
        ]

#    Fitting contexts        
defs += [dict(qualifier='iters',     description='Number of iterations',repr='%d',cast_type=int,value=1000,frame=["phoebe"],context='fitting:pymc'),
         dict(qualifier='burn',     description='Burn parameter',repr='%d',cast_type=int,value=0,frame=["phoebe"],context='fitting:pymc'),
         dict(qualifier='thin',     description='Thinning parameter',repr='%d',cast_type=int,value=1,frame=["phoebe"],context='fitting:pymc'),
         dict(qualifier='feedback', description='Results from fitting procedure',repr='%s',cast_type=dict,value={},frame=["phoebe"],context='fitting:pymc'),
         dict(qualifier='incremental',description='Store results in a pickle file and start from previous results',repr='%s',cast_type='make_bool',value=False,frame=['phoebe'],context='fitting:pymc'),
         dict(qualifier='label',    description='Fit run name',repr='%s',cast_type=str,value='',frame=["phoebe"],context='fitting:pymc'),
        ]

defs += [dict(qualifier='iters',    description='Number of iterations',repr='%d',cast_type=int,value=1000,frame=["phoebe"],context='fitting:emcee'),
         dict(qualifier='burn',     description='Burn-in parameter',repr='%d',cast_type=int,value=0,frame=["phoebe"],context='fitting:emcee'),
         dict(qualifier='thin',     description='Thinning parameter',repr='%d',cast_type=int,value=1,frame=["phoebe"],context='fitting:emcee'),
         dict(qualifier='walkers',  description='Number of walkers',repr='%d',cast_type=int,value=6,frame=["phoebe"],context='fitting:emcee'),
         dict(qualifier='threads',  description='Number of threads',repr='%d',cast_type=int,value=1,frame=["phoebe"],context='fitting:emcee'),
         dict(qualifier='incremental',description='Store results in a file emcee_chain.label and start from previous results',repr='%s',cast_type='make_bool',value=False,frame=['phoebe'],context='fitting:emcee'),
         dict(qualifier='feedback', description='Results from fitting procedure',repr='%s',cast_type=dict,value={},frame=["phoebe"],context='fitting:emcee'),
         dict(qualifier='label',    description='Fit run name',repr='%s',cast_type=str,value='',frame=["phoebe"],context='fitting:emcee'),
        ]
        
defs += [dict(qualifier='method',    description='Nonlinear fitting method',repr='%s',cast_type='choose',value='leastsq',choices=['leastsq','nelder','lbfgsb','anneal','powell','cg','newton','cobyla','slsqp'],frame=["phoebe"],context='fitting:lmfit'),
         dict(qualifier='iters',     description='Number of iterations',repr='%d',cast_type=int,value=0,frame=["phoebe"],context='fitting:lmfit'),
         dict(qualifier='label',     description='Fit run name',repr='%s',cast_type=str,value='',frame=["phoebe"],context='fitting:lmfit'),
         dict(qualifier='compute_ci',description='Compute detailed confidence intervals',repr='%s',cast_type=bool,value=True,frame=["phoebe"],context='fitting:lmfit'),
         dict(qualifier='bounded',   description='Include boundaries in fit',repr='%s',cast_type=bool,value=True,frame=["phoebe"],context='fitting:lmfit'),
         dict(qualifier='feedback',  description='Results from fitting procedure',repr='%s',cast_type=dict,value={},frame=["phoebe"],context='fitting:lmfit'),
        ]

#    MPI and computation context
defs += [dict(qualifier='np',       description='Number of nodes',repr='%d',cast_type=int,value=4,frame=["phoebe"],context='mpi'),
         dict(qualifier='hostfile',     description='hostfile',repr='%s',cast_type=str,value='',frame=["phoebe"],context='mpi'),
         dict(qualifier='byslot',     description='byslot',repr='%s',cast_type='make_bool',value=True,frame=["phoebe"],context='mpi'),
         dict(qualifier='python',   description='Python executable',repr='%s',cast_type=str,value='python',frame=["phoebe"],context='mpi'),
        ]
        
#    Plotting context
defs += [dict(qualifier='ref',          description='Name of the data structure',repr='%s',cast_type=str,value='',frame=["phoebe"],context='plot'),
         dict(qualifier='type',         description='Whether plotting syn or obs dataset',repr='%s',cast_type=str,value='lcobs',frame=["phoebe"],context='plot'),
         dict(qualifier='color',        description='',repr='%s',cast_type=str,value='auto',frame=["phoebe"],context='plot'),
         dict(qualifier='marker',       description='',repr='%s',cast_type=str,value='.',frame=["phoebe"],context='plot'),
         dict(qualifier='markersize',   description='',repr='%d',cast_type=int,value=5,frame=["phoebe"],context='plot'),
         dict(qualifier='linestyle',    description='',repr='%s',cast_type=str,value='auto',frame=["phoebe"],context='plot'),
         dict(qualifier='linewidth',    description='',repr='%d',cast_type=int,value=1,frame=["phoebe"],context='plot'),
        ]
        
defs += [dict(qualifier='time',                 description='Compute observables of system at these times',repr='%s',value='auto',frame=["phoebe"],context='compute'),
         dict(qualifier='refs',                 description='Compute observables of system at these times',repr='%s',value='auto',frame=["phoebe"],context='compute'),
         dict(qualifier='types',                description='Compute observables of system at these times',repr='%s',value='auto',frame=["phoebe"],context='compute'),
         dict(qualifier='heating',              description='Allow irradiators to heat other Bodies',repr='%s',cast_type='make_bool',value=False,frame=['phoebe'],context='compute'),
         dict(qualifier='refl',                 description='Allow irradiated Bodies to reflect light',repr='%s',cast_type='make_bool',value=False,frame=['phoebe'],context='compute'),
         dict(qualifier='refl_num',             description='Number of reflections',repr='%d',cast_type=int,value=1,frame=['phoebe'],context='compute'),
         dict(qualifier='ltt',                  description='Correct for light time travel effects',repr='%s',cast_type='make_bool',value=False,frame=['phoebe'],context='compute'),
         dict(qualifier='subdiv_alg',           description='Subdivision algorithm',repr='%s',cast_type=str,value='edge',frame=["phoebe"],context='compute'),
         dict(qualifier='subdiv_num',           description='Number of subdivisions',repr='%d',cast_type=int,value=3,frame=["phoebe"],context='compute'),
         dict(qualifier='eclipse_alg',          description='Type of eclipse algorithm',choices=['auto','full','convex'],cast_type='choose',value='auto',frame=['phoebe'],context='compute'),
        ]        

        
#  /* ********************* DERIVABLE QUANTITIES ********************************* */
defs += [dict(qualifier='tdyn',   description='Dynamical timescale',repr='%f',cast_type=float,value=0,frame=['phoebe'],context='derived'),
         dict(qualifier='ttherm', description='Thermal timescale',  repr='%f',cast_type=float,value=0,frame=['phoebe'],context='derived'),
        ]
        

constraints = {'phoebe':{}}        
constraints['phoebe']['orbit'] = ['{sma1} = {sma} / (1.0 + 1.0/{q})',
                         '{sma2} = {sma} / (1.0 + {q})',
                         '{totalmass} = 4*pi**2 * {sma}**3 / {period}**2 / constants.GG',
                         '{mass1} = 4*pi**2 * {sma}**3 / {period}**2 / constants.GG / (1.0 + {q})',
                         '{mass2} = 4*pi**2 * {sma}**3 / {period}**2 / constants.GG / (1.0 + 1.0/{q})',
                         '{asini} = {sma} * sin({incl})',
                         '{com} = {q}/(1.0+{q})*{sma}',
                         '{q1} = {q}',
                         '{q2} = 1.0/{q}',
                         #'{circum} = 4*{sma1}*special.ellipk({ecc})/{period}',
                         ]
constraints['phoebe']['star'] = ['{surfgrav} = constants.GG*{mass}/{radius}**2',
#                                 '{angdiam} = 2*{radius}/{distance}',
                        ]