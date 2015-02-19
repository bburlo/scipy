"""
Sane parameters for stats.distributions.
"""

distcont = [
    ['alpha', (3.5704770516650459,)],
    ['anglit', ()],
    ['arcsine', ()],
    ['beta', (2.3098496451481823, 0.62687954300963677)],
    ['betaprime', (5, 6)],
    ['bradford', (0.29891359763170633,)],
    ['burr', (10.5, 4.3)],
    ['cauchy', ()],
    ['chi', (78,)],
    ['chi2', (55,)],
    ['cosine', ()],
    ['dgamma', (1.1023326088288166,)],
    ['dweibull', (2.0685080649914673,)],
    ['erlang', (10,)],
    ['expon', ()],
    ['expongauss', (1.0,)],
    ['exponpow', (2.697119160358469,)],
    ['exponweib', (2.8923945291034436, 1.9505288745913174)],
    ['f', (29, 18)],
    ['fatiguelife', (29,)],   # correction numargs = 1
    ['fisk', (3.0857548622253179,)],
    ['foldcauchy', (4.7164673455831894,)],
    ['foldnorm', (1.9521253373555869,)],
    ['frechet_l', (3.6279911255583239,)],
    ['frechet_r', (1.8928171603534227,)],
    ['gamma', (1.9932305483800778,)],
    ['gausshyper', (13.763771604130699, 3.1189636648681431,
                    2.5145980350183019, 5.1811649903971615)],  # veryslow
    ['genexpon', (9.1325976465418908, 16.231956600590632, 3.2819552690843983)],
    ['genextreme', (-0.1,)],
    ['gengamma', (4.4162385429431925, 3.1193091679242761)],
    ['genhalflogistic', (0.77274727809929322,)],
    ['genlogistic', (0.41192440799679475,)],
    ['genpareto', (0.1,)],   # use case with finite moments
    ['gilbrat', ()],
    ['gompertz', (0.94743713075105251,)],
    ['gumbel_l', ()],
    ['gumbel_r', ()],
    ['halfcauchy', ()],
    ['halflogistic', ()],
    ['halfnorm', ()],
    ['hypsecant', ()],
    ['invgamma', (4.0668996136993067,)],
    ['invgauss', (0.14546264555347513,)],
    ['invweibull', (10.58,)],
    ['johnsonsb', (4.3172675099141058, 3.1837781130785063)],
    ['johnsonsu', (2.554395574161155, 2.2482281679651965)],
    ['ksone', (1000,)],  # replace 22 by 100 to avoid failing range, ticket 956
    ['kstwobign', ()],
    ['laplace', ()],
    ['levy', ()],
    ['levy_l', ()],
    ['levy_stable', (0.35667405469844993,
                     -0.67450531578494011)],  # NotImplementedError
    #           rvs not tested
    ['loggamma', (0.41411931826052117,)],
    ['logistic', ()],
    ['loglaplace', (3.2505926592051435,)],
    ['lognorm', (0.95368226960575331,)],
    ['lomax', (1.8771398388773268,)],
    ['maxwell', ()],
    ['mielke', (10.4, 3.6)],
    ['nakagami', (4.9673794866666237,)],
    ['ncf', (27, 27, 0.41578441799226107)],
    ['nct', (14, 0.24045031331198066)],
    ['ncx2', (21, 1.0560465975116415)],
    ['norm', ()],
    ['pareto', (2.621716532144454,)],
    ['pearson3', (0.1,)],
    ['powerlaw', (1.6591133289905851,)],
    ['powerlognorm', (2.1413923530064087, 0.44639540782048337)],
    ['powernorm', (4.4453652254590779,)],
    ['rayleigh', ()],
    ['rdist', (0.9,)],   # feels also slow
    ['recipinvgauss', (0.63004267809369119,)],
    ['reciprocal', (0.0062309367010521255, 1.0062309367010522)],
    ['rice', (0.7749725210111873,)],
    ['semicircular', ()],
    ['t', (2.7433514990818093,)],
    ['triang', (0.15785029824528218,)],
    ['truncexpon', (4.6907725456810478,)],
    ['truncnorm', (-1.0978730080013919, 2.7306754109031979)],
    ['truncnorm', (0.1, 2.)],
    ['tukeylambda', (3.1321477856738267,)],
    ['uniform', ()],
    ['vonmises', (3.9939042581071398,)],
    ['vonmises_line', (3.9939042581071398,)],
    ['wald', ()],
    ['weibull_max', (2.8687961709100187,)],
    ['weibull_min', (1.7866166930421596,)],
    ['wrapcauchy', (0.031071279018614728,)]]


distdiscrete = [
    ['bernoulli',(0.3,)],
    ['binom', (5, 0.4)],
    ['boltzmann',(1.4, 19)],
    ['dlaplace', (0.8,)],  # 0.5
    ['geom', (0.5,)],
    ['hypergeom',(30, 12, 6)],
    ['hypergeom',(21,3,12)],  # numpy.random (3,18,12) numpy ticket:921
    ['hypergeom',(21,18,11)],  # numpy.random (18,3,11) numpy ticket:921
    ['logser', (0.6,)],  # reenabled, numpy ticket:921
    ['nbinom', (5, 0.5)],
    ['nbinom', (0.4, 0.4)],  # from tickets: 583
    ['planck', (0.51,)],   # 4.1
    ['poisson', (0.6,)],
    ['randint', (7, 31)],
    ['skellam', (15, 8)],
    ['zipf', (6.5,)]
]
