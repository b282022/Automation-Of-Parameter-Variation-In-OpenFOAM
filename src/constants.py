LIST_OF_ALL_OPENFOAM_SOLVERS = ['simpleFoam',
                                'pimpleFoam',
                                'shallowWaterFoam',
                                'sonicFoam',
                                'cavitatingFoam',
                                'laplacianFoam',
                                'potentialFoam',
                                'scalarTransportFoam',
                                'adjointShapeOptimizationFoam',
                                'boundaryFoam',
                                'icoFoam',
                                'nonNewtonianIcoFoam',
                                'pimpleFoam',
                                'pimpleDyMFoam',
                                'SRFPimpleFoam',
                                'pisoFoam',
                                'shallowWaterFoam',
                                'simpleFoam',
                                'porousSimpleFoam',
                                'SRFSimpleFoam',
                                'rhoCentralFoam',
                                'rhoCentralDyMFoam',
                                'rhoPimpleFoam',
                                'rhoPimpleDyMFoam',
                                'rhoSimpleFoam',
                                'rhoPorousSimpleFoam',
                                'sonicFoam',
                                'sonicDyMFoam',
                                'sonicLiquidFoam',
                                'cavitatingFoam',
                                'cavitatingDyMFoam',
                                'compressibleInterFoam',
                                'compressibleInterDyMFoam',
                                'compressibleMultiphaseInterFoam',
                                'driftFluxFoam',
                                'interFoam',
                                'interDyMFoam',
                                'interMixingFoam',
                                'interIsoFoam',
                                'interFoam',
                                'interPhaseChangeFoam',
                                'interPhaseChangeDyMFoam',
                                'MPPICInterFoam',
                                'multiphaseEulerFoam',
                                'multiphaseInterFoam',
                                'multiphaseInterDyMFoam',
                                'potentialFreeSurfaceFoam',
                                'potentialFreeSurfaceDyMFoam',
                                'reactingMultiphaseEulerFoam',
                                'reactingTwoPhaseEulerFoam',
                                'twoLiquidMixingFoam',
                                'twoPhaseEulerFoam',
                                'dnsFoam',
                                'chemFoam',
                                'coldEngineFoam',
                                'engineFoam',
                                'fireFoam',
                                'PDRFoam',
                                'reactingFoam',
                                'rhoReactingBuoyantFoam',
                                'rhoReactingFoam',
                                'XiFoam',
                                'XiDyMFoam',
                                'buoyantBoussinesqPimpleFoam',
                                'buoyantBoussinesqSimpleFoam',
                                'buoyantPimpleFoam',
                                'buoyantSimpleFoam',
                                'chtMultiRegionFoam',
                                'chtMultiRegionSimpleFoam',
                                'thermoFoam',
                                'coalChemistryFoam',
                                'DPMFoam',
                                'DPMDyMFoam',
                                'MPPICDyMFoam',
                                'MPPICFoam',
                                'icoUncoupledKinematicParcelFoam',
                                'icoUncoupledKinematicParcelDyMFoam',
                                'reactingParcelFilmFoam',
                                'reactingParcelFoam',
                                'simpleReactingParcelFoam',
                                'simpleCoalParcelFoam',
                                'sprayFoam',
                                'sprayDyMFoam',
                                'sprayEngineFoam',
                                'uncoupledKinematicParcelFoam',
                                'mdEquilibrationFoam',
                                'mdFoam',
                                'dsmcFoam',
                                'electrostaticFoam',
                                'magneticFoam',
                                'mhdFoam',
                                'solidDisplacementFoam',
                                'solidEquilibriumDisplacementFoam',
                                'financialFoam']


def exists_solver(solver_name):
    """
    Helper function to check if the solver's name entered by user is correct or not
    :param solver_name: Name of the solver to be searched
    :return bool: If solver exists in OpenFOAM then return True else return False

    :Examples:
        >>> exists_solver('icoFoam')
            True
        >>> exists_solver('someGarbageSolver')
            False
    """
    if solver_name in LIST_OF_ALL_OPENFOAM_SOLVERS:
        return True
    return False
