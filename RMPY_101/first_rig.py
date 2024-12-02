from RMPY.rig import rigFK
from RMPY.rig import rigIK
import pymel.core as pm



# my_rig = rigFK.RigFK()
my_rig = rigIK.IKRig()
my_rig.create_point_base('C_test00_reference_pnt', 'C_test01_reference_pnt', 'C_test02_reference_pnt', 'C_test03_reference_pnt')